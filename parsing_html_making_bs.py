from bs4 import BeautifulSoup

with open('website.html') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.string)

"""find_all & find are used to get a list or get a particular element based on the html tag name and other attrs of that element"""
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText(), tag.get("href"))
    pass

h3_with_heading_class = soup.find(name="h3", class_="heading")
print(h3_with_heading_class.getText())

"""select and select_one help select a list of element or a particular element based on a selector which is literally just how we target html elements in css"""
company_url = soup.select_one(selector="p a")
print(company_url.getText(), company_url.get("href"))