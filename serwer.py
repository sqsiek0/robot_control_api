from flask import Flask, request, jsonify

app = Flask(__name__)
isRobotWork = True

@app.route('/control', methods=['POST'])
def control():
    data = request.get_json()
    if data is None:
        
        return "Invalid JSON data", 400
    
    return {'success': True}

@app.route('/working', methods = ['GET'])
def working():
    try:    
        if isRobotWork:
            isRobotWork = False
            return jsonify({'isWorking': isRobotWork}), 200
        else:
            isRobotWork = True;
            return jsonify({'isWorking': isRobotWork}), 200
    except:
        return jsonify({'Error during checking robot', 400})