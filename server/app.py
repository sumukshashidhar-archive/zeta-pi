import flask
import mainreq as ms
import PiCamera

import jw

app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST="0.0.0.0"
TOKEN = None

name = "raspi"
pw = "raspi"

@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        "status": 200,
        "message": "Pi Server is Running"
    })

@app.route('/api/snap', methods=['POST'])
def snap_picture():
	# check if the token is sent in with the request first
	try:
		token = flask.request.form['token']
	except:
		return flask.jsonify({
            "message":"Auth Required"
        }), 401
	try:
		response = jw.decode(token)
	except:
		return flask.jsonify({
            "message":"JWT Deserialization Failed"
        }), 500


if __name__ == "__main__":
	app.run(host=HOST)
