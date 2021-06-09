# Lesson 2

## Problems/Solutions: 
L2.11 and L2.12:
https://www.youtube.com/watch?v=0eQqnULB1qk 

L2.14
```
 "{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"
```

```
import logging
import sys
def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        file_handler = logging.FileHandler('app.log')
        formatter = logging.Formatter(
            "%(asctime)s— %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger
```

```
from flask import Flask
from .utils.logger import get_logger
app = Flask(__name__)
logger = get_logger(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/status")
def status():
    logger.debug('"/status" was reached')
    return {"result": "OK - healthy"}
@app.route("/metrics")
def metrics():
    logger.debug('"/metrics" was reached')
    return {"data": {
        "UserCount": 140,
        "UserCountActive": 23
    }}
if __name__ == "__main__":
    app.run(host='0.0.0.0')
```
For the above code to work, I created a package, utils and added the file logger.py which had my get_logger(name) function I have shared above. also made the python-helloworld a package.

directory structure:
```
python-helloworld
├── __init__.py
├── app.log
├── app.py
├── requirements.txt
└── utils
    ├── __init__.py
    └── logger.py
1 directory, 6 files
```

things in {{ }} are placeholders for example you can write status instead of {{ ENDPOINT_NAME}} and {{TIMESTAMP}} is already added when you run app.py we are just using the output and store it in logs.
You can add timestamp by getting it from modules like datetime, time, etc. But IMO, it's not required as we already get time in logs
INFO:app:/status endpoint reached successfully
INFO:werkzeug:192.168.0.107 - - [08/Jun/2021 08:05:26] "GET /status HTTP/1.1" 200 -
You can see from this example that timestamp is automatically logged by werkzeug
I hope it makes sense, if not feel free to ask further.

A log line should be recorded the timestamp and the requested endpoint e.g. "{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"
This is the exact instruction from Exercise page, you can see that it's just an example not the required format. In the end, it totally depends on you, that which logs are most beneficial for you. For me personally, having to write more code just to log time which BTW is already being logged is not a good approach.

In the course solution, they add the line:
```
if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
```
The line logging.basicConfig(filename='app.log', level=logging.DEBUG) allows writing logs to app.log filename
Actually, I did the exact thing but it didn't write. I searched a little bit and move the line logging.basicConfig(filename='app.log', level=logging.DEBUG) out of this if and it works.

It depends on how you run the application. if you use flask run , code inside if __name__ == '__main__':  will not run. if you use python {{filename.py}}  it should work.

local, and remote. Suppose you log and collect the logs remotely and index by Elastic Search, you'll reduce the time of incident detection.

https://www.manning.com/books/microservices-patterns?a_aid=microservices-patterns-chris&a_bid=2d6d8a4d

https://flask.palletsprojects.com/en/1.1.x/logging/

https://microservices.io

I didn't have good intuition as to what they meant by ECOsystems in regards to these topics UNTIL I saw [this video](https://www.youtube.com/watch?v=t7iVCIYQbgk) recomended by a fellow student(Giorgio Zoppi) intro: "...1600 microservices in our ecosystem and growing..." makes the point better than dictionary definition on this. 
