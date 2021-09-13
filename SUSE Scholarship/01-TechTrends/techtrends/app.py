from flask import Flask
from flask import json
import logging 

app = Flask(__name__)

postsCounter = 0
def get_db_connection():
    global postsCounter
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.row_factory
    postsCounter += 1
    return connection

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    ## added log line
    app.logger.info("Status request successful")
    return response

@app.route('cd')
def healthz():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    ## added log line
    app.logger.info("Status request successful")
    return response

@app.route('/metrics')
def metrics():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts'.fetchall())
    connection.close()
    response = app.response_class(
            response=json.dumps({"status": "success", "code": 0, "data": {"db_connection_count": PostsCounter, "post_count": len(posts)}}),
            status=200,
            mimetype='application/json'
    )
    ## added log line
    app.logger.info("Metrics request successful")
    return response

@app.route("/")
def hello():
    ## added log line
    app.logger.info("Main request successful")
    return "Hello World!"

if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port='3111')