from flask import Flask, request, jsonify
import variables

app = Flask(__name__)

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
           if value == 'minus': variables.translationState = 's'
        elif axis == 'y':
            if value == 'plus': variables.translationState = 'd'
            if value == 'minus': variables.translationState = 'a'
        elif axis == 'z':
            if value == 'plus': variables.translationState = 'q'
            if value == 'minus': variables.translationState = 'e'
        else:
            return jsonify({'error': 'Invalid rotate value'}), 400
        
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
            if value == 'minus': variables.rotationState = 'i'
            
        elif axis == 'y':
            if value == 'plus': variables.rotationState = 'j'
            if value == 'minus': variables.rotationState = 'k'

        elif axis == 'z':
            if value == 'plus': variables.rotationState = 'm'
            if value == 'minus': variables.rotationState = ','
        else:
            return jsonify({'error': 'Invalid rotate value'}), 400
        
        return jsonify({'message': 'Correct'}), 200
    except Exception as e:
        return jsonify({'error': 'Error during rotation', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)