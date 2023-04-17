from flask import Flask, render_template, request, redirect, url_for, session
import sys
import pandas as pd
import importlib


TEMPLATES_AUTO_RELOAD = True

# Flask Web App
app = Flask(__name__, static_folder='static')


# index page
@app.route("/", methods=[ 'GET', 'POST' ])	# 'GET' and 'POST' are HTML methods that are used in the corresponding html file
def index():
	curruser = session.get('curruser', None)

	if request.method == 'POST':
		# Go to login page
		if request.form.get('log') == 'Login':
			return redirect(url_for('login'))
		# go to sign up page
		elif request.form.get('sign') == 'Sign Up':
			return redirect(url_for('sign_up'))
		# Go straight to home
		elif request.form.get('skip') == 'Home':
			# Throw error if not logged in
			if not curruser:
				error = 'Currently not logged in.'
				return render_template('index.html', error=error)
			else:
				return redirect(url_for('home'))
	return render_template('index.html', error=None)

if __name__ == "__main__":
	port = 5000
	if(len(sys.argv) >= 2):
		port = sys.argv[1]
	#app.secret_key = 'NA.bcr*xB2KJc7W!7mVHeG!xUC9uQo8qAJj7fE7wr2FbHM8A7kdRRaaN7a-zK9*.vxB92o3s.wgLRV76Z6qWvj9gb@Er*2cThNpe'
	app.config['SECRET_KEY'] = 'NA.bcr*xB2KJc7W!7mVHeG!xUC9uQo8qAJj7fE7wr2FbHM8A7kdRRaaN7a-zK9*.vxB92o3s.wgLRV76Z6qWvj9gb@Er*2cThNpe'
	app.run('0.0.0.0', port) # 5000 is the port for the url, change this when test so that multiple devs can run at same time on different ports