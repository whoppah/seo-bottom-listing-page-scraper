# 🤖 GitHub Actions Workflows

This repository includes several automated workflows to run the Whoppah scraper in the cloud.

## 🔄 Available Workflows

### 1. 🔍 **Scrape Content** (`scrape-content.yml`)
**Purpose**: Automated daily scraping of multiple categories  
**Trigger**: Daily at 8 AM UTC + Manual  
**What it does**:
- Scrapes 6 major categories daily
- Stores results as downloadable artifacts  
- Generates summary report
- Optionally commits results to repository

**Manual Usage**:
1. Go to **Actions** tab in GitHub
2. Select "🔍 Scrape Whoppah Content"  
3. Click "Run workflow"
4. Customize categories (optional)
5. Choose whether to commit results

### 2. 🎯 **Manual Scrape** (`manual-scrape.yml`)
**Purpose**: Quick single-category scraping  
**Trigger**: Manual only  
**What it does**:
- Scrapes one category of your choice
- Shows immediate results in logs
- Uploads content as artifact

**Usage**:
1. Go to **Actions** tab
2. Select "🎯 Manual Scrape"
3. Click "Run workflow"  
4. Choose category from dropdown
5. View results in workflow logs

### 3. 🧪 **Test Scraper** (`test-scraper.yml`)
**Purpose**: Validate setup without scraping  
**Trigger**: On pull requests and pushes  
**What it does**:
- Tests Python environment setup
- Validates dependencies
- Checks configuration files

## 📊 Using the Results

### Download Artifacts
1. Go to completed workflow run
2. Scroll to "Artifacts" section  
3. Download the zip file
4. Extract to get JSON files

### View in Logs
- Results summary appears in workflow logs
- Content statistics shown for each category
- File sizes and character counts displayed

## ⚙️ Configuration

### Scheduled Scraping
Edit `.github/workflows/scrape-content.yml`:
```yaml
schedule:
  - cron: '0 8 * * *'  # Daily at 8 AM UTC
  # - cron: '0 8 * * 1'  # Weekly on Mondays
  # - cron: '0 8 1 * *'  # Monthly on 1st
```

### Default Categories
Modify the categories list in `scrape-content.yml`:
```yaml
categories="furniture,lighting,decoration/vases,style/vintage"
```

### Commit Results to Repo
Enable automatic commits by setting `commit_results: true` when running manually.

## 🚨 Important Notes

### Rate Limiting
- Workflows include 3-second delays between requests
- Respects Whoppah.com's servers
- Uses GitHub's infrastructure (not your machine)

### Usage Limits
- **Public repos**: Unlimited minutes
- **Private repos**: 2,000 minutes/month on free plan
- Each run takes ~2-5 minutes

### Storage
- Artifacts kept for 30 days (configurable)
- Results can be committed to `data/` folder
- Download before expiration

## 🔧 Troubleshooting

### Workflow Failed
- Check logs for specific error messages
- Verify categories exist on Whoppah.com
- May be temporary site issues

### No Results
- Check if scraper found content
- Some categories might have different structures
- Try manual scrape first

### Rate Limited
- Reduce frequency of scheduled runs
- Increase delays between requests
- GitHub Actions may be temporarily blocked

---

**🎯 Perfect for automated content monitoring and SEO analysis!**