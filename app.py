from flask import Flask
from flask_cors import CORS

from blueprints import analyzer

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-type"

app.register_blueprint(analyzer, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
