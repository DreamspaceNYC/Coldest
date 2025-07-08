🚀 TikTok Hook Generator - Complete Databutton Package

I want to build a professional TikTok Hook Generator that helps content creators generate viral hook lines using AI.

## WHAT I WANT BUILT:

A beautiful, fast web application with these features:

### CORE FUNCTIONALITY:
- **Two Input Methods**: Topic-based ("fitness tips") or Transcript-based (paste video content)
- **AI Hook Generation**: Generate 3-10 viral TikTok hooks using OpenRouter AI
- **Smart Prompting**: Uses psychology triggers (curiosity, shock, FOMO) for viral content
- **Progressive Web App**: Installs like native iPhone app, works offline
- **Copy Features**: Individual hook copy + copy all hooks
- **Responsive Design**: Perfect on mobile, tablet, desktop

### USER EXPERIENCE:
1. Beautiful landing page with purple/pink gradient design
2. Tab navigation between "Topic" and "Transcript" input
3. Clean input fields with helpful placeholders
4. Dropdown to select 3, 5, 7, or 10 hooks
5. Large "Generate Viral Hooks" button with loading animation
6. Results display as numbered list with copy buttons
7. Install button for iPhone PWA functionality
8. Offline indicator when internet unavailable

### TECHNICAL REQUIREMENTS:
- **Frontend**: React + Tailwind CSS + Modern UI
- **Backend**: FastAPI + OpenRouter AI integration
- **AI Model**: openrouter/auto (automatically selects best model)
- **PWA Features**: Manifest + Service Worker + Offline capability
- **Mobile**: iPhone optimized, add-to-homescreen ready
- **Performance**: < 3 second loading, < 5 second hook generation

## ENVIRONMENT VARIABLES NEEDED:
```
OPENROUTER_API_KEY=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
```

## AI INTEGRATION DETAILS:
- **API**: https://openrouter.ai/api/v1/chat/completions
- **Model**: "openrouter/auto"
- **Temperature**: 0.8 (high creativity)
- **Max Tokens**: 500
- **Request Format**: Standard OpenAI-compatible chat completion

## EXAMPLE PROMPTS FOR AI:
```
Generate 5 viral TikTok hook lines for the topic: "fitness tips"

Requirements:
- Each hook under 15 words
- Use psychological triggers (curiosity, shock, FOMO)
- Include numbers, questions, or bold statements
- Make them scroll-stopping and engaging
- Format as numbered list

Examples of good hooks:
- "This fitness hack will blow your mind"
- "Nobody talks about this workout secret"
- "You're doing cardio wrong - here's why"
```

## OFFLINE FUNCTIONALITY:
When no internet, use template-based generation:
- "This [topic] hack will blow your mind"
- "Nobody talks about this [topic] secret" 
- "You're doing [topic] wrong - here's why"
- Smart word substitution for engaging hooks

## DEPLOYMENT PREFERENCES:
- **Custom Domain**: Something like tiktokHooks.app or viralHooks.com
- **PWA Optimized**: Perfect iPhone Safari experience
- **SSL Certificate**: Required for PWA features
- **Fast Performance**: Mobile-optimized loading
- **Scalable**: Ready for high traffic

## SUCCESS CRITERIA:
✅ Installs on iPhone like native app
✅ Generates viral hooks in < 5 seconds
✅ Works offline with templates
✅ Professional design creators would pay for
✅ Copy-to-clipboard works perfectly
✅ Mobile-responsive across all devices

This should feel like a premium tool that content creators and marketers would actually use and potentially pay for. Focus on user experience, reliability, and beautiful design.

## EXISTING CODE REFERENCE:
I have working code you can build upon or reference - it's a complete React + FastAPI implementation. Feel free to rebuild from scratch using your platform's capabilities or enhance what I have.

Let me know if you need any clarification or additional details!