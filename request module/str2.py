import requests

data = {
    "A" : 100,
    "B" : 200
}

url = 'https://www.connectbud.com'
# r = requests.get(url)
# print(r.text)

# print(dir(r)) #accesable methods and attributes from the response
# print(help(r)) #detail explaination

# print(r.status_code,r.ok)
# r = requests.get(url,params=data) #Optional. A dictionary, list of tuples or bytes to send as a query string
# print(r.text)

# allow redirects
# url1 = 'http://www.connectbud.com'

# r1 = requests.get(url1,allow_redirects=False)
# print(r1.text)

# 'headers' parameter to set the HTTP headers:
# x = requests.get(url, headers = {"HTTP_HOST": "OwnHost"})

# print(x.text)


#allow the response to be streamed by setting the 'stream' parameter to True: default false
# x = requests.get(url, stream=True)

# print(x.status_code)

#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
# x = requests.get(url, timeout=0.001)

# print(x.text)
























