#!/usr/bin/env python3
import emoji
import sys

def search_emojis(keyword):
    """Search for emojis containing a keyword in their name"""
    keyword = keyword.lower()
    results = []
    
    for emoji_char, data in emoji.EMOJI_DATA.items():
        if keyword in data['en'].lower():
            results.append(f"{emoji_char} :{data['en']}:")
    
    if results:
        print(f"\nFound {len(results)} emojis with '{keyword}':")
        print("-" * 40)
        for result in results:
            print(result)
    else:
        print(f"No emojis found with '{keyword}'")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_emojis(sys.argv[1])
    else:
        print("Usage: python3 emoji_search.py <keyword>")
        print("Example: python3 emoji_search.py money")




        # grep -i "money" all_emojis.txt
