# [Scalable Microservices with Kubernetes](https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615)
This course is designed to teach you about managing microservices, using Kubernetes. This course is built in partnership with experts such as Google's Kelsey Hightower.

![trailer-screenshot]()


## Lesson 1: 
Intro to Microservices: Learn how modern, always-on applications use the microservices design pattern. 

Instructors are: 

    Kelsey Hightower @kelseyhightower
    Carter Morgan @_askcarter
    Adrian Cockcroft @adrianco
    Gundega Dekena @pytonc
 

Hot Industry Buzz Words:
- Containers 
- Microservices
- Kubernetes

What is behind the buzz hype?
- User demand for "always on" services. 
- Expect & Demand 24/7 everywhere access 

Used by Operations: 
- Sys Admin 
- Developer 
- Mananing Applications at Scale 

Automation Tools:
- Puppet 
- Chef 
- Ansible 

Course introduces distributed systems for automation. 
- Docker
- Kubernetes 

Cloud Application Lifestyle:
- Packaging into a container 
- Managing into production 

Understand: 
- Modern-day applications 
- new design patterns such as microservices 
- need for robust infrastructure 
- packages 
- distrubuting apps 
- docker image format 
- container technologies 
- running apps in distributed (cloud) platform 
- start small, scale to giant 

## Resources: 
* [Kubernetes: Up and Running, Kelsey Hightower](http://shop.oreilly.com/product/0636920043874.do)
* [Building Microservices: Defining Fine-Grained Systems](http://shop.oreilly.com/product/0636920033158.do)
* [Microservices: Pros](https://martinfowler.com/articles/microservices.html)
* [Microservices: Cons](https://martinfowler.com/articles/microservice-trade-offs.html)
* [12 Fractured Apps](https://medium.com/@kelseyhightower/12-fractured-apps-1080c73d481c)
* [Open Data: Small Pieces Loosely Joined]()
* [7
The State of the Art in Microservices by Adrian Cockcroft](https://youtu.be/pwpxq9-uw_0)
* [Microservices • Martin Fowler • GOTO 2014](https://youtu.be/wgdBVIX9ifA)
* [The Next Chapter in Native Cloud Computing - Craig McLuckie (Kubernetes Launch)](https://youtu.be/mPhjFYXoAD0)


Tech Used:
- [Go Programming Language](https://golang.org/) Our app is written in Go. If you’re not already using Go, you owe it to yourself to try it out. 
- [Google Cloud Shell](https://cloud.google.com/shell/docs/) - a ree temp VM preloaded with the tools need to manage our clusters.
- [Docker](https://www.docker.com/) use Docker to package, distribute, and run our application. 
- [Kubernetes](http://kubernetes.io/) for once we have an application, we use Kubernetes to handle the heavy lifting of managing, deploying, and scaling our application.
- [Google Container Engine (GKE)](https://cloud.google.com/container-engine/) -  a hosted Kubernetes service 

1.3 Evolution of Applications: 
- Adrian - Netflix.  
- Made microservices mainstream 
- used to have huge applications (5 million lines)
- hours to build 
- take a long time to run 
- used release software infrequently
- it was a lot of work to do it
- now we've sped it up!
- now we break the build time from hours into seconds
- wrap it into a container 
- test
- deploy 
- free up everone to go at their own speed 
- coodinate the pieces: you don't-thats a monolith
- let everyone release on their own cycle 
- deploy any piece independent of other pieces 
- face-to-face meetings are now an API release 
- container schedule 

1.4 Microservices 
- Architectural approach which includes: 
- it is modular 
- it is easy to deply
- it can scale independently 

The Microservice Design pattern benefits most from Rapid Depolyment and Continuous Delivery.

Microservices push the limits of most automation tools and infrastructure 

Microservices are one of the reasons we needed advanced tools like kubernetes 

1.5 Get the Source:
- Set up GCE account. 
- [Enable Cloud shell](https://cloud.google.com/shell/docs)
- Create a Project.  (Use [a new](https://support.google.com/cloud/answer/6251787) or existing GCP project 
- Enable Compute Engine API 
- Enable Container Engine API
https://developers.googleblog.com/2016/03/introducing-google-api-console.html
- [Explore Google cloud shell](https://cloud.google.com/shell/docs/quickstart)
- configure cloud shell environement 
```
Create two Cloud Shell Sessions and run the following commands to avoid setting the compute zone.

List available time zones:

gcloud compute zones list

Set a time zone example:

gcloud config set compute/zone europe-west1-d
```
- Download Go:

Note: Cloud Shell comes with an installed Go, but it's not the most recent version, so you should perform the steps below to install the latest Go and set GOPATH.
```
wget https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.6.2.linux-amd64.tar.gz
echo "export GOPATH=~/go" >> ~/.bashrc
source ~/.bashrc

Get the code:

mkdir -p $GOPATH/src/github.com/udacity
cd $GOPATH/src/github.com/udacity
git clone https://github.com/udacity/ud615

Get ready for the next lesson

cd ud615/app
```

1.6 Build and Interact with Monolith 
```
Commands to run
On shell 1 - build the app:

Make sure you are in the app directory and build the app:

cd $GOPATH/src/github.com/udacity/ud615/app
mkdir bin
go build -o ./bin/monolith ./monolith

Optional - if you run into errors building your go binaries, you probably need to install the dependencies first by running:

$ go get -u 

On shell 1 - run the monolith server:

sudo ./bin/monolith -http :10080

On shell 2 - test the app:

curl http://127.0.0.1:10080
curl http://127.0.0.1:10080/secure

On shell 2 - authenticate (password is password):

curl http://127.0.0.1:10080/login -u user

It prints out the token.

You can copy and paste the long token in to the next command manually, but copying long, wrapped lines in cloud shell is broken. To work around this, you can either copy the JWT token in pieces, or - more easily - by assigning the token to a shell variable as follows
On shell 2 - login and assign the value of the JWT to a variable

TOKEN=$(curl http://127.0.0.1:10080/login -u user | jq -r '.token')

Check that it worked:

echo $TOKEN

On shell 2 - access the secure endpoint using the JWT:

curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:10080/secure

On shell 2 - check out dependencies

ls vendor 
cat vendor/vendor.json

```

Testing 
We use "curl" to test our application. 
If we get a response back, it is working. 

1.7: 12-Factor Apps 
- Important for designing scalable applications 
- 12 Factor are the best practices for building deployable software as a service - - 12 factor acts fit these criteria: Porability, Deployablility and Scalabililty.
- Portable: because they focus on eliminating elements that vary between execution environments (like depenencies and configurations)
- deployed on cloud platforms 
- continuaously deployable 
- we will be able to scale to user demands when built like this 


Find out more about the 12-factor manifesto here: http://12factor.net/

1.8 12-Factor QUIZ: For each item, enter the related factor from https://12factor.net

Code is stored in Git: Codebase
Output goes to stdout: Logs 
Import Statements: Dependencies 

1.9 refactor to MSA 
- Refactor: break down our monolith application into microservices 
- break the monolith around functionality which is self contained 
- the example uses a hello and auth service which is its own binary 
- additional complexity
- need clients to be able to talk to more and more containers as complexity grows

```
Shell 1 - build and run the hello service

go build -o ./bin/hello ./hello
sudo ./bin/hello -http 0.0.0.0:10082

Shell 2 - build and run the auth service

go build -o ./bin/auth ./auth
sudo ./bin/auth -http :10090 -health :10091

Shell 3 - interact with the auth and hello microservices

TOKEN=$(curl 127.0.0.1:10090/login -u user | jq -r '.token')
curl -H "Authorization:  Bearer $TOKEN" http://127.0.0.1:10082/secure

```

1.10 Microservices Architectures are Solutions to which of the following problems? 
Slow application speeds (Microservices doesn't help) 
Tightly coupled compoonets (microservices helps) 
Maintenance (microservices helps) 

1.11 JWT  JSON Web Tokens 
- pronounced as jot
- useful standard
- can be verified
- compact info 
- authentication
- information exchange 
- they can be signed 

1.12 JWT 
JSON Web Tocken 

Here's the JWT token to test copy from here and paste at https://jwt.io/ :

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpXVCBtYWRlIGVhc3kiLCJhZG1pbiI6dHJ1ZX0.RhS5_R99IA0u_UffKr8xDh05Ob9Lb-kOBlmOWlspcc0

paste that token into the "encoded" field and check the payload section 

Enter the payloads name field: 

1.13 How does JWT work 
Example: 

Client     Server 

- The client wants to access the info on the server.  
- The server will only give the data to a trusted client. 
- The client sends its data to the server.
- the server validats it and returns a token
- the client saves the jwt token
- the server re-verifies the token to be certain it hasn't been tampered with
- the server sends the info to the client 
 

1.14 outro 
- Modern apps are pushing the limits 
- Modern application design 
- no longer one large bianary
- now composed of smaller, independent bianaries 
- rethink of tooling and practices 


## Lesson 2: 
* Building the Containers with Docker: Use Docker to build container images that package an application and its dependencies for deployment on a single machine. 
* Started: 2021-06-19
* Completed: 2021-06-19
* This lesson provides a work along instruction and quiz intro to using docker. 
* The previous lesson gave us a great overview understanding of modern application design.
* Our next step is to deploy our code. 


## Lesson 3: 
Kubernetes: The infrastructure to support an application at scale is as important as the application itsself.  See how Kubernetes allows you to focus on the big picture. 


## Lesson 4: 
Deploying Microservices 


Once a student has completed this course, Udacity recommends taking: [Machine Learning Engineer](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)
