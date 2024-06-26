from flask import Flask, render_template, jsonify
from database import getAllJobs, loadJob
import json

app = Flask(__name__)
print(app)



TITLE = "OSAMA's page"

@app.route('/')
def hello_world():
  return render_template('temp.html', names=getAllJobs(), title=TITLE)

@app.route('/jobs')
def list_jobs():
  jobsList = []
  for job in getAllJobs():
    jobsList.append(list(job))

  return jsonify(jobsList)

@app.route('/jobs/<id>')
def show_job(id):
  job = loadJob(id)
  return jsonify(list(job)) if job != None else jsonify(["None"])



    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
