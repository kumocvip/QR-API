from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
latest_qr = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/send', methods=['POST'])
def send_qr():
    global latest_qr
    data = request.get_json()
    latest_qr = data.get('qr')
    return jsonify({"status": "ok"})

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify({ "qr": latest_qr })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)