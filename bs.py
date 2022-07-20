# from turtle import title
import requests
from bs4 import BeautifulSoup

# If u want to scrape a website :
# use the API / HTML web scraping using some tool like bs4


#url = "https://www.tutorialspoint.com/index.htm"
url='https://codewithharry.com'

# S1: Get the HTML

req = requests.get(url)
htmlcontent=req.content
# print(htmlcontent)

# S2: Parse the HTML

soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup)
# print(soup.prettify)

# S3: HTML tree traversal

title=soup.title # Get the title of the HTML page

# print(title)

# # types of object 
# print(type(title)) # 1.Tag

# print(title.string)
# print(type(title.string)) # 2. NavigableString

# print(type(soup)) # 3. BeautifulSoup

# # 4. Comment


# Get all the paragraphs from the page
# paras=soup.find_all('p')
# print(paras)


# Get all the anchor tags from the page
anchors=soup.find_all('a')
print(anchors)










'''
from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
'''
