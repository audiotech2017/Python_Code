#启动一个小的http服务 返回hello world


from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World! xx"

app.run(debug=True)