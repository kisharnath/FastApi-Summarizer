import requests
from bs4 import BeautifulSoup

# Function to scrape text from a given URL
def scrape_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all paragraphs from the webpage
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    words = text.split()[:1000]
    limited_text = " ".join(words)


    return limited_text