import requests
#r=requests.get('https://www.flipkart.com/?s_kwcid=AL!739!3!582822043916!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_exe_buyers_goog&gclid=CjwKCAjw_b6WBhAQEiwAp4HyIBR2C0B_Ob6NOi_sO-qIJX21SkQtmFwFB5n0cSlyWL8_g8JEbPtOUhoCvLEQAvD_BwE')
#print(dir(r)) #show us the attribute and methods that we can access within this response object

#print(help(r))

#print(r.text)

# print(r.content)

# print(r.status_code)

# print(r.headers)


# payload={'page': 2,'count':25}
# r=requests.get('https://httpbin.org/get',params=payload)
# # print(r.text)
# print(r.url)


# payload={'username': 'sweety','password':'testing'}
# r=requests.post('https://httpbin.org/post',data=payload)
# # print(r.text)
# # print(r.text)
# # print(r.json())

# r_dict=r.json()
# print(r_dict['form'])

## Get

# payload={'key1':'value1'}

# r=requests.get('https://httpbin.org/get',params=payload)

# print(r.text)

##post


# payload={'key1':'value1'}

# r=requests.post('https://httpbin.org/post',data=payload)

# print(r.text)



# r=requests.get('https://httpbin.org/get')

# print(r.text)
# print(r.cookies)
# print(r.headers)
# print(r.json)


# cookies=dict(key1='values1')
# r=requests.get('https://httpbin.org/cookies',cookies=cookies)
# print(r.text)




# r=requests.get('https://httpbin.org/headers')
# print(r.headers)

# s=requests.session()
# s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# r=s.get('https://httpbin.org/cookies')
# print(r.text)


import requests

#the required first parameter of the 'delete' method is the 'url':
x = requests.delete('https://w3schools.com/python/demopage.php')

#print the response text (the content of the requested file):
print(x.text)
