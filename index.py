from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from datetime import *
from prediction import *
import time


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/api/prediction")
def getPrediction():
	start = request.args['start']
	end = request.args['end']
	company = request.args['company']

	startDate = datetime.datetime.strptime(start, "%m/%d/%Y").date()
	endDate =  datetime.datetime.strptime(end, "%m/%d/%Y").date()

	prediction = CustomPredict(startDate, endDate, company);
	#prediction = 1
	#time.sleep(10);

	print prediction
	return jsonify(prediction=prediction)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
