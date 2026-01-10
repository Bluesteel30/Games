from flask import Flask, render_template, request, make_response, redirect
import requests

app = Flask(__name__)
@app.route('/', methods = ['GET','POST'])

def blackjack():
	return render_template('bjw.html')


if __name__ == '__main__':

    app.run(debug=True, use_reloader=False)
