# 🚀 DATABUTTON PROJECT SUBMISSION

## PROJECT OVERVIEW
**Name**: TikTok Hook Generator
**Type**: Full-Stack AI Web Application
**Purpose**: Generate viral TikTok hook lines using AI to help content creators boost engagement

## 🎯 NATURAL LANGUAGE PROJECT DESCRIPTION FOR DATABUTTON AI

Create a full-stack web application that generates viral TikTok hook lines using AI. The app should have a beautiful, modern interface with the following features:

### CORE FUNCTIONALITY:
1. **Two Input Methods**:
   - Topic-based generation (user enters a topic like "fitness tips")
   - Transcript-based generation (user pastes video transcript or content)

2. **AI Hook Generation**:
   - Generate 3-10 viral TikTok hooks per request
   - Use psychological triggers (curiosity, shock, FOMO, secrets)
   - Keep hooks under 15 words for optimal TikTok format
   - Focus on scroll-stopping, engagement-driving content

3. **User Interface**:
   - Clean, modern design with purple/pink gradient theme
   - Tab-based navigation (Topic vs Transcript)
   - Dropdown to select number of hooks (3, 5, 7, 10)
   - Large generate button with loading states
   - Results displayed as numbered list with copy buttons

4. **Progressive Web App (PWA)**:
   - Install button for iPhone/mobile devices
   - Offline functionality with template-based fallback
   - Works like a native app when installed
   - Mobile-optimized responsive design

5. **Smart Features**:
   - Copy individual hooks to clipboard
   - Copy all hooks at once
   - Online/offline status indicators
   - Graceful fallback when API is unavailable
   - Error handling with user-friendly messages

### TECHNICAL REQUIREMENTS:
- **Frontend**: React with modern UI components
- **Backend**: FastAPI with OpenRouter AI integration
- **Styling**: Tailwind CSS with custom gradients
- **AI Integration**: OpenRouter API (openrouter/auto model)
- **PWA Features**: Service worker, manifest, offline capability
- **Mobile-First**: iPhone optimized, add-to-homescreen ready

### USER EXPERIENCE FLOW:
1. User visits the app
2. Chooses between "Topic" or "Transcript" input
3. Enters their content (topic or transcript text)
4. Selects number of hooks to generate
5. Clicks "Generate Viral Hooks"
6. Sees loading animation with encouraging text
7. Gets 5 professionally crafted hooks displayed beautifully
8. Can copy individual hooks or all at once
9. Can install as PWA for native app experience

### HOOK GENERATION STRATEGY:
The AI should generate hooks using proven viral patterns:
- "This [topic] hack will blow your mind"
- "Nobody talks about this [topic] secret"
- "You're doing [topic] wrong - here's why"
- "This changes everything about [topic]"
- Use numbers, questions, and bold statements
- Create curiosity gaps without spoiling content
- Focus on emotional triggers and psychology

### OFFLINE FEATURES:
When internet is unavailable, the app should:
- Detect offline status
- Use pre-built template system
- Generate hooks using smart word substitution
- Show offline indicator to user
- Maintain full functionality

### DEPLOYMENT REQUIREMENTS:
- Custom domain preferred (something like tiktokHooks.app)
- PWA optimized for iPhone Safari
- Fast loading times
- Scalable infrastructure
- SSL certificate
- Mobile-responsive across all devices

This should be a professional-grade application that content creators would pay for, with a beautiful interface and reliable AI-powered hook generation.