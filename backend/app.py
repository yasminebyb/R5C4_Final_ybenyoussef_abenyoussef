from flask import Flask
from flask_cors import CORS
from controllers.search_controller import search_bp
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})


# Enregistrer le blueprint
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)

