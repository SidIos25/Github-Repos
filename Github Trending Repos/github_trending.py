import requests
from bs4 import BeautifulSoup
import csv

url = "https://github.com/trending"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

repo_list = soup.find_all('article', class_='Box-row')[:5]

with open('top_trending.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Repository Name', 'Link'])

    for repo in repo_list:

        h2_tag = repo.find('h2')
        if h2_tag:
            repo_name = h2_tag.text.strip().replace('\n', '').replace(' ', '')
            repo_link = "https://github.com" + h2_tag.a['href']
            writer.writerow([repo_name, repo_link])
        else:
            print("Could not find repo name in one of the articles.")

print("Top 5 trending repositories saved to top_trending.csv")
