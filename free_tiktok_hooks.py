#!/usr/bin/env python3
"""
FREE TikTok Hook Generator - No API Required
Uses pre-built templates and word combinations
"""

import random
import argparse
import sys

# Hook templates with placeholders
HOOK_TEMPLATES = [
    "This {topic} hack will {impact} your {outcome}",
    "Nobody talks about this {topic} secret that {impact}",
    "You're doing {topic} wrong - here's what {experts} do",
    "This {time} {topic} trick {impact} everything",
    "The {topic} mistake that's {negative_impact}",
    "Why {experts} {action} this {topic} method",
    "This changes everything about {topic}",
    "You won't believe what happens when you {action}",
    "The {topic} secret that went viral",
    "This {number}-{time} {topic} hack {impact}",
    "Most people don't know this {topic} trick",
    "This {topic} method {impact} in just {time}",
    "The {topic} rule that {impact} everything",
    "Why your {topic} isn't working (and how to fix it)",
    "This simple {topic} change {impact} my entire {outcome}"
]

# Word banks for different categories
WORD_BANKS = {
    'impact': ['will blow your mind', 'changes everything', 'transforms', 'revolutionizes', 'will shock you'],
    'outcome': ['life', 'routine', 'results', 'success', 'mindset', 'productivity', 'game'],
    'experts': ['professionals', 'experts', 'coaches', 'trainers', 'successful people'],
    'time': ['5-minute', '10-second', '30-day', '1-hour', 'overnight', 'instant'],
    'action': ['try this', 'do this', 'apply this', 'use this method', 'follow this'],
    'negative_impact': ['ruining your progress', 'holding you back', 'sabotaging your success'],
    'number': ['3', '5', '7', '10', 'simple', 'secret']
}

def generate_hooks_free(topic, count=5):
    """Generate hooks using templates and word substitution"""
    hooks = []
    
    # Clean topic for better insertion
    topic_clean = topic.lower().strip()
    
    # Generate hooks using templates
    for _ in range(count):
        template = random.choice(HOOK_TEMPLATES)
        
        # Replace placeholders with topic and random words
        hook = template.format(
            topic=topic_clean,
            impact=random.choice(WORD_BANKS['impact']),
            outcome=random.choice(WORD_BANKS['outcome']),
            experts=random.choice(WORD_BANKS['experts']),
            time=random.choice(WORD_BANKS['time']),
            action=random.choice(WORD_BANKS['action']),
            negative_impact=random.choice(WORD_BANKS['negative_impact']),
            number=random.choice(WORD_BANKS['number'])
        )
        
        # Capitalize first letter
        hook = hook[0].upper() + hook[1:]
        hooks.append(hook)
    
    return hooks

def generate_from_transcript_free(transcript, count=5):
    """Generate hooks from transcript using keyword extraction"""
    # Simple keyword extraction
    keywords = []
    important_words = ['secret', 'mistake', 'discovered', 'changed', 'amazing', 'shocking', 'simple', 'powerful']
    
    words = transcript.lower().split()
    for word in words:
        if len(word) > 6 and word not in ['the', 'and', 'but', 'that', 'this', 'with', 'from']:
            keywords.append(word)
    
    # If no good keywords found, use general templates
    if not keywords:
        keywords = ['method', 'technique', 'approach', 'strategy', 'system']
    
    hooks = []
    templates = [
        "This {keyword} will change how you think about everything",
        "Nobody talks about the {keyword} that actually works",
        "The {keyword} secret that everyone missed",
        "This {keyword} discovery will blow your mind",
        "Why this {keyword} changes everything"
    ]
    
    for i in range(count):
        keyword = random.choice(keywords[:5])  # Use first 5 keywords
        template = random.choice(templates)
        hook = template.format(keyword=keyword)
        hook = hook[0].upper() + hook[1:]
        hooks.append(hook)
    
    return hooks

def main():
    parser = argparse.ArgumentParser(description="FREE TikTok Hook Generator - No API Required")
    parser.add_argument("--topic", "-t", type=str, help="Topic to generate hooks for")
    parser.add_argument("--transcript", "-f", type=str, help="Path to transcript file")
    parser.add_argument("--count", "-c", type=int, default=5, help="Number of hooks to generate")
    
    args = parser.parse_args()
    
    if not args.topic and not args.transcript:
        print("❌ Please provide either --topic or --transcript")
        sys.exit(1)
    
    print("🎯 FREE TikTok Hook Generator")
    print("=" * 50)
    
    try:
        if args.topic:
            print(f"📝 Generating {args.count} hooks for: '{args.topic}'")
            hooks = generate_hooks_free(args.topic, args.count)
        else:
            with open(args.transcript, 'r') as f:
                transcript = f.read()
            print(f"📄 Generating {args.count} hooks from transcript")
            hooks = generate_from_transcript_free(transcript, args.count)
        
        print("\n🚀 YOUR VIRAL HOOKS:")
        print("=" * 50)
        for i, hook in enumerate(hooks, 1):
            print(f"{i}. {hook}")
        
        print("=" * 50)
        print(f"✅ Generated {len(hooks)} hooks successfully!")
        print("💡 Tip: Run multiple times for different variations!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()