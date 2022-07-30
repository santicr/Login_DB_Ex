from readline import insert_text
from flask import Flask, request, g, redirect, url_for, render_template, session
import uuid
import controller

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/error')
def error():
	return render_template('error.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/register_process', methods = ['POST'])
def register_process():
	user = request.form['username']
	pass1 = request.form['password1']
	pass2 = request.form['password2']
	if pass1 == pass2 and controller.verifyReg(user):
		controller.insertRow(user, pass1)
		return redirect('/')
	return redirect('/error')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login_process', methods = ['POST'])
def login_process():
	user = request.form['username']
	passw = request.form['password']
	if controller.verifyLog(user, passw):
		return redirect('/')
	return redirect('/error')

if __name__ == "__main__":
	app.run(debug = True, port = 5000)