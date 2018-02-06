import scraper
from flask import Flask, render_template, json, request
app = Flask(_name_)
@app.route("/")
def main():
	return render_template('froala.html')
    #return "Welcome!"
#@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')
#@app.route('/signUp',methods=['POST','GET'])
@app.route('/', methods=['GET','POST'])
def getURL():
	if request.method == 'GET':
		return render_template('froala.html')
	else:      
		_url = request.form['input-url']
		if _url:
			return json.dumps({'wow!!!': scraper.scrapey(_url)})

		#return render_template('froala.html', _anchor="add", result=_url)

		#return json.dumps ({'yikes': 'oh no'})
		#return json.dumps({'wow!!!': scraper.scrapey(_url) })

		#return json.dumps({'html':'<span>All fields good !!' + _url + '</span>'})
		#return render_template('froala.html', _anchor="add", result=_url)
	if _url:
		return json.dumps({'html':'<span>All fields good !!</span>'})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})

if _name_ == "_main_":
	app.run()