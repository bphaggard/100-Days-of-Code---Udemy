from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.prettify())

all_paragraphs = soup.find_all(name="a")
#print(all_paragraphs)

for tag in all_paragraphs:
    #print(tag.getText()) # show only text
    #print(tag.get("href")) # show only links
    pass

# heading = soup.find(name="h1", id="name") # find exact tag which we want
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a") # find for id -> #name, class -> .heading
print(company_url)