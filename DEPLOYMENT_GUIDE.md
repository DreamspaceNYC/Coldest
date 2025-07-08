# TikTok Hook Generator - Deployment Guide

## 📋 Project Overview
- **Name**: TikTok Hook Generator
- **Type**: Full-stack web application
- **Purpose**: Generate viral TikTok hooks using AI

## 🏗️ Architecture
- **Backend**: FastAPI (Python)
- **Frontend**: React (JavaScript)
- **API**: OpenRouter AI integration
- **Database**: None required (stateless)

## 📁 File Structure
```
tiktok-hook-generator/
├── backend/
│   ├── server.py          # Main FastAPI app
│   ├── requirements.txt   # Python dependencies
│   └── .env              # Environment variables
├── frontend/
│   ├── src/
│   │   ├── App.js        # Main React component
│   │   └── App.css       # Styling
│   ├── public/
│   └── package.json      # Node dependencies
└── README.md
```

## 🔧 Technical Requirements

### Backend Requirements
- **Python**: 3.9+
- **Framework**: FastAPI
- **Dependencies**: 
  - fastapi
  - requests
  - python-dotenv
  - uvicorn
- **Port**: 8001

### Frontend Requirements
- **Node.js**: 16+
- **Framework**: React 18
- **Build Tool**: Create React App
- **Port**: 3000

## 🌐 Environment Variables
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

## 🚀 Deployment Commands

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8001
```

### Frontend
```bash
cd frontend
npm install
npm run build  # For production
npm start      # For development
```

## 📊 Resource Requirements
- **Memory**: 512MB minimum
- **CPU**: 1 core minimum
- **Storage**: 100MB
- **Network**: Outbound HTTPS (for API calls)

## 🔒 Security Notes
- API key stored in environment variables
- CORS configured for cross-origin requests
- No sensitive data stored locally

## 🧪 Testing
- Backend endpoint: `http://localhost:8001`
- Frontend: `http://localhost:3000`
- API test: `POST /api/generate-hooks`

## 📞 Support
- Contact for deployment issues
- OpenRouter API documentation
- React/FastAPI documentation references