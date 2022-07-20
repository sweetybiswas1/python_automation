
from bs4 import BeautifulSoup
import requests
url = "https://www.geeksforgeeks.org/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title) #extract title from the website

# for link in soup.find_all('a'):
#     print(link.get('href'))

# title of the page
# print(soup.title)

# get attributes:
# print(soup.title.name)

# get values:
# print(soup.title.string)

# beginning navigation:
# print(soup.title.parent.name)

# getting specific values:
# print(soup.p)

# print(soup.find_all('p')) #paragraph tag

# for paragraph in soup.find_all('p'):
#    print(paragraph.string)
#    print(str(paragraph.text))
# print(soup.get_text())

# print(soup.prettify()) #as req.text

# z = soup.find_all("p")[0]

# print(z.find_all("<b"))

# print(soup.find('p')) 1st paragraph

links = soup.find_all('a')
all_links = set()

for link in links:
   if(link!='#'):
      link =  (link.get('href'))
      all_links.add(link)
print(f"{all_links}/n")

ul = soup.find("ul")
print(ul.contents)



ul = soup.find("ul")
for i in ul.children:
	print(i)


ul = soup.find("ul")
print(ul.parent)

print(ul.parent.parent) #parent of parent


ul = soup.find(id="li")
print(ul.next_sibling.next_sibling)


for i in ul.previous_siblings:
   print(i)


print(ul.previous_sibling.previous_sibling)