#!/usr/bin/env python3
"""
iPhone-Optimized TikTok Hook Generator
Lightweight version that could theoretically run on mobile with Python
"""

import json
import random
from typing import List, Dict

class MobileHookGenerator:
    def __init__(self):
        self.templates = [
            "This {topic} hack will {effect}",
            "Nobody talks about this {topic} secret",
            "You're doing {topic} wrong - here's what {experts} do",
            "This {duration} {topic} trick changes everything",
            "The {topic} mistake that's {problem}",
            "Why {experts} {action} this {topic} method",
            "This {topic} discovery will shock you",
            "The {topic} secret that went viral",
            "Most people don't know this {topic} fact",
            "This simple {topic} change {effect}"
        ]
        
        self.word_banks = {
            'effect': ['blow your mind', 'change everything', 'transform your life', 'shock you', 'amaze you'],
            'experts': ['professionals', 'experts', 'coaches', 'successful people', 'pros'],
            'duration': ['5-minute', '10-second', '30-day', '1-hour', 'instant'],
            'action': ['swear by', 'secretly use', 'recommend', 'prefer', 'choose'],
            'problem': ['ruining your progress', 'holding you back', 'costing you', 'sabotaging you']
        }
    
    def generate_hooks(self, topic: str, count: int = 5) -> List[str]:
        """Generate hooks using template substitution"""
        hooks = []
        
        for _ in range(count):
            template = random.choice(self.templates)
            
            # Replace placeholders
            hook = template.format(
                topic=topic.lower(),
                effect=random.choice(self.word_banks.get('effect', ['amaze you'])),
                experts=random.choice(self.word_banks.get('experts', ['experts'])),
                duration=random.choice(self.word_banks.get('duration', ['instant'])),
                action=random.choice(self.word_banks.get('action', ['use'])),
                problem=random.choice(self.word_banks.get('problem', ['limiting you']))
            )
            
            # Capitalize first letter
            hook = hook[0].upper() + hook[1:] if hook else hook
            hooks.append(hook)
        
        return hooks
    
    def generate_from_keywords(self, keywords: List[str], count: int = 5) -> List[str]:
        """Generate hooks from extracted keywords"""
        hooks = []
        
        simple_templates = [
            "This {keyword} will change everything",
            "Nobody talks about {keyword}",
            "The {keyword} secret everyone missed",
            "This {keyword} discovery is viral",
            "Why {keyword} is the game-changer"
        ]
        
        for i in range(count):
            keyword = random.choice(keywords) if keywords else "method"
            template = random.choice(simple_templates)
            hook = template.format(keyword=keyword)
            hooks.append(hook.capitalize())
        
        return hooks
    
    def export_for_ios(self, hooks: List[str]) -> str:
        """Export hooks in iOS-friendly format"""
        ios_output = {
            "hooks": hooks,
            "count": len(hooks),
            "format": "tiktok_hooks",
            "timestamp": "generated_on_device"
        }
        return json.dumps(ios_output, indent=2)

# Main execution for mobile/lightweight use
def main():
    generator = MobileHookGenerator()
    
    # Example usage
    topic = "fitness tips"
    hooks = generator.generate_hooks(topic, 5)
    
    print("📱 Mobile TikTok Hook Generator")
    print("=" * 40)
    print(f"Topic: {topic}")
    print("=" * 40)
    
    for i, hook in enumerate(hooks, 1):
        print(f"{i}. {hook}")
    
    print("=" * 40)
    print("✅ Generated successfully!")
    
    # Export for iOS
    ios_format = generator.export_for_ios(hooks)
    print("\n📱 iOS Export Format:")
    print(ios_format)

if __name__ == "__main__":
    main()