import os

from flask import Flask, request, render_template, send_from_directory

__author__ = "ibininja"

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')

def index():
	return render_template('index.html')




@app.route('/upload', method={"POST"})
def upload():
	target = os.path.join(APP_ROOT,'images/')
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)
	else:
		print("Couldnt create upload directory {}" .format(target))

	print(request.files.getlist(file))

	for upload in request.files.getlist(file):
		print("{} is the filename".format(upload.filename))
		filename = upload.filename
		destination="/".join(target,filename)
		print("Accept incoming file: ",filename)
		print("Saving to: ",destination)
		upload.save(destination)

		return render_template("complete.html", treat_name=filename)

@app.route('/upload/<filename')
def send_treat(filename):
	return send_from_directory("treats",filename)

@app.route('/treats')
def treats():
	treat_names = os.listdir('/treats')
	return render_template("treats.html", treat_names=treat_names)

if __name__ ="__main__":
	app.run(port:4555 debug=True)