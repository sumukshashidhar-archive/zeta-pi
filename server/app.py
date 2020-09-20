import flask
import mainreq as ms
from picamera import PiCamera
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

@app.route('/api/snap', methods=['GET'])
def snap_picture():
	i = 0
	global TOKEN
	if TOKEN == None:
		TOKEN = ms.getToken(name,pw)

	if jw.validate_token(TOKEN):
		camera = PiCamera()
		camera.capture('/home/pi/Desktop/capture'+ str(i) +'.jpg')
		print("Token Valid")
		r = requests.post(
			url ="http://40.76.37.214:80/api/upload/image",
			data = {
			"token" :TOKEN
			}, 
			files = {'image':open('/home/pi/Desktop/capture' + str(i) + '.jpg','rb')}
		)

		print(r)
	else:
		print("Invalid token")	



if __name__ == "__main__":
	app.run(host=HOST)
