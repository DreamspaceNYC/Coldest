import React, { useState, useEffect } from 'react';
import './App.css';

// PWA Service Worker Registration
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then((registration) => {
        console.log('SW registered: ', registration);
      })
      .catch((registrationError) => {
        console.log('SW registration failed: ', registrationError);
      });
  });
}

function App() {
  const [activeTab, setActiveTab] = useState('topic');
  const [topic, setTopic] = useState('');
  const [transcript, setTranscript] = useState('');
  const [count, setCount] = useState(5);
  const [hooks, setHooks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [sourceInfo, setSourceInfo] = useState('');

  const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8001';

  const generateHooks = async () => {
    if (!topic && !transcript) {
      setError('Please provide either a topic or transcript');
      return;
    }

    setLoading(true);
    setError('');
    setHooks([]);

    try {
      const response = await fetch(`${backendUrl}/api/generate-hooks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          topic: activeTab === 'topic' ? topic : null,
          transcript: activeTab === 'transcript' ? transcript : null,
          count: count,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate hooks');
      }

      const data = await response.json();
      setHooks(data.hooks);
      setSourceInfo(`Generated ${data.hooks.length} hooks from ${data.source_type}: "${data.source_content}"`);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    // You could add a toast notification here
  };

  const copyAllHooks = () => {
    const allHooks = hooks.map((hook, index) => `${index + 1}. ${hook}`).join('\n');
    navigator.clipboard.writeText(allHooks);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-10">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            🚀 TikTok Hook Generator
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Generate viral TikTok hook lines that stop scrollers in their tracks. 
            Perfect for content creators, marketers, and anyone looking to boost engagement.
          </p>
        </div>

        {/* Main Content */}
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8">
            {/* Tab Navigation */}
            <div className="flex space-x-1 mb-8 bg-gray-100 rounded-lg p-1">
              <button
                onClick={() => setActiveTab('topic')}
                className={`flex-1 py-3 px-4 rounded-md font-medium transition-all ${
                  activeTab === 'topic'
                    ? 'bg-white text-purple-600 shadow-sm'
                    : 'text-gray-600 hover:text-gray-800'
                }`}
              >
                🎯 Generate from Topic
              </button>
              <button
                onClick={() => setActiveTab('transcript')}
                className={`flex-1 py-3 px-4 rounded-md font-medium transition-all ${
                  activeTab === 'transcript'
                    ? 'bg-white text-purple-600 shadow-sm'
                    : 'text-gray-600 hover:text-gray-800'
                }`}
              >
                📝 Generate from Transcript
              </button>
            </div>

            {/* Input Section */}
            <div className="mb-8">
              {activeTab === 'topic' ? (
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-3">
                    Enter your topic:
                  </label>
                  <input
                    type="text"
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    placeholder="e.g., productivity tips for students, cooking hacks, fitness motivation..."
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 outline-none transition-all"
                  />
                </div>
              ) : (
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-3">
                    Paste your transcript:
                  </label>
                  <textarea
                    value={transcript}
                    onChange={(e) => setTranscript(e.target.value)}
                    placeholder="Paste your video transcript, podcast notes, or any text content here..."
                    rows="6"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 outline-none transition-all resize-none"
                  />
                </div>
              )}
            </div>

            {/* Count Selector */}
            <div className="mb-8">
              <label className="block text-sm font-medium text-gray-700 mb-3">
                Number of hooks to generate:
              </label>
              <select
                value={count}
                onChange={(e) => setCount(parseInt(e.target.value))}
                className="px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 outline-none"
              >
                {[3, 5, 7, 10].map((num) => (
                  <option key={num} value={num}>
                    {num} hooks
                  </option>
                ))}
              </select>
            </div>

            {/* Generate Button */}
            <button
              onClick={generateHooks}
              disabled={loading || (!topic && !transcript)}
              className="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white font-medium py-4 px-6 rounded-lg hover:from-purple-700 hover:to-pink-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all transform hover:scale-105 shadow-lg"
            >
              {loading ? (
                <div className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Generating Viral Hooks...
                </div>
              ) : (
                '✨ Generate Viral Hooks'
              )}
            </button>

            {/* Error Message */}
            {error && (
              <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
                <div className="flex items-center">
                  <svg className="h-5 w-5 text-red-400 mr-2" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                  </svg>
                  <span className="text-red-700">{error}</span>
                </div>
              </div>
            )}

            {/* Results Section */}
            {hooks.length > 0 && (
              <div className="mt-8">
                <div className="flex justify-between items-center mb-4">
                  <h2 className="text-xl font-semibold text-gray-800">
                    🎉 Your Viral Hooks
                  </h2>
                  <button
                    onClick={copyAllHooks}
                    className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors flex items-center space-x-2"
                  >
                    <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                    <span>Copy All</span>
                  </button>
                </div>

                {sourceInfo && (
                  <p className="text-sm text-gray-600 mb-4">{sourceInfo}</p>
                )}

                <div className="space-y-4">
                  {hooks.map((hook, index) => (
                    <div
                      key={index}
                      className="bg-gradient-to-r from-purple-50 to-pink-50 p-4 rounded-lg border border-purple-100 hover:shadow-md transition-shadow"
                    >
                      <div className="flex justify-between items-start">
                        <div className="flex-1">
                          <span className="text-lg font-medium text-purple-600 mr-3">
                            {index + 1}.
                          </span>
                          <span className="text-gray-800">{hook}</span>
                        </div>
                        <button
                          onClick={() => copyToClipboard(hook)}
                          className="ml-4 p-2 text-gray-400 hover:text-purple-600 transition-colors"
                          title="Copy hook"
                        >
                          <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                          </svg>
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="text-center mt-12 text-gray-500">
          <p>Powered by OpenRouter AI • Built for Content Creators</p>
        </div>
      </div>
    </div>
  );
}

export default App;