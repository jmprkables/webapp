from flask import Flask, request
import rethinkdb as r

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to jmprkableserver"

@app.route('/fall', methods=['POST'])
def fall():
    conn = r.connect("mr-karan.local", 28015)

    data = request.data
    dataDict = json.loads(data)
    try:
        status = dataDict["status"]
    except:
        return("Invalid data")
    
    r.db("hackiiitd").insert({
        "status": status,
        "timestamp": adsd
        })



if __name__ == "__main__":
    app.run(port=8085, debug=True, host="0.0.0.0")
