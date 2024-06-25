from flask import Flask, render_template, jsonify

app = Flask(__name__)
print(app)
print("getfff")

JOBS = ["name", "game", "shame", "tame", "fame", "THE LAST", "the last"]
TITLE = "OSAMA's page"
@app.route('/')
def hello_world():
  return render_template('temp.html', names=JOBS, title=TITLE)

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
