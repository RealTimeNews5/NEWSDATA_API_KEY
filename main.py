import requests
import os

# Get your API key from environment variables (set in GitHub Secrets)
API_KEY = os.getenv("NEWSDATA_API_KEY")

def fetch_news():
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&language=en"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Description: {article.get('description', 'N/A')}")
            print(f"Link: {article.get('link', 'N/A')}")
            print("---")
            # Here you would add your Stage 2 logic: Send to Gemini for classification
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    fetch_news()