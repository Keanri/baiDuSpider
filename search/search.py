from flask import Flask
from flask import render_template
from flask import request
from baiduspider import getBaiduMsg

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/s")
def search():
    keyword = request.args.get('wd')
    page = request.args.get("pn")
    text = getBaiduMsg(keyword,page)
    return text

if __name__ == '__main__':
    app.run(debug=True,port=8000)

