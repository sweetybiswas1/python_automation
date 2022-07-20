# import requests
import bs4


from bs4 import BeautifulSoup

# url = 'https://www.connectbud.com'
# myobj = {'somekey': 'somevalue'}

# x = requests.post(url, json = myobj)

# print(x.text)

html = '''
<body>
    <ul>
        <li>This</li>
        <li><a>This</a>This</li>
        <li>This</li>
        <li>This</li>
        <li id="li">This</li>
        <li>    This    </li>
    </ul>
</body>
'''
soup = BeautifulSoup(html, 'html.parser')