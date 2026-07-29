from flask import Flask
from routes.risk_routes import risk_bp
from database.database import create_database

app = Flask(__name__)

app.register_blueprint(risk_bp)

create_database()

@app.route("/")
def home():
    return "GovernX Backend Running Successfully"

if __name__ == "__main__":
    app.run(debug=True)