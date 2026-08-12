# Sports & Music Web Scraper

A Python web scraping project that collects popular song and artist data in relation to sports culture. Built with BeautifulSoup and Requests.

---

## Author
Alex Jimenez

---

## What It Does

- Scrapes the top 60 songs and artist names from Pitchfork's *Best Songs of the 1990s* list
- Saves the results to a local `data.txt` file
- Demonstrates basic web scraping of music industry and sports hype song sources

---

## Data Collected

- **60 songs** with artist names from Pitchfork
- Data is relevant to displaying popular songs in relation to sports culture

---

## Technologies Used

- Python 3
- `requests` — HTTP requests to fetch web pages
- `beautifulsoup4` — HTML parsing
- `lxml` — HTML parser backend

---

## Installation

```bash
pip install requests beautifulsoup4 lxml
```

---

## How to Run

```bash
python scraper.py
```

Output will print to the console and be saved to `data.txt` in the same directory.

---

## Sample Output

```
Song: Nirvana — Smells Like Teen Spirit
Song: TLC — Waterfalls
Song: Aaliyah — Are You That Somebody
...
```
