# TikTok Hook Generator CLI Tool

A Python CLI tool that generates viral TikTok hook lines using OpenRouter API. Takes a topic or transcript as input and returns 5 engaging hook lines designed to stop scrollers and increase engagement.

## Features

- 🎯 Generate hooks from any topic
- 📄 Process transcript files
- 🔄 Uses OpenRouter's auto-select for best model
- 🔒 Secure API key management with .env
- 📝 Clean formatted output
- ⚡ Fast and efficient

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your OpenRouter API key:
   - Get your API key from https://openrouter.ai/dashboard
   - The API key is already configured in `.env` file

## Usage

### Generate hooks from a topic:
```bash
python tiktok_hooks.py --topic "productivity tips for students"
python tiktok_hooks.py -t "cooking hacks" --count 7
```

### Generate hooks from a transcript file:
```bash
python tiktok_hooks.py --transcript podcast_transcript.txt
python tiktok_hooks.py -f interview.txt --count 3
```

### Options:
- `--topic, -t`: Topic to generate hooks for
- `--transcript, -f`: Path to transcript file
- `--count, -c`: Number of hooks to generate (default: 5)

## Examples

```bash
# Basic usage
python tiktok_hooks.py --topic "fitness motivation"

# Custom count
python tiktok_hooks.py --topic "investment tips" --count 10

# From transcript
python tiktok_hooks.py --transcript my_podcast.txt
```

## Sample Output

```
🎯 Generating 5 viral TikTok hooks for topic: 'productivity tips for students'
🔄 Processing...

============================================================
🚀 VIRAL TIKTOK HOOKS
============================================================
1. This productivity hack helped me get straight A's in college
2. Nobody talks about this study method that actually works
3. You're studying wrong - here's what successful students do differently
4. This 5-minute morning routine changed my entire academic life
5. The productivity secret that professors don't want you to know
============================================================
✅ Generated 5 hooks successfully!
```

## API Usage

The tool uses OpenRouter's API with the `openrouter/auto` model for optimal results. Each hook is optimized for:
- Maximum engagement
- Psychological triggers (curiosity, FOMO, shock)
- Scroll-stopping power
- Under 15 words for TikTok format

## Error Handling

The tool includes robust error handling for:
- Missing API keys
- Network issues
- Invalid files
- API rate limits

## Security

- API keys are stored in `.env` file
- Never commit API keys to version control
- Add `.env` to your `.gitignore`