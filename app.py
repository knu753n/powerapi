from flask import Flask
from price import Pris

pris = Pris()

app = Flask(__name__)
@app.route('/')
def index():
	return f"strompris api, /naa /idag /imorgen \n\nPris naa: {pris.naa()} | gjennomsnitt  {pris.maned()}"

@app.route('/naa')
def current():
	return pris.naa()

@app.route('/idag')
def idag():
	return pris.idag()

@app.route('/imorgen')
def imorgen():
	return pris.imorgen()

if __name__ == '__main__':
	app.run(host='10.0.0.158', port='80', debug=True)
