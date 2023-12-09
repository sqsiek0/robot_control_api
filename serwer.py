import RPi.GPIO as GPIO
from flask import Flask, request
from pyngrok import ngrok
import os

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@app.route('/control', methods=['POST'])
def control():
    data = request.get_json()
    if data is None:
        return "Invalid JSON data", 400

    pin_state = data['pin_state']

    if pin_state == 'on':
        GPIO.output(18, GPIO.HIGH)
    elif pin_state == 'off':
        GPIO.output(18, GPIO.LOW)

    return {'success': True}

@app.route('/walking', methods = ['POST'])
def walking():
    data = request.get_json()
    # if data is 

# if __name__ == '__main__':
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    # app.run(host='0.0.0.0', port=5000)
    # ngrok_tunnel = ngrok.connect(5000)
    # print('Ngrok URL:', ngrok_tunnel.public_url)