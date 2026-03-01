# Automated News Fetcher with GitHub Actions

This repository automatically fetches news articles every 4 hours using **GitHub Actions** as a free scheduler.

## How It Works

1. **GitHub Actions Scheduler**: Runs your Python script every 4 hours (00:00, 04:00, 08:00, 12:00, etc. UTC)
2. **NewsData.io API**: Fetches the latest news articles in English
3. **Automatic Execution**: No server needed, no costs, runs 24/7

## Setup Instructions

### Step 1: Get Your NewsData.io API Key

1. Go to https://newsdata.io/
2. Sign up for a free account
3. Get your API key from the dashboard
4. Copy your API key

### Step 2: Add API Key to GitHub Secrets

1. Go to your repository on GitHub: https://github.com/RealTimeNews5/NEWSDATA_API_KEY
2. Click **Settings** (top right)
3. Click **Secrets and variables** > **Actions** (left sidebar)
4. Click **New repository secret**
5. **Name**: `NEWSDATA_API_KEY`
6. **Value**: Paste your NewsData.io API key
7. Click **Add secret**

### Step 3: Trigger the Workflow

The workflow will automatically run every 4 hours. To test it immediately:

1. Go to your repository
2. Click **Actions** (top navigation)
3. Click **4-Hour News Fetcher** (left sidebar)
4. Click **Run workflow** > **Run workflow**

You should see the workflow execute and fetch news articles!

## Files Explained

- **main.py**: The Python script that fetches news from NewsData.io
- **requirements.txt**: Python dependencies (requests library)
- **.github/workflows/news_bot.yml**: The GitHub Actions workflow that schedules the script to run every 4 hours
- **README.md**: This file

## Next Steps

To add **Gemini AI** integration for classifying news articles by industry, update the `main.py` script to send articles to Google's Gemini API.

## Costs

✅ **Completely Free** - GitHub Actions provides free runner minutes for public repositories!

## Support

For issues with the NewsData.io API, visit: https://newsdata.io/docs/
For GitHub Actions documentation, visit: https://docs.github.com/en/actions