from flask import Flask, jsonify, request
import socket
import os
import time

app = Flask(__name__)

# Server-Identifikation
SERVER_ID = os.environ.get('SERVER_ID', 'unknown')
HOSTNAME = socket.gethostname()
PORT = int(os.environ.get('PORT', 8000))

@app.route('/')
def home():
    return jsonify({
        'server_id': SERVER_ID,
        'hostname': HOSTNAME,
        'port': PORT,
        'message': 'Hello from Web Server Lab!',
        'timestamp': time.time()
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'server_id': SERVER_ID
    }), 200

@app.route('/info')
def info():
    return jsonify({
        'server_id': SERVER_ID,
        'hostname': HOSTNAME,
        'port': PORT,
        'headers': dict(request.headers),
        'remote_addr': request.remote_addr
    })

@app.route('/slow')
def slow():
    """Simuliert langsamen Request (für Testing)"""
    time.sleep(2)
    return jsonify({
        'server_id': SERVER_ID,
        'message': 'This was slow!'
    })

@app.route('/error')
def error():
    """Simuliert Error (für Testing)"""
    raise Exception("Simulated error!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)