from flask import Flask, request, jsonify
import variables as variables
import paho.mqtt.client as mqtt

app = Flask(__name__)
# app.config['MQTT_BROKER_URL'] = 'stingray-app-97v6u.ondigitalocean.app'
# app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_KEEPALIVE'] = 60  # sekundy
# app.config['MQTT_TLS_ENABLED'] = False  # czy używać TLS

# mqtt_client = mqtt.Client()
# mqtt_client.connect('104.248.252.28', 1883)

def initialize_mqtt():
    mqtt_client = mqtt.Client()
    try:
        mqtt_client.connect('104.248.252.28', 1883)
        # Dodatkowa konfiguracja klienta MQTT
        # ...
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
        
        body = {'robotState': variables.robotState, 'moveDirection': variables.moveDirection}
        
        mqtt_client.publish('robot/walking', body)
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during walking', 'details': str(e)}), 400
    
@app.route('/turning', methods=['POST'])
def turning():
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
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during turning', 'details': str(e)}), 400
    
@app.route('/translation', methods=['POST'])
def translation():
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
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during translation', 'details': str(e)}), 400
    
@app.route('/rotate', methods=['POST'])
def rotate():
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
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during rotation', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)