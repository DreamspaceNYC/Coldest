from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import requests
import time
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="TikTok Hook Generator API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OpenRouterClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is required")
        
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_text(self, prompt: str, model: str = "openrouter/auto", 
                     temperature: float = 0.8, max_tokens: int = 500) -> str:
        """Generate text using OpenRouter API with retry logic"""
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json=payload,
                    timeout=45
                )
                response.raise_for_status()
                
                result = response.json()
                return result["choices"][0]["message"]["content"]
                
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception("Request timed out after multiple attempts")
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception(f"OpenRouter API error: {str(e)}")
            except KeyError as e:
                raise Exception(f"Unexpected API response format: {str(e)}")

class HookRequest(BaseModel):
    topic: Optional[str] = None
    transcript: Optional[str] = None
    count: int = 5

class HookResponse(BaseModel):
    hooks: List[str]
    source_type: str
    source_content: str

def parse_hooks(response: str, count: int) -> List[str]:
    """Parse the API response to extract clean hook lines"""
    hooks = []
    lines = response.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
            # Remove numbering/bullets and clean up
            if '.' in line and line[0].isdigit():
                hook = line.split('.', 1)[1].strip()
            else:
                hook = line.lstrip('- •0123456789.').strip()
            
            # Clean up formatting
            hook = hook.strip('"*')  # Remove quotes and asterisks
            hook = hook.split('**')[0].strip()  # Remove bold markdown
            hook = hook.split('[')[0].strip()  # Remove brackets and content
            hook = hook.split('(')[0].strip()  # Remove parentheses explanations
            
            if hook and len(hook) > 10 and len(hook) < 150:  # Filter reasonable length
                hooks.append(hook)
    
    # If we didn't get enough hooks from parsing, try a different approach
    if len(hooks) < count:
        # Split by common delimiters and filter
        all_text = response.replace('\n', ' ').replace('\t', ' ')
        sentences = [s.strip() for s in all_text.split('.') if s.strip()]
        
        for sentence in sentences:
            sentence = sentence.lstrip('- •0123456789').strip()
            sentence = sentence.strip('"*')
            sentence = sentence.split('**')[0].strip()
            sentence = sentence.split('[')[0].strip()
            sentence = sentence.split('(')[0].strip()
            
            if sentence and len(sentence) > 10 and len(sentence) < 150:
                # Avoid duplicates
                if sentence not in hooks:
                    hooks.append(sentence)
                    if len(hooks) >= count:
                        break
    
    return hooks[:count]  # Return exactly the requested count

@app.get("/")
async def root():
    return {"message": "TikTok Hook Generator API is running!"}

@app.post("/api/generate-hooks", response_model=HookResponse)
async def generate_hooks(request: HookRequest):
    """Generate viral TikTok hooks from topic or transcript"""
    try:
        if not request.topic and not request.transcript:
            raise HTTPException(status_code=400, detail="Either topic or transcript is required")
        
        if request.topic and request.transcript:
            raise HTTPException(status_code=400, detail="Please provide either topic OR transcript, not both")
        
        client = OpenRouterClient()
        
        if request.topic:
            prompt = f"""
Generate {request.count} viral TikTok hook lines for the topic: "{request.topic}"

Requirements:
- Each hook should be attention-grabbing and under 15 words
- Use psychological triggers like curiosity, shock, or FOMO
- Include numbers, questions, or bold statements when appropriate
- Make them scroll-stopping and engaging
- Focus on creating hooks that would make people stop scrolling
- Use patterns like "You won't believe...", "This changes everything...", "Nobody talks about..."
- Format as a numbered list (1. 2. 3. etc.)

Topic: {request.topic}

Generate exactly {request.count} hooks:
"""
            source_type = "topic"
            source_content = request.topic
        else:
            prompt = f"""
Generate {request.count} viral TikTok hook lines based on this content: "{request.transcript[:500]}"

Requirements:
- Each hook should be attention-grabbing and under 15 words
- Use psychological triggers like curiosity, shock, or FOMO
- Include numbers, questions, or bold statements when appropriate
- Make them scroll-stopping and engaging
- Focus on creating hooks that would make people stop scrolling
- Format as a numbered list (1. 2. 3. etc.)

Generate exactly {request.count} hooks:
"""
            source_type = "transcript"
            source_content = request.transcript[:100] + "..." if len(request.transcript) > 100 else request.transcript
        
        response = client.generate_text(
            prompt=prompt,
            temperature=0.8,
            max_tokens=500
        )
        
        hooks = parse_hooks(response, request.count)
        
        if not hooks:
            # Fallback with sample hooks for demo
            if request.topic:
                hooks = [
                    f"This {request.topic} hack will blow your mind",
                    f"Nobody talks about this {request.topic} secret",
                    f"You're doing {request.topic} wrong - here's why",
                    f"This changes everything about {request.topic}",
                    f"The {request.topic} trick that went viral"
                ][:request.count]
            else:
                hooks = [
                    "This story will change how you think about everything",
                    "Nobody talks about what really happened next",
                    "You won't believe what I discovered",
                    "This changes everything I thought I knew",
                    "The secret that everyone missed"
                ][:request.count]
        
        return HookResponse(
            hooks=hooks,
            source_type=source_type,
            source_content=source_content
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)