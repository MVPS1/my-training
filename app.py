from flask import Flask, url_for, render_template, jsonify, request
from database import getAllJobs, loadJob, addJob
import json
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

serial = URLSafeTimedSerializer('SecretKey!') #This supposed to be secret


app = Flask(__name__)
print(app)

mail = Mail(app)

TITLE = "OSAMA's Page"

@app.route('/')
def hello_world():
  return render_template('temp.html', names=getAllJobs(), title=TITLE)

@app.route('/login', methods=['get','post'])
def login():
  return render_template('login.html')

@app.route('/submit', methods=['get', 'post'])
def submit():
  email = request.form['email']
  token = serial.dumps(email, salt='email-confirm') #salt is not necessary

  link = url_for('confirm_email', token=token, _external=True)
  return "<h1>Your email is {} <a href='{}'>Click to Confirm</a></h1>".format(email, link)

@app.route('/email_confirm/<token>')
def confirm_email(token):
  try:
    email = serial.loads(token, salt='email-confirm', max_age=120)
  except SignatureExpired:
    return "<h1 style='color: red'>The session is expired !</h1>"
    
  return "<h1 style='color: green'>The email is confirmed !</h1>"

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

@app.route('/addNew', methods=['post'])
def add_job():

  job = request.form
  #job = request.args # for get method
 
  addJob(job['ID'],job['job'],job['location'],job['salary'])

  return jsonify(job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
