from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  ## the host key for '0.0.0.0' means the host is local