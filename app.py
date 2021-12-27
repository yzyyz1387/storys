from flask import Flask, render_template, abort
import re
from random import *
import time
import img
from wsgiref.simple_server import make_server


app = Flask(__name__)
bg=img.get_img()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',bg=bg), 404

@app.route('/nolink')
def no_page():
    return render_template('nolink.html', bg=bg)

@app.route('/')
def story():
    text = open("story", "r", errors='ignore', encoding='utf-8')
    sotry = text.read()
    findSum = re.compile('!story(.*?)story!', re.S)
    sum = re.findall(findSum, sotry)
    # 故事总数
    findInfo = re.compile(r'【(.*?)】', re.S)
    # print(findInfo)
    # print(len(sum))
    number = randint(0, len(sum) - 1)
    # print(number)
    info = choice(sum)
    info = re.findall(findInfo, info)
    info[4] = info[4].replace("\n", "<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
    
    return render_template("index.html", info=info,bg=bg)
    abort(404)

@app.route('/about')
def about():
    text = open("story", "r", errors='ignore', encoding='utf-8')
    sotry = text.read()
    # print(sotry)
    findSum = re.compile('!story(.*?)story!', re.S)
    sum = re.findall(findSum, sotry)
    length=len(sum)
    return render_template("about.html", length=length,bg=bg)



if __name__ == '__main__':
    server = make_server('127.0.0.1', 5002, app)
    server.serve_forever()
    app.run(debuu=True)
