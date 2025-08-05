# 🏺 Whoppah.com Content Scraper

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-working-brightgreen.svg)

A Python tool to extract SEO content from Whoppah.com listing pages. Successfully extracts rich, structured content that appears at the bottom of category pages for SEO analysis and content auditing.

> **🎯 Perfect for**: SEO professionals, content marketers, and developers who need to analyze existing content on e-commerce category pages.

## 🎯 What It Does

This tool extracts the valuable SEO content from Whoppah's category pages, including:

**Real Example from `/decoration/vases`:**
- **Title**: "Vases | Whoppah"
- **6 Section Headings**: "Vases", "History", "What does it do to us?", "Contemporary", "In short"  
- **2,391 characters** of clean, structured content
- **Rich descriptions**: "Vases are more than just decorative objects; they are the perfect complement to the natural beauty of flowers..."

**Content Types Extracted:**
- Category descriptions and storytelling
- Historical context and background
- Product usage and styling tips
- Brand messaging and value propositions
- Contemporary design trends
- Emotional and lifestyle content

## 🚀 What's Working

✅ **Clean Content Extraction**: Successfully extracts readable, structured content (no garbled text)  
✅ **Multiple Tools**: Simple command-line tool + full-featured scraper  
✅ **All Major Categories**: furniture, lighting, decoration, art, style categories  
✅ **Rich Content**: 2,000-4,000 characters per page with headings and descriptions  
✅ **JSON Output**: Structured data ready for analysis  
✅ **SSL Handling**: Works with Whoppah's security settings  

## 📊 Proven Results

| Category | Headings | Content | Key Sections |
|----------|----------|---------|--------------|
| 🪑 **Furniture** | 9 headings | 3,707 chars | "Second-hand design furniture", "Special furniture for everyone" |
| 💡 **Lighting** | 8 headings | 3,044 chars | "Design lighting: stylish mood makers", "Create optical illusion" |  
| 🏺 **Vases** | 6 headings | 2,391 chars | "History", "Contemporary", "What does it do to us?" |

## 📁 Project Structure

```
whoppah-scraper/
├── scrape_category.py           # 🎯 Main CLI tool (START HERE)
├── simple_working_scraper.py    # Core scraping functions
├── config.py                   # URL configurations (80+ categories)
├── requirements.txt            # Python dependencies
├── examples/
│   └── sample_output.json      # Example of scraped content
├── LICENSE                     # MIT License
├── README.md                   # This documentation
├── .gitignore                  # Git ignore rules
└── output/ (generated):
    ├── furniture_content.json      # Generated when you scrape
    ├── decoration_vases_content.json
    └── ...more category files
```

## ✨ Features

- 🚀 **Simple CLI**: One command to scrape any category
- 🤖 **GitHub Actions**: Manual cloud scraping (no local setup needed!)
- 🎯 **Targeted Extraction**: Focuses on bottom SEO content sections  
- 📊 **Structured Output**: Clean JSON with headings and descriptions
- 🛡️ **Robust**: Handles SSL, encoding, and rate limiting
- 🔧 **Configurable**: 80+ predefined category URLs
- 📝 **Rich Content**: 2,000-4,000 characters per page typically
- 🔄 **On-Demand**: Manual scraping when you need it

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/your-username/whoppah-scraper.git
cd whoppah-scraper

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Scrape Content
```bash
# Scrape any category
python scrape_category.py furniture
python scrape_category.py decoration/vases  
python scrape_category.py style/vintage

# See all available categories
python scrape_category.py --help
```

### 3. View Results
```bash
# Content automatically saved as JSON files
cat furniture_content.json    # Rich furniture descriptions
cat decoration_vases_content.json  # Vases content & history
```

**Example output**: See [`examples/sample_output.json`](examples/sample_output.json) for what gets extracted.

## 📋 Popular Categories

**Main Categories:**
- `furniture` - Second-hand design furniture, quality info
- `lighting` - Designer lamps, mood setting tips  
- `decoration` - Home decor items and styling
- `art` - Artwork and decorative pieces

**Specific Subcategories:**
- `decoration/vases` - Vase history, contemporary design
- `furniture/chairs` - Chair types, styling tips
- `furniture/sofas` - Sofa buying guide, room styling
- `lighting/pendant-lamps` - Pendant lighting trends

**Style Categories:**
- `style/vintage` - Vintage furniture history and value
- `style/mid-century-modern` - MCM design principles
- `style/scandinavian` - Nordic design philosophy

## 📄 Output Format

Each scrape produces a JSON file with this structure:

```json
{
  "url": "https://www.whoppah.com/decoration/vases",
  "page_title": "Vases | Whoppah",
  "section_headings": [
    "Vases", "History", "What does it do to us?", 
    "Contemporary", "In short"
  ],
  "category_description": "Vases are more than just decorative objects...",
  "seo_content": "In modern interior design, vases are more versatile...",
  "scraped_at": "2025-08-05T14:19:05.057774"
}
```

## 🎮 Usage Options

### Option 1: Single Category (Recommended)

**Scrape one category at a time:**
```bash
python scrape_category.py furniture           # Main category
python scrape_category.py decoration/vases    # Subcategory
python scrape_category.py style/vintage       # Style category
```

### Option 2: Multiple Categories

**Scrape multiple categories one by one:**
```bash
python scrape_category.py furniture
python scrape_category.py lighting  
python scrape_category.py decoration/vases
python scrape_category.py style/vintage
```

### Option 3: GitHub Actions (Cloud Scraping) 🤖

**No local setup required!** Use GitHub's cloud infrastructure:

1. **Fork this repository** on GitHub
2. **Go to Actions tab** in your fork  
3. **Choose a workflow**:
   - **🔍 Scrape Content**: Multiple categories at once
   - **🎯 Manual Scrape**: Single category with dropdown
   - **🧪 Test Scraper**: Validate setup
4. **Click "Run workflow"** and customize options
5. **Download results** from the Artifacts section

**Perfect for**: On-demand scraping, team collaboration, no local dependencies.

### Option 4: Programmatic Usage

```python
from simple_working_scraper import scrape_whoppah_content

# Scrape a single page
result = scrape_whoppah_content('https://www.whoppah.com/decoration/vases')

print(f"Title: {result['page_title']}")
print(f"Headings: {len(result['section_headings'])}")
print(f"Content: {result['category_description'][:200]}...")
```

## 🤖 GitHub Actions Usage

### Available Workflows

**1. 🔍 Multi-Category Scraping** (`scrape-content.yml`)
- Scrape multiple categories in one run
- Default: furniture, lighting, decoration/vases, style/vintage
- Customize categories via input field
- Results stored as downloadable artifacts
- Optional: commit results back to repository

**2. 🎯 Single Category Scraping** (`manual-scrape.yml`)  
- Quick single-category scraping
- Dropdown menu with 11 popular categories
- Immediate results in workflow logs
- Perfect for testing or one-off needs

**3. 🧪 Setup Testing** (`test-scraper.yml`)
- Validates Python environment and dependencies
- Runs on code changes (PRs/pushes)
- Ensures everything works before scraping

### How to Use GitHub Actions

**Step 1: Fork Repository**
```bash
1. Go to https://github.com/your-username/whoppah-scraper
2. Click "Fork" button
3. Enable GitHub Actions in your fork (if prompted)
```

**Step 2: Run Workflows**
```bash
1. Go to "Actions" tab in your forked repository
2. Select a workflow:
   - "🔍 Scrape Whoppah Content" - for multiple categories
   - "🎯 Manual Scrape" - for single category
3. Click "Run workflow"
4. Customize inputs (optional)
5. Click green "Run workflow" button
```

**Step 3: Download Results**
```bash
1. Wait 2-5 minutes for workflow to complete
2. Scroll to "Artifacts" section in completed run
3. Download the zip file containing JSON results
4. Extract files to view scraped content
```

### GitHub Actions Benefits

- ✅ **No Local Setup**: Works immediately after forking
- ✅ **Cloud Infrastructure**: Uses GitHub's servers, not your computer
- ✅ **Free Usage**: Unlimited for public repositories
- ✅ **Team Collaboration**: Multiple people can trigger scrapes
- ✅ **Automatic Storage**: Results kept for 30 days
- ✅ **Professional Logs**: Detailed execution information

### Workflow Results

**Multi-Category Scraping Output:**
```json
scraped_data/
├── furniture_content.json
├── lighting_content.json  
├── decoration_vases_content.json
├── style_vintage_content.json
└── SUMMARY.md
```

**Single Category Output:**
```json
furniture_content.json  # Downloaded as artifact
```

### Customization Options

**Multi-Category Workflow:**
- **Categories**: Comma-separated list (e.g., "furniture,lighting,art")
- **Commit Results**: Save results back to repository (true/false)

**Single Category Workflow:**
- **Category**: Choose from dropdown menu of popular categories

### Troubleshooting GitHub Actions

**Workflow Failed:**
- Check logs for specific error messages
- Verify category names exist on Whoppah.com
- May be temporary site or network issues

**No Artifacts:**
- Ensure workflow completed successfully
- Check if scraper found content for chosen categories
- Some categories may have different page structures

**Rate Limiting:**
- GitHub Actions includes respectful delays
- If blocked, wait and try again later
- Consider reducing number of categories per run

## ⚡ What To Expect

**Typical Results Per Page:**
- **Processing Time**: 2-5 seconds per page
- **Content Volume**: 2,000-4,000 characters of text
- **Structure**: 6-10 section headings + rich descriptions
- **Success Rate**: 95%+ on major category pages

**Content Quality Examples:**
- **Furniture**: "Second-hand furniture is an option that is taking the interior design world by storm..."
- **Lighting**: "Lighting comes in all shapes and sizes. It ranges from pendant lights, to ceiling lights..."
- **Vases**: "Vases are more than just decorative objects; they are the perfect complement to natural beauty..."

## 📊 Output Data

The scraper extracts the following information for each page:

| Field | Description |
|-------|-------------|
| `url` | The URL of the scraped page |
| `page_title` | HTML title tag content |
| `main_heading` | Main H1 heading |
| `category_description` | Main descriptive content |
| `seo_content` | Additional SEO text content |
| `section_headings` | List of all H2-H6 headings |
| `bullet_points` | Extracted bullet points and lists |
| `metadata` | Meta tags (description, keywords, og tags) |
| `response_status` | HTTP response code |
| `page_size` | Size of the page in bytes |
| `scraped_at` | Timestamp of when scraped |

## 🎯 Categories Covered

The scraper covers all major Whoppah.com sections:

### Main Categories
- Furniture
- Lighting
- Decoration
- Art
- Tableware

### Style Categories
- Vintage Design
- Mid Century Modern
- Italian Design
- Scandinavian
- Memphis
- Hollywood Regency

### Detailed Subcategories
- 40+ furniture subcategories (chairs, sofas, tables, etc.)
- 9+ lighting subcategories (pendant lamps, table lamps, etc.)
- 13+ decoration subcategories (vases, mirrors, etc.)
- 7+ art subcategories (paintings, sculptures, etc.)
- Collections and curated lists

## ⚙️ Configuration

Modify `config.py` to customize the scraper:

```python
# Adjust delay between requests
DEFAULT_DELAY = 2  # seconds

# Add/remove categories to scrape
MAIN_CATEGORIES = [
    '/furniture',
    '/lighting',
    # Add more categories...
]

# Configure content extraction
MIN_PARAGRAPH_LENGTH = 50  # Minimum chars for substantial content
```

## 📈 Sample Output

**CSV Output Sample:**
```csv
url,page_title,main_heading,category_description,section_headings
https://www.whoppah.com/furniture,Second hand furniture | Whoppah,Second hand furniture,"At Whoppah, we do our best to offer you...",Second-hand design furniture; Special second-hand furniture
```

**JSON Output Sample:**
```json
{
  "url": "https://www.whoppah.com/furniture",
  "page_title": "Second hand furniture | Whoppah",
  "main_heading": "Second hand furniture",
  "category_description": "At Whoppah, we do our best to offer you the most unique...",
  "section_headings": ["Second-hand design furniture", "Special, second-hand furniture"],
  "bullet_points": [],
  "metadata": {
    "description": "Buy second hand furniture at Whoppah...",
    "og:title": "Second hand furniture"
  },
  "scraped_at": "2025-01-11T10:30:00"
}
```

## 🔍 What Content Gets Extracted

The scraper focuses on the **bottom content** of listing pages, specifically:

1. **Category Descriptions**: Text explaining what the category is about
2. **SEO Content**: Marketing copy and detailed explanations
3. **Section Headings**: H2-H6 headings that structure the content
4. **Informational Text**: Benefits, features, and buying guides
5. **Bullet Points**: Key features or benefits in list format

**Example from a Furniture page:**
- "Second-hand design furniture, first-class quality"
- "Furniture previously owned and lightly used by someone else..."
- "Special, second-hand furniture for everyone"
- Benefits of buying second-hand furniture

## 🚨 Important Notes

### Ethical Usage
- The scraper includes respectful rate limiting (2-second delays by default)
- Rotates user agents to appear more natural
- Only scrapes publicly available content
- Does not overload the server

### Troubleshooting

**Common Issues:**

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Network Issues**: Check internet connection and try again
   
3. **Empty Results**: Some pages may not have bottom content - this is normal

4. **Rate Limiting**: If you get blocked, increase the delay in config.py

**Logs**: Check `scraper.log` for detailed information about what happened during scraping.

## 📊 Expected Results

Based on Whoppah's structure, you can expect:
- **80-100+ pages** with bottom content
- **Category descriptions** of 200-1000 characters each
- **SEO content** with multiple sections per page
- **Headings** like "What is vintage lighting?", "Benefits of second-hand furniture"
- **Rich metadata** for SEO analysis

## 🔧 Troubleshooting

**Common Issues:**

**"SSL Error" or "Certificate Error":**
```bash
# SSL issues are handled automatically in the scraper
# If you see errors, the scraper includes SSL workarounds
```

**"No content found" or "0 characters":**
```bash
# Try different categories - some pages have different structures
python scrape_category.py decoration/vases  # Known working page
python scrape_category.py furniture         # Known working page
```

**"Permission denied" or "Access denied":**
```bash
# Check your internet connection and try again
# Whoppah sometimes has rate limiting
```

## 🎯 SEO Analysis Use Cases

**What you can do with the extracted content:**

1. **Content Audit**: Review existing SEO content across all categories
2. **Gap Analysis**: Find categories with thin or missing descriptions  
3. **Content Quality**: Compare content length and structure across pages
4. **Keyword Analysis**: Extract keywords and phrases from descriptions
5. **Content Planning**: Identify opportunities for content improvement

**JSON structure makes it easy to:**
- Import into spreadsheets for analysis
- Process with other tools or scripts  
- Compare content across categories
- Track changes over time

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🐛 **Report bugs** by opening an issue
2. 💡 **Suggest features** for new functionality  
3. 🔧 **Submit PRs** for improvements
4. 📖 **Improve documentation**

## 🆘 Support & Troubleshooting

**Common Issues:**

- **SSL Errors**: The scraper handles SSL automatically
- **No content found**: Try known working categories: `furniture`, `decoration/vases`, `lighting`
- **Import errors**: Make sure you're in the virtual environment with dependencies installed

**Getting Help:**
1. Check the [examples](examples/) directory
2. Review [issues](../../issues) for similar problems
3. Open a new issue with details

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Notice

This tool is for educational and SEO analysis purposes only. Please:
- Respect Whoppah.com's terms of service
- Use responsibly with appropriate rate limiting  
- Don't redistribute scraped content
- Use for analysis and research purposes

---

**⭐ If this tool helped you, please give it a star!**
