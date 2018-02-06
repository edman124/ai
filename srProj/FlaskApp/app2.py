from flask import Flask, render_template, request, json
import lxml.html as lh
from urllib.request import urlopen
import requests
import sys
app = Flask(__name__)
url="error"
@app.route("/")
def main():
	return render_template('index.html')
def parsePage(url):
	page = requests.get(url)
	tree = lh.fromstring(page.content)	
	# intro = tree.xpath("//*[@id=\"mw-content-text\"]/div/p/text()")
	intro = tree.xpath("//*[@id=\"mw-content-text\"]/div//p")
	ret=[]
	ret.append("intro")
	ret.append("-------------------")
	for i in range(len(intro)):
		x=intro[i].xpath("string()")
		if len(x)>4:
			ret.append(x)
		ret.append("----")
		if intro[i].xpath("string()")=="":
			ret.append("intro end ---------------")
			ret.append("body")
			ret.append("----------------")
	ret.append("body end -------------------")
	# toc = tree.xpath("//*[@id=\"toc\"]/ul/li//a/@href")
	# ret.append("contents")
	# ret.append("-------------------")
	# ret.append(toc)
	return "\n".join(ret)
@app.route('/', methods=['POST'])
def parse():
	if request.method == 'POST':
		url = request.form['input-url']
		if url:
			parsed =  parsePage(url)
			parsed = parsed.replace("^^", "\n")
			return render_template('index.html', output=parsed)
			return parsePage(url)
	return render_template('index.html')
	# if request.method=='POST':
	# 	_url = request.form.get['input-url']
	# 	if _url:
	# 		return _url
     
	# 	return("hi")
	# 	print("in else", file=sys.stderr)
		# _url = request.form['input-url']
		# if _url:
		# 	print(parsePage("https://en.wikipedia.org/wiki/Machine"),file=sys.stderr)
		# 	return json.dumps({'wow!!!': parsePage(_url)})

		#return render_template('froala.html', _anchor="add", result=_url)

		#return json.dumps ({'yikes': 'oh no'})
		#return json.dumps({'wow!!!': scraper.scrapey(_url) })

		#return json.dumps({'html':'<span>All fields good !!' + _url + '</span>'})
		#return render_template('froala.html', _anchor="add", result=_url)
	# if _url:
	# 	return json.dumps({'html':'<span>All fields good !!</span>'})
	# else:
	# 	return json.dumps({'html':'<span>Enter the required fields</span>'})
if __name__ == "__main__":
	print(url)
	app.run()



# '<!DOCTYPE html><html lang="en"><head><title>Python Flask Bucket List App</title><link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">    <!-- <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet"> --></head><body>    <div class="container">        <div class="header"><h3 class="text-muted">Wikipedia Parser</h3></div>        <div class="jumbotron" style="border-radius:25px;">   <form method = "POST" name = "form2" id = "form2">                <input id = "input-url" name ="input-url" type="text" class="form-control" autofocus autocomplete="off">                <!-- <input oninput="check()" type="text" name="answers" id="answers" disabled autocomplete="off" autofocus> -->            </form>        </div>        <div class="row marketing">            <div class="col-lg-6">            </div>       <div class="col-lg-6">            </div>        </div>     </div></body> </html>' + 
