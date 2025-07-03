from flask import Flask, request, jsonify

app = Flask(__name__)
latest_qr = None

@app.route('/send', methods=['POST'])
def send_qr():
    global latest_qr
    data = request.get_json()
    latest_qr = data.get('qr')
    return jsonify({"status": "ok"})

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify({"qr": latest_qr})
