import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "{data: " + str(random.randint(0,1)) + "}"


if __name__ == "__main__":
    app.run(port="8008", debug=False, host="0.0.0.0")
