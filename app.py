from flask import Flask, request, g, redirect, url_for, render_template, session
import uuid
import controller

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/register_process', methods = ['GET', 'POST'])
def register_process():
	user = request.form['username']
	pass1 = request.form['password1']
	pass2 = request.form['password2']
	if pass1 == pass2 and controller.verifyRow(user):
		return redirect(url_for('index'))

app.run(debug = True, port = 5000)