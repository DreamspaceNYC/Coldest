# 🔧 TECHNICAL SPECIFICATIONS

## ENVIRONMENT VARIABLES NEEDED:
```
OPENROUTER_API_KEY=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
```

## API INTEGRATION DETAILS:

### OpenRouter API Configuration:
- **Endpoint**: https://openrouter.ai/api/v1/chat/completions
- **Model**: "openrouter/auto" (automatically selects best model)
- **Temperature**: 0.8 (high creativity for viral content)
- **Max Tokens**: 500
- **Authentication**: Bearer token in header

### Request Format:
```json
{
  "model": "openrouter/auto",
  "messages": [
    {"role": "user", "content": "Generate 5 viral TikTok hooks for: fitness tips"}
  ],
  "temperature": 0.8,
  "max_tokens": 500
}
```

## BACKEND API ENDPOINTS NEEDED:

### POST /api/generate-hooks
**Request Body:**
```json
{
  "topic": "string (optional)",
  "transcript": "string (optional)", 
  "count": "integer (3-10)"
}
```

**Response:**
```json
{
  "hooks": ["hook1", "hook2", "hook3"],
  "source_type": "topic|transcript",
  "source_content": "brief description"
}
```

## FRONTEND REQUIREMENTS:

### Components Needed:
1. **Header**: Title, description, install button
2. **Tab Navigation**: Topic vs Transcript input
3. **Input Section**: Text field or textarea based on tab
4. **Count Selector**: Dropdown for 3, 5, 7, 10 hooks
5. **Generate Button**: With loading states and animations
6. **Results Display**: Numbered list with copy buttons
7. **Status Indicators**: Online/offline, loading states
8. **PWA Elements**: Install prompt, offline indicators

### Styling Requirements:
- **Colors**: Purple to pink gradients (#8b5cf6 to #ec4899)
- **Layout**: Clean, modern, mobile-first
- **Typography**: Clear hierarchy, readable fonts
- **Animations**: Smooth transitions, loading spinners
- **Responsive**: Works perfectly on iPhone, tablet, desktop

## PWA CONFIGURATION:

### Manifest.json:
```json
{
  "name": "TikTok Hook Generator",
  "short_name": "TikTokHooks",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#8b5cf6",
  "start_url": "/",
  "orientation": "portrait"
}
```

### Service Worker Features:
- Cache static assets
- Offline hook generation fallback
- Background sync when connection returns
- Install prompt handling

## DEPLOYMENT SPECIFICATIONS:

### Infrastructure:
- **Frontend**: Static hosting with CDN
- **Backend**: Serverless or containerized API
- **Database**: None required (stateless application)
- **SSL**: Required for PWA functionality
- **Domain**: Custom domain preferred

### Performance Requirements:
- **Loading**: < 3 seconds on mobile
- **API Response**: < 5 seconds for hook generation
- **Offline**: Instant template-based generation
- **Mobile**: 90+ Lighthouse score

### Security:
- API key stored server-side only
- CORS properly configured
- Input validation and sanitization
- Rate limiting on API endpoints

## TESTING REQUIREMENTS:

### Manual Testing Needed:
1. Generate hooks from various topics
2. Generate hooks from transcript text
3. Test offline functionality
4. Test PWA installation on iPhone
5. Verify copy-to-clipboard functionality
6. Test responsive design across devices

### Expected Performance:
- 5 hooks generated in < 5 seconds
- Offline fallback in < 1 second
- PWA install prompt appears on mobile
- All features work in iPhone Safari