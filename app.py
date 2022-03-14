from flask import Flask, render_template, abort
import re
import random
import img
from wsgiref.simple_server import make_server

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    bg = img.get_img()
    return render_template('404.html', bg=bg), 404


@app.route('/nolink')
def no_page():
    bg = img.get_img()
    return render_template('nolink.html', bg=bg)


@app.route('/')
def story():
    bg = img.get_img()
    text = open("story", "r", errors='ignore', encoding='utf-8')
    story_ = text.read()
    findSum = re.compile('!story(.*?)story!', re.S)
    sum_ = re.findall(findSum, story_)
    findInfo = re.compile(r'【(.*?)】', re.S)
    number = random.randint(0, len(sum_) - 1)
    info = random.choice(sum_)
    info = re.findall(findInfo, info)
    info[4] = info[4].replace("\n", "<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

    return render_template("index.html", info=info, bg=bg)
    abort(404)


@app.route('/about')
def about():
    bg = img.get_img()
    text = open("story_", "r", errors='ignore', encoding='utf-8')
    story_ = text.read()
    findSum = re.compile('!story(.*?)story!', re.S)
    sum_ = re.findall(findSum, story_)
    length = len(sum_)
    return render_template("about.html", length=length, bg=bg)


if __name__ == '__main__':
    server = make_server('127.0.0.1', 5002, app)
    server.serve_forever()
    app.run(debuu=True)
