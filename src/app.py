# -*- coding: utf-8 -*-
import logging
from flask import Flask

# Enable logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    return f"Secret Key: {os.getenv('API_KEY', 'No Secret')}"

if __name__ == '__main__':
    print("🔥 Starting Flask server on http://0.0.0.0:5000/")
    app.run(host="0.0.0.0", port=5000, debug=True)



