import flask
import mainreq as ms
import PiCamera


app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST="0.0.0.0"
TOKEN = None

@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        "status": 200,
        "message": "Pi Server is Running"
    })

@app.route('/api/snap', methods=['GET'])
def snap_picture():
	#if TOKEN == None:
	#	TOKEN = ms.getToken()
		url = "http://40.76.37.214:80/api/upload/image"
		data = {}
		global TOKEN
		camera = PiCamera()

		camera.capture('/home/pi/Desktop/capture.jpg')
		
		obj = {
			"token" = TOKEN
		}
		files = {'image':open('/home/pi/Desktop/capture.jpg','rb')}

		r = requests.post(url,data = obj, files = files)

		print(r)



if __name__ == "__main__":
	app.run(host=HOST)
