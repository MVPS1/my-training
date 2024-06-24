from flask import Flask

app = Flask(__name__)
print(app)
print("getfff")


@app.route('/')
def hello_world():
  return 'Hello, HHggHH!'


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
