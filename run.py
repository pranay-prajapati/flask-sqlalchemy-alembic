from flask import Flask
import os

app = Flask(__name__)

if __name__ == "__main__":
    os.system("alembic upgrade head")  # upgrade database to latest version
    app.run(debug=True)
