
from flask import Flask, flash, render_template, request, redirect
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup




app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    js = ""

    if request.method=="POST":
        url=request.form["url"]
    
    #url='https://en.wikipedia.org/wiki/List_of_stars_on_the_Hollywood_Walk_of_Fame'


        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        table=soup.find_all('table',{'class':'wikitable sortable jquery-tablesorter'})

        rows = soup.find_all("tr")


        columns=[v.text.replace('\n','') for v in rows[0].find_all('th')]
        df=pd.DataFrame(columns=columns)

        for i in range(2,len(rows)):

            tds=rows[i].find_all('td')
    
            if len(tds)==3:
                values=[tds[0].text,tds[1].text,tds[2].text.replace('\n','').replace('\xa0','')]
            #else:

            #values=[td.text.replace('\n','').replace('\xa0','') for td in tds]
            df=df.append(pd.Series(values,index=columns),ignore_index=True)
            js = df.to_json(orient = 'columns')
    
    
    
    
    
    return render_template("index.html",js=js)



if __name__ == "__main__":
    app.run(debug=True,port=4000)
