from flask import Flask, request, jsonify
import variables

app = Flask(__name__)

@app.route('/working', methods = ['GET'])
def working():
    try:    
        if variables.isRobotWork:
            variables.isRobotWork = False
            return jsonify({'isWorking': variables.isRobotWork}), 200
        else:
            variables.isRobotWork = True;
            return jsonify({'isWorking': variables.isRobotWork}), 200
    except:
        return jsonify({'Error during checking robot', 400})
    
@app.route('/walking', methods = ['POST'])
def walking():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'No body provided', 400})
        
        walk = data['walkState']
        
        if walk == 'front':
            variables.robotState = '4'
            variables.moveDirection = '1'
            return 200
        elif walk == 'back':
            variables.robotState = '4'
            variables.moveDirection = '2'
            return 200
        elif walk == 'stop':
            variables.robotState = '1'
            variables.moveDirection = '1'
            return 200
    except:
        return jsonify({'Error during walking', 400})
    
@app.route('/turning', methods = ['POST'])
def turning():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'No body provided', 400})
        
        turn = data['turn']
        
        if turn == 'left':
            variables.robotState = '5'
            return 200
        elif turn == 'right':
            variables.robotState = '6'
            return 200
    except:
        return jsonify({'Error during turning', 400})
    
@app.route('/translation', methods = ['post'])
def translation():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'No body provided', 400})
        
        axis = data['axis']
        value = data['value']
        
        if axis == 'x':
            if value == 'plus': variables.translationState = 'w'
            if value == 'minus': variables.translationState = 's'
            return 200
        elif axis == 'y':
            if value == 'plus': variables.translationState = 'd'
            if value == 'minus': variables.translationState = 'a'
            return 200
        elif axis == 'z':
            if value == 'plus': variables.translationState = 'q'
            if value == 'minus': variables.translationState = 'e'
            return 200
    except:
        return jsonify({'Error during translation', 400})
    
@app.route('/rotate', methods = ['post'])
def rotate():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'No body provided', 400})
        
        axis = data['axis']
        value = data['value']
        
        if axis == 'x':
            if value == 'plus': variables.rotationState = 'u'
            if value == 'minus': variables.rotationState = 'i'
            return 200
        elif axis == 'y':
            if value == 'plus': variables.rotationState = 'j'
            if value == 'minus': variables.rotationState = 'k'
            return 200
        elif axis == 'z':
            if value == 'plus': variables.rotationState = 'm'
            if value == 'minus': variables.rotationState = ','
            return 200
    except:
        return jsonify({'Error during translation', 400})