#!/usr/bin/env python3
"""
Simple working scraper using the exact same approach as our successful test
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import urllib3

# Disable SSL warnings for this test
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_whoppah_content(url):
    """Simple scraper using the working approach from our test"""
    
    print(f"Scraping: {url}")
    
    # Add headers and disable SSL verification for testing
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    response = requests.get(url, headers=headers, verify=False, timeout=30)
    print(f"Status: {response.status_code}, Size: {len(response.content)} bytes")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Remove scripts and styles (but keep nav/header/footer like the test)
    for element in soup(['script', 'style']):
        element.decompose()
    
    # Find content using exact same approach as successful test
    content_paragraphs = soup.find_all('p', class_=lambda x: x and 'font-body' in x and 'text-sm' in x)
    content_headings = soup.find_all(['h1', 'h2', 'h3'], class_=lambda x: x and 'font-title' in x and 'font-bold' in x)
    
    print(f"Found {len(content_paragraphs)} content paragraphs")
    print(f"Found {len(content_headings)} content headings")
    
    # Extract content
    result = {
        'url': url,
        'scraped_at': datetime.now().isoformat(),
        'page_title': '',
        'section_headings': [],
        'category_description': '',
        'seo_content': '',
        'debug': {
            'total_paragraphs': len(content_paragraphs),
            'total_headings': len(content_headings)
        }
    }
    
    # Get page title
    title_tag = soup.find('title')
    if title_tag:
        result['page_title'] = title_tag.get_text().strip()
    
    # Extract headings
    for h in content_headings:
        text = h.get_text().strip()
        if len(text) > 3:
            result['section_headings'].append(text)
    
    # Extract paragraph content
    paragraphs = []
    for p in content_paragraphs:
        text = p.get_text().strip()
        if len(text) > 20:
            paragraphs.append(text)
    
    if paragraphs:
        result['category_description'] = "\n\n".join(paragraphs[:3])
        if len(paragraphs) > 3:
            result['seo_content'] = "\n\n".join(paragraphs[3:])
    
    return result

if __name__ == "__main__":
    test_url = "https://www.whoppah.com/furniture"
    
    result = scrape_whoppah_content(test_url)
    
    print("\n" + "="*50)
    print("RESULTS:")
    print(f"Title: {result['page_title']}")
    print(f"Headings found: {len(result['section_headings'])}")
    print(f"Description length: {len(result['category_description'])}")
    print(f"SEO content length: {len(result['seo_content'])}")
    
    if result['section_headings']:
        print("\nSample headings:")
        for h in result['section_headings'][:3]:
            print(f"  - {h}")
    
    if result['category_description']:
        print(f"\nSample description: {result['category_description'][:200]}...")
    
    # Save result
    with open('simple_test_result.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nResult saved to simple_test_result.json")