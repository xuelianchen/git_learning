# _*_encoding:utf-8_*_
from flask import Flask
import requests

url  = "http://www.baidu.com"
res = requests.get(url)
content = res.text
app = Flask(__name__)
@app.route('/baidu')
def index():
    # return 'Hello World'
    return content

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()