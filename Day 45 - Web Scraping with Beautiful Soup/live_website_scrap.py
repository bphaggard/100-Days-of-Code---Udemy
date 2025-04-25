from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# Find values from first article
article_text = soup.find('span', class_='titleline').find('a')
#print(article_text.getText())
article_link = article_text.get("href")
#print(article_link)
article_score = soup.find('span', class_='score')
#print(article_score.getText())
# Find values from all articles
articles = soup.find_all('span', class_='titleline')

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
#print(article_scores)
#print(int(article_scores[0].split()[0])) # Convert first point to integer. It removed space and points word

# Show values for highest score
highest_score_index = article_scores.index(max(article_scores))
print(article_texts[highest_score_index])
print(article_links[highest_score_index])