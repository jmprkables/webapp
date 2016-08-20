from flask import Flask, request
import rethinkdb as r
import time
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to jmprkableserver"

@app.route('/fall', methods=['GET'])
def fall():
    timezone = time.strftime("%z")
    reql_tz = r.make_timezone(timezone[:3] + ":" + timezone[3:])
    the_date = datetime.now(reql_tz)
    timestamp = time.mktime(the_date.timetuple())
    json_date = the_date.isoformat()
    conn = r.connect("192.168.6.26", 28015)
    conn.use('hackiiitd')
    r.table('fall').run(conn) # refers to r.db('marvel').table('heroes')

    data = request.args.get('fallen')
    ''''
    dataDict = json.loads(data)
    try:
        fallen = dataDict["fallen"]
    except:
        return("Invalid data")
    '''
    r.table("fall").insert({
        "fallen": data,
        'from_object': the_date,
        'from_epoch': r.epoch_time(timestamp),
        'from_iso': r.iso8601(json_date)
    }).run(conn)

@app.route('/medicine', methods=['GET'])
def medicine():
    timezone = time.strftime("%z")
    reql_tz = r.make_timezone(timezone[:3] + ":" + timezone[3:])
    the_date = datetime.now(reql_tz)
    timestamp = time.mktime(the_date.timetuple())
    json_date = the_date.isoformat()
    conn = r.connect("192.168.6.26", 28015)

    data = request.data
    dataDict = json.loads(data)
    try:
        status = dataDict["status"]
    except:
        return("Invalid data")

    r.table("fall").insert({
        "status": status,
        'from_object': the_date,
        'from_epoch': r.epoch_time(timestamp),
        'from_iso': r.iso8601(json_date)
    }).run(conn)

@app.route('/door', methods=['GET'])
def door():
    data = request.data
    dataDict = json.loads(data)
    try:
        status = dataDict["status"]
    except:
        return("Invalid data")
    # if status is True increase the counter
    if status:
        r.table('aggregated').get(id).update(
            { 'count': (r.row['count'].default(0)+1) }
        ).run(conn)


if __name__ == "__main__":
    app.run(port=8085, debug=False, host="0.0.0.0")
