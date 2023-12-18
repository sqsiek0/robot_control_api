from flask import Flask, request, jsonify
import json
import variables as variables
import paho.mqtt.client as mqtt

app = Flask(__name__)
mqtt_client = mqtt.Client()

def initialize_mqtt():
    global mqtt_client
    
    # mqtt_client = mqtt.Client()
    try:
        mqtt_client.connect('134.122.84.130', 1883)
        mqtt_client.loop_start()
        mqtt_client.keepalive = 60
        mqtt_client.reconnect_delay_set(min_delay=1, max_delay=120)

    except Exception as e:
        app.logger.error(f"Failed to connect to MQTT: {e}")
        

@app.route('/working', methods=['GET'])
def working():
    try:    
        variables.isRobotWork = not variables.isRobotWork
        return jsonify({'isWorking': variables.isRobotWork}), 200
    except Exception as e:
        return jsonify({'error': 'Error during checking robot status', 'details': str(e)}), 400
    
@app.route('/walking', methods=['POST'])
def walking():
    global mqtt_client
    
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No body provided'}), 400
        
        walk = data.get('walkState')
        
        if walk == 'front':
            variables.robotState = '4'
            variables.moveDirection = '1'
        elif walk == 'back':
            variables.robotState = '4'
            variables.moveDirection = '2'
        elif walk == 'stop':
            variables.robotState = '1'
            variables.moveDirection = '1'
        else:
            return jsonify({'error': 'Invalid walk state'}), 400
        
        body = json.dumps({'robotState': variables.robotState, 'moveDirection': variables.moveDirection})
        
        mqtt_client.publish('robot/walking', body)
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during walking', 'details': str(e)}), 400
    
@app.route('/turning', methods=['POST'])
def turning():
    global mqtt_client
    
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No body provided'}), 400
        
        turn = data.get('turn')
        
        if turn == 'left':
            variables.robotState = '5'
        elif turn == 'right':
            variables.robotState = '6'
        else:
            return jsonify({'error': 'Invalid turn direction'}), 400
        
        body = json.dumps({'robotState': variables.robotState})
        
        mqtt_client.publish('robot/turning', body)
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during turning', 'details': str(e)}), 400
    
@app.route('/translation', methods=['POST'])
def translation():
    global mqtt_client
    
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No body provided'}), 400
        
        axis = data.get('axis')
        value = data.get('value')
        
        if axis == 'x':
           if value == 'plus': variables.translationState = 'w'
           elif value == 'minus': variables.translationState = 's'
           else:
               return jsonify({'error': 'Invalid value'}), 400
           
        elif axis == 'y':
            if value == 'plus': variables.translationState = 'd'
            elif value == 'minus': variables.translationState = 'a'
            else:
               return jsonify({'error': 'Invalid value'}), 400
           
        elif axis == 'z':
            if value == 'plus': variables.translationState = 'q'
            elif value == 'minus': variables.translationState = 'e'
            else:
               return jsonify({'error': 'Invalid value'}), 400

        else:
            return jsonify({'error': 'Invalid translation axis value'}), 400
        
        variables.robotState = '7'
        
        body = json.dumps({'translationState': variables.translationState, 'robotState': variables.robotState})
        
        mqtt_client.publish('robot/translation', body)
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during translation', 'details': str(e)}), 400
    
@app.route('/rotate', methods=['POST'])
def rotate():
    global mqtt_client
    
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No body provided'}), 400
        
        axis = data.get('axis')
        value = data.get('value')
        
        if axis == 'x':
            if value == 'plus': variables.rotationState = 'u'
            elif value == 'minus': variables.rotationState = 'i'
            else:
               return jsonify({'error': 'Invalid value'}), 400
            
        elif axis == 'y':
            if value == 'plus': variables.rotationState = 'j'
            elif value == 'minus': variables.rotationState = 'k'
            else:
               return jsonify({'error': 'Invalid value'}), 400

        elif axis == 'z':
            if value == 'plus': variables.rotationState = 'm'
            elif value == 'minus': variables.rotationState = ','
            else:
               return jsonify({'error': 'Invalid value'}), 400   
        else:
            return jsonify({'error': 'Invalid rotate axis value'}), 400
        
        variables.robotState = '7'
        
        body = json.dumps({'rotationState': variables.rotationState, 'robotState': variables.robotState})
        
        mqtt_client.publish('robot/rotate', body)
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during rotation', 'details': str(e)}), 400

if __name__ == '__main__':
    initialize_mqtt()
    app.run(host='0.0.0.0', port=8080)