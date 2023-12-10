from flask import Flask, request, jsonify
import variables

app = Flask(__name__)


@app.route('/control', methods=['POST'])
def control():
    data = request.get_json()
    if data is None:
        
        return "Invalid JSON data", 400
    
    return {'success': True}

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