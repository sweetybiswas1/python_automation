import requests

r = requests.get("https://www.w3schools.com/python/demopage.php")

#print(r) #return response

#print(dir(r)) #return attributes and methods that we can access from the response

#print(help(r)) #detail explaination

#print(r.text)      

# how to download image
# r = requests.get("https://www.google.com/search?q=image&tbm=isch&source=iu&ictx=1&vet=1&fir=JoR7JNzGko0S6M%252C0JWe7yDOKrVFAM%252C_%253Bsp12V8x9gw6KuM%252C4O2GvGuD-Cf09M%252C_%253BDH7p1w2o_fIU8M%252CBa_eiczVaD9-zM%252C_%253Bn5hAWsQ-sgKo_M%252C-UStXW0dQEx4SM%252C_%253B-VCM1w56w6u5VM%252CaVwfeogQqK1XmM%252C_%253Bz4_uU0QB2pe-SM%252C7SySw5zvOgPYAM%252C_%253B2nDXavJs9DoKTM%252CB51x0PBR9KNzvM%252C_%253BMOAYgJU89sFKnM%252CygIoihldBPn-LM%252C_%253B2DNOEjVi-CBaYM%252CAOz9-XMe1ixZJM%252C_%253BkwgHAQqTiLQXLM%252CR0KnAtfyBDsyiM%252C_%253B0sOgRvZZyWRMuM%252CZaycYywhXLmIVM%252C_%253BBx81dUgHmqLhzM%252CNMmM-IXyCkU2hM%252C_%253B0vb1Fq79Feed-M%252CRFPJWHwalThlKM%252C_&usg=AI4_-kQH16PzWCMi_nyccUE3Ho45wC6-dw&sa=X&ved=2ahUKEwjh27yS-Oj4AhU_TmwGHSVVAp4Q9QF6BAgMEAE#imgrc=DH7p1w2o_fIU8M")

# with open("nat.img.jpg","wb") as f:
#     f.write(r.content)

# print(r.status_code) #return http status code

# print(r.ok) #return false if there is any kind of server error







