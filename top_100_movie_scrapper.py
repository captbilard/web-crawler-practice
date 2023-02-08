from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movie_list_tag = soup.select(selector=".jsx-4245974604")
movie_list_tag.reverse()

file = open("top_100_movies.txt", "w")

for tag in movie_list_tag:
    file.write(tag.getText())

file.close()
