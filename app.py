from flask import Flask, render_template, jsonify
from database import getAllJobs
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
    jobsList.append(job)
    print(job)
  return jsonify()
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
