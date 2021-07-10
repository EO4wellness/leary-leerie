# Lesson 2
* Considering Architecture 
* When we need to build an application, we first: 
  - need a list of requirements it must meet 
  - the list defines the structure
  - this helps with the design of the application 
  - aim: to build without fundamental flaws (which customers hate) 
  - this saves time and effort 
* migration process: moving an application from development to deployment 
* all applications have trade offs
* design the application with this in mind 
* design patterns: monolith and microservices 
* examin trade offs of each model 
* discover the best practices to adopt in the immplementation stage 
* Optimize: 
- visibility 
- management
- troubleshooting 
- timeframe to implement 
*  Requirements and available resources may dictate which architecture is most suitable for a project 

## 2.1 Intro: Lesson 2 Goal: 
* By Lesson 2's end, we should be able to evaluate the most suitable architecture for an application
* Considering: 
- functional requirements 
- available resources 
- time frame 

## 2.2 Design Considerations for Cloud-Native Applications
* Goal: Designing a cloud native application 
* Allocate time for Context Discovery 
* this helps us define the overall structure 
* this also helps to define the design of the components 
* making this step, first, help contribute to maintainable projects 
* minimal engineering effort to add new features in the future 
* Context Discovery Process: 
1. List Functional Requiremes 
Answers the question: What should this application / service deliver to consumers? 
2. List all available resources.
Answers the question: What will help with the implementation of this project? 
* The answers are two data points of the context discovery process needed to discover which architecture works best for the project 
* context discovery must include the buisness requiremtns 
* need to know what functionality needs to be implemented
* to whom should that new functionality be implemented to 
* Answer basic questions:
1. Who are the stakeholders? 
2. Who requires this application? 
3. Who is sponsoring this application? 
4. What functionalities are needed? 
5. Who are the end consumers or customers? 
6. Is it an internal tool for employees to use? 
7. Is it a customer-facing application?
8. How should inputs be processed? 
9. How should outputs be processed? 
10. Should there be notifications? If so, which ones?  If not, why not? 
11. Does the customer need to input info for the function to execute successfully? 
12. Which engineering team can build the application? 
13. Which build team(s) have the skill(s) and available time frame to implement the project? 
14. Which aspects can facilitate or block the product release? 
15. What are the available engineering resources? 
16. If no one is available, do we have the ability to hire contractors to do the work? 
17. What is the budget for the project? 
18. Is there any urgency to bring this to the market? 
19. What is the expected time frame? 
20. Which tools or languages should be used for development? "Internal Knowledge" 

## 2.3 [Monoliths and Microservices:](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/fcc8c401-8331-4214-9609-f2f8529f50a1/concepts/e883bfb7-b199-4351-b7ee-355a0429fb87)


## 2.11: [Exercise: Endpoints for Application Status](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/fcc8c401-8331-4214-9609-f2f8529f50a1/concepts/a0b4638d-2ca8-4c49-90c8-ea6e729f2552)
- Goal: aims to extend a Python Flask web application with status and metrics endpoints. 
- Environment Setup
```
Set up your environment to extend a Python Flask application:
1. Clone the course exercise repository using GIT. 
https://github.com/udacity/nd064_course_1

2. Navigate inside the _exercises/python-helloworld_ folder 

3. Using Python or Flask run commands, run the app.py application

4. Access Hello World application on your local browser (note: Python Flask uses port 5000 by default) 

5.  Open your editor of choice (IDE or VIM) to edit the HEllo World application

```
Once all the pre-requisites are completed, you can get started on developing endpoints to describe the application state.
Exercise

Extend the Python Flask application with /status and /metrics endpoints, considering the following requirements:

    Both endpoints should return an HTTP 200 status code
    Both endpoints should return a JSON response e.g. {"user": "admin"}. (Note: the JSON response can be hardcoded at this stage)
    The /status endpoint should return a response similar to this example: result: OK - healthy
    The /metrics endpoint should return a response similar to this example: data: {UserCount: 140, UserCountActive: 23}

Tips: If you get stuck, feel free to check the [solution video](https://youtu.be/Kj_hGnViybg) where detailed operations are demonstrated.


## [L2.12: Solution: Endpoints for Application Status](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/fcc8c401-8331-4214-9609-f2f8529f50a1/concepts/4bf9175a-b8f9-4679-9337-5b5e7b4f1c37)
After watching this solution/walk through, since our instructor specifically mentioned Firefox or Chrome for testing, I want to try this same testing on other browsers and see if any fail, or if all chrome-based or firefox-based browsers work too, just out of curiousity sake. 

## L2.13 

## L2.14 "Implementing logging is going to be very specific to the framework that you are using. Most of the time there are already libraries that are available for you to use to implement basic logging capabilities. This is the case with flask as well."   as we have seen in our work-through of these codes. 

## L2.15: Morphing, constant movement. Consider if the structure of the project is enabling or blocking the new feature development(s). 

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
