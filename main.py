from bs4 import BeautifulSoup
import lxml
import requests

# URL to scrape
url = 'https://roblox.com'
url = 'https://www.musicindustryhowto.com/football-hype-songs/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the page
    title = soup.title.string
    print(f'Page Title: {title}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
