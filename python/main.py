from flask import Flask
import os
from utils.log_utils import log_config

app = Flask(__name__)
@app.route('/')
def hello():
    return f'Hello, World! Running on port {port}!'


# Run the Flask app
if __name__ == '__main__':
    log = log_config("haproxy_python_web_app")
    log.info("Starting Flask app")
    port = os.environ.get('FLASK_PORT', '5000')
    app.run(debug=True, host='0.0.0.0', port=int(port))
