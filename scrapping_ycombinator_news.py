from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
article_text_list, article_link_list = [], []
articles = soup.select(selector=".titleline > a:nth-of-type(1)")
for tag in articles:
    article_text_list.append(tag.getText())
    article_link_list.append(tag.get("href"))

article_up_score = [
    int(score.getText().split()[0]) for score in soup.select(selector=".score")
]

highest_score = max(article_up_score)
highest_score_idx = article_up_score.index(highest_score)

highest_score_article = article_text_list[highest_score_idx]
highest_score_article_link = article_link_list[highest_score_idx]

print(highest_score_article)
print(highest_score_article_link)
print(highest_score)
