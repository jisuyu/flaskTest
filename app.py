from flask import Flask,render_template,request
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup    

app=Flask(__name__)

#print(datetime.today())

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/hello/<string:name>")
def hellojs(name):
    return render_template("hello.html",n=name)
    
#/cube/숫자
@app.route("/cube/<int:number>")
def cube(number):
    return render_template("cube.html",n=number*number)
    
@app.route("/lunch")
def lunch():
    lunch_box=['20층','양자강','바스버거','김까','시골집']
    lunch=random.choice(lunch_box)
    return render_template("lunch.html",lunch=lunch,box=lunch_box)
    
@app.route("/vonvon/<string:name>")
def vonvon(name):
    hour_arr=range(1,1001)
    minuate_arr=range(-1,60)
    hour=random.choice(hour_arr)
    minuate=random.choice(minuate_arr)
    return render_template("vonvon.html",hour=hour,minuate=minuate,name=name)

@app.route("/christmas")
def christmas():
    christmas=""
    if datetime.today().month==12 & datetime.today().day==25:
        christmas="맞아"
    else:
        christmas="아니야"
    return render_template("christmas.html",christmas=christmas)
@app.route('/google')
def google():
    return render_template("google.html")
    
@app.route('/opgg')
def opgg():
    return render_template("opgg.html")

@app.route('/opggresult')
def opggresult():
    name=request.args.get('q')
    res=requests.get("http://www.op.gg/summoner/userName="+name)
    soup = BeautifulSoup(res.content, 'html.parser') 
    wins=soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    losses=soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    
    return render_template("opggresult.html",name=name,wins=wins[0].text,losses=losses[0].text)
    
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8080)
