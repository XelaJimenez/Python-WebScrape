# Alex Jimenez,The data values I'm collecting are 60 songs with artist names.
#These values are important to display popular songs in relation to sports.
import requests
from bs4 import BeautifulSoup

url = 'https://pitchfork.com/features/lists-and-guides/the-best-songs-of-the-1990s/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    all_h2_tags = soup.find_all('h2')

    with open('data.txt', 'w') as file:
        for i in range(60):
            songInformation = all_h2_tags[i].text.strip()
            file.write(f"Song: {songInformation}\n")
            print(f"Song: {songInformation}")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

