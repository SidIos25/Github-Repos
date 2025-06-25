# Github-Repos

This Python script scrapes the top 5 trending repositories from [GitHub Trending](https://github.com/trending) and saves them into a CSV file. It’s a great beginner-friendly project for learning web scraping, file handling, and working with real-time data.


## Features

- Extracts **top 5 trending repositories** on GitHub
- Gets the **repository name** and direct **link**
- Saves the results to a `top_trending.csv` file
- Clean and human-friendly code using `requests` and `BeautifulSoup`

---

## How to Run

### 1. Clone or Download the Repo

```bash
git clone https://github.com/your-username/github-trending-scraper.git
cd github-trending-scraper

### 2. Install Required Python Libraries
pip install requests beautifulsoup4


### 3.Run the Script
python github_trending.py


### 4. View the Output
A file named top_trending.csv will be created in the same folder. You can open it using Excel, Google Sheets, or any text editor.
