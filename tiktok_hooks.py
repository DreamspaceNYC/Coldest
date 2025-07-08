#!/usr/bin/env python3
"""
TikTok Hook Generator CLI Tool
Generates viral TikTok hook lines using OpenRouter API
"""

import os
import requests
import argparse
import sys
import time
import random
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
                    timeout=45  # Increased timeout
                )
                response.raise_for_status()
                
                result = response.json()
                return result["choices"][0]["message"]["content"]
                
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"⏳ Request timeout, retrying in {wait_time:.1f}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception("Request timed out after multiple attempts")
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                    print(f"⏳ API error, retrying in {wait_time:.1f}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception(f"OpenRouter API error: {str(e)}")
            except KeyError as e:
                raise Exception(f"Unexpected API response format: {str(e)}")

class TikTokHookGenerator:
    def __init__(self):
        self.client = OpenRouterClient()
        
    def generate_hooks_from_topic(self, topic: str, count: int = 5) -> List[str]:
        """Generate viral TikTok hooks from a topic"""
        prompt = f"""
Generate {count} viral TikTok hook lines for the topic: "{topic}"

Requirements:
- Each hook should be attention-grabbing and under 15 words
- Use psychological triggers like curiosity, shock, or FOMO
- Include numbers, questions, or bold statements when appropriate
- Make them scroll-stopping and engaging
- Focus on creating hooks that would make people stop scrolling
- Use patterns like "You won't believe...", "This changes everything...", "Nobody talks about..."
- Format as a numbered list (1. 2. 3. etc.)

Topic: {topic}

Generate exactly {count} hooks:
"""
        
        response = self.client.generate_text(
            prompt=prompt,
            temperature=0.8,  # Higher creativity for viral content
            max_tokens=500
        )
        
        # Parse the response to extract individual hooks
        hooks = self._parse_hooks(response, count)
        return hooks
    
    def generate_hooks_from_transcript(self, transcript: str, count: int = 5) -> List[str]:
        """Generate viral TikTok hooks from a transcript"""
        # Use the same approach as topic-based generation
        prompt = f"""
Generate {count} viral TikTok hook lines based on this content: "{transcript[:500]}"

Requirements:
- Each hook should be attention-grabbing and under 15 words
- Use psychological triggers like curiosity, shock, or FOMO
- Include numbers, questions, or bold statements when appropriate
- Make them scroll-stopping and engaging
- Focus on creating hooks that would make people stop scrolling
- Format as a numbered list (1. 2. 3. etc.)

Generate exactly {count} hooks:
"""
        
        response = self.client.generate_text(
            prompt=prompt,
            temperature=0.8,
            max_tokens=400
        )
        
        hooks = self._parse_hooks(response, count)
        return hooks
    
    def _parse_hooks(self, response: str, count: int) -> List[str]:
        """Parse the API response to extract clean hook lines"""
        hooks = []
        lines = response.strip().split('\n')
        
        # Debug
        print(f"DEBUG - Response length: {len(response)}")
        print(f"DEBUG - Lines: {lines}")
        
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
        
        print(f"DEBUG - Final hooks: {hooks}")
        return hooks[:count]  # Return exactly the requested count

def main():
    parser = argparse.ArgumentParser(
        description="Generate viral TikTok hooks using OpenRouter API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tiktok_hooks.py --topic "productivity tips for students"
  python tiktok_hooks.py --transcript podcast_transcript.txt --count 7
  python tiktok_hooks.py -t "cooking hacks" -c 3
        """
    )
    parser.add_argument("--topic", "-t", type=str, help="Topic to generate hooks for")
    parser.add_argument("--transcript", "-f", type=str, help="Path to transcript file")
    parser.add_argument("--count", "-c", type=int, default=5, help="Number of hooks to generate (default: 5)")
    
    args = parser.parse_args()
    
    if not args.topic and not args.transcript:
        print("❌ Error: Please provide either --topic or --transcript")
        print("\nUsage examples:")
        print("  python tiktok_hooks.py --topic 'fitness tips'")
        print("  python tiktok_hooks.py --transcript transcript.txt")
        sys.exit(1)
    
    if args.topic and args.transcript:
        print("❌ Error: Please provide either --topic OR --transcript, not both")
        sys.exit(1)
    
    try:
        generator = TikTokHookGenerator()
        
        if args.topic:
            print(f"🎯 Generating {args.count} viral TikTok hooks for topic: '{args.topic}'")
            print("🔄 Processing...")
            hooks = generator.generate_hooks_from_topic(args.topic, args.count)
        else:
            # Read transcript from file
            try:
                with open(args.transcript, 'r', encoding='utf-8') as f:
                    transcript_content = f.read()
                
                if not transcript_content.strip():
                    print(f"❌ Error: Transcript file '{args.transcript}' is empty")
                    sys.exit(1)
                
                print(f"📄 Generating {args.count} viral TikTok hooks from transcript: '{args.transcript}'")
                print("🔄 Processing...")
                hooks = generator.generate_hooks_from_transcript(transcript_content, args.count)
            except FileNotFoundError:
                print(f"❌ Error: Transcript file '{args.transcript}' not found")
                sys.exit(1)
            except Exception as e:
                print(f"❌ Error reading transcript file: {str(e)}")
                sys.exit(1)
        
        # Display results
        print("\n" + "="*60)
        print("🚀 VIRAL TIKTOK HOOKS")
        print("="*60)
        
        if hooks:
            for i, hook in enumerate(hooks, 1):
                print(f"{i}. {hook}")
        else:
            print("❌ No hooks were generated. Please try a different topic or check your transcript.")
            
        print("="*60)
        print(f"✅ Generated {len(hooks)} hooks successfully!")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nTroubleshooting:")
        print("- Check your OpenRouter API key in .env file")
        print("- Ensure you have internet connection")
        print("- Try a simpler topic or shorter transcript")
        sys.exit(1)

if __name__ == "__main__":
    main()