from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

# If app.py is in backend/ and detections/ is in the parent folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DETECTIONS_DIR = os.path.join(BASE_DIR, 'detections')
LOG_FILE = os.path.join(DETECTIONS_DIR, 'detection_log.csv')

@app.route('/api/logs', methods=['GET'])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify([])
    df = pd.read_csv(LOG_FILE)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
