from flask import Flask, request

app = Flask(__name__)

@app.route('/control', methods=['POST'])
def control():
    data = request.get_json()
    if data is None:
        return "Invalid JSON data", 400
    
    return {'success': True}