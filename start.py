"""App entry point."""

import sys

from flask_cors import CORS

from app.create_app import create_app

sys.path.append("./app")
app = create_app()
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
