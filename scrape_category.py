#!/usr/bin/env python3
"""
Simple script to scrape any Whoppah category page
Usage: python scrape_category.py [URL or category]
"""

import sys
from simple_working_scraper import scrape_whoppah_content
import json

def main():
    if len(sys.argv) < 2:
        print("🔍 Whoppah Category Scraper")
        print("=" * 30)
        print("\nUsage:")
        print("  python scrape_category.py [URL or category]")
        print("\nExamples:")
        print("  python scrape_category.py furniture")
        print("  python scrape_category.py decoration/vases")
        print("  python scrape_category.py style/vintage")
        print("  python scrape_category.py https://www.whoppah.com/lighting")
        print("\nPopular categories:")
        print("  • furniture")
        print("  • lighting")
        print("  • decoration")
        print("  • decoration/vases")
        print("  • art")
        print("  • style/vintage")
        print("  • style/mid-century-modern")
        return
    
    input_arg = sys.argv[1]
    
    # Convert category to full URL if needed
    if input_arg.startswith('http'):
        url = input_arg
        category = input_arg.replace('https://www.whoppah.com/', '')
    else:
        category = input_arg.strip('/')
        url = f"https://www.whoppah.com/{category}"
    
    print(f"🔍 Scraping: {category}")
    print("=" * 50)
    
    try:
        result = scrape_whoppah_content(url)
        
        print(f"\n✅ SUCCESS!")
        print(f"Title: {result['page_title']}")
        print(f"Headings: {len(result['section_headings'])}")
        print(f"Content length: {len(result['category_description']) + len(result['seo_content'])} chars")
        
        if result['section_headings']:
            print(f"\nHeadings found:")
            for i, heading in enumerate(result['section_headings'], 1):
                print(f"  {i}. {heading}")
        
        if result['category_description']:
            print(f"\nFirst 300 chars:")
            preview = result['category_description'][:300]
            print(f"  {preview}{'...' if len(result['category_description']) > 300 else ''}")
        
        # Save to file
        filename = f"{category.replace('/', '_')}_content.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Saved to: {filename}")
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main() or 0)