import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST="0.0.0.0"

@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        "status": 200,
        "message": "Pi Server is Running"
    })

@app.route('/api/snap', methods=['GET'])
def snap_picture():
	"""
	Write code here to snap a picture on the raspberry pi.
	And send it to the main azure server
	"""
	pass


if __name__ == "__main__":
	app.run(host=HOST)
