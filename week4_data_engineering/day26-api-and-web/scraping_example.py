import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://news.ycombinator.com/"

# Get the content
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract article titles
    titles = soup.find_all("a", class_="titlelink")
    
    for i, title in enumerate(titles[:5], 1):  # Print first 5 titles
        print(f"{i}. {title.text}")
else:
    print("Failed to retrieve webpage")