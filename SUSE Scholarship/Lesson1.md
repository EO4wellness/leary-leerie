# L1
* [Recommended Milestone Deadline: Week 1](https://drive.google.com/file/d/1Y8Hup0sZok_h2vmbZgyFt2zFHffqTtYk/view)
* Week 1: June 7 – 11, 2021 
* Began Lesson 1: June 7
* Completed Lesson 1: June 8

# Lesson 1 Overview:
1.1 [Meet Your Instructor](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#11-meet-your-instructor): Katie Gamanji  @k_gamanii 


1.2 [Prerequisites](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#12-must-be-comfortable-with)


1.3 [Course Outlilne](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#13-course-outline)


1.4 [Introduction to Cloud-Native](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#14-introduction-to-cloud-native-)


1.5 [CNCS and Cloud-Native Tooling](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#15-cncf-and-cloud-native-tooling)


1.6 [Stakeholders](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#16-stakeholders) 

1.7 [Tools Environment and Dependencies](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#17-tools-environment-and-dependencies)

1.8 [Recap](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#18-recap)

1.9 [Good Luck!](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/Lesson1.md#19-good-luck)

## 1.1 Meet your Instructor 
 - cloud platform engineer 
 - enable developers to deploy their application 
 - looks at deploying with minimal effort 
 - best accomplished thru a high-degree of automation 
 - scaling 
 - upskilling 
 - constant iteration 
 - user feedback 
 - service mesh 
 - policy based access management 
 - TOC (technical Oversight Committee) member 
 - CNCF (Cloud native computing foundation) 
 - advocate for vender nutrality 
 - KEPTN (a sandbox CNCF project) 
Terms 
- CI/CD Pipeline
- Container / Containerize 
- Application 
- Kubernetes
- Kubernetes Cluster 
- Cloud Platform Engineer 
- Platform Maintanance 
- Developers 
- Deploy Applications 
- Host Applications 
- Automation 
- Upskilling
- Iterations 
- User Feedback 
- CNCF (Cloud Native Computing Foundation) 
- Ecosystem
- Ecosystem Advocate 
- End-User Community 
- Keptn 
- sandbox CNCF project 

## 1.2 Must be comfortable with: 
 - be comfortable wtih web application development 
 - write a web application with multiple API endpoints in python 
 - use a framework such as flask 
 - CLI (command-line interace)
 - use commands to navigate directories 
 - create files 
 - install packages 
 - know and use git commands 
 - create or clone a repo 
 - make changes 
 - commit to a main branch 
 - create a docker hub account 
 - create or have a git account 
* web application development with Python (ie: writing a web application with multiple API endpoints in Python or familiar with a framework like Flask)
* Using CLI (Comand-Line Interface) (create and navigate directories by command, create files, install packages, binaries, etc)
* using git commands (create or clone a repo, make changes, comitt them to a branch) have a github account
* create DockerHub account (we will be pushing images to the public registry) 
* used in course
* install now
* follow along all demos and examples 

## 1.3 Course Outline: 
* course long-looking at realistic examples 
* pratice applying good development practices 
* containerize an application before release 
* use automated CI/CD pipeline 
* Introduction to Microservice Fundamentals 
* Overview Cloud-Native ecosystem 
* architectural models 
* consider these when developing applications 
* design paterns: 
  - monoliths 
  - microservices 
* best practices
* implementation stage 
* optimize applications 
* how to package applications 
* Use of Docker 
* deploy it 
* Kubernetes cluster 
* configurations: 
  - declarative 
  - imperative 
* deploy Kubernetes cluster using K3s
* evaluate 
* PaaS (Platform as a serivce) 
* use of Cloud Foundry for deploying applications 
* underlying infrastructure 
* use of cloud-native tooling
* construct CI/CD pipeline 
* Deployment Mechanisms:
   - GitHub actions 
   - Argo CD
* Template Configuration Managers:
  - Helm 
* Walk thru realistic examples
* Follow allong with each video
* Overview of Cloud Native ecosystem 
* Architectural models to be considered 
* design patterns 
* best practices at implmentation 
* package an application 
* deploy kubernetes 
* paas solution 
* cloud foundry use 
* CI/CD 
* cloud native tooling 
* ARGO CD 
* template configuration managers: HELM 
* containers 
* microservice based architecture 
* tools in Cloud Native ecosystem 
* traceability 
* stakeholders 
* key points to consider (tech and business prospectives) 
* tools to install throughout course
* follow demos and exercises with solutions closely 

- Introduction to Cloud Native
- Introduction to Principles Cloud Native Advocates. 
- Containers: closely correlated with microservice-based architecture 
- Cloud-Native ecosystem tools 
- Kubernetes: Framework to manage containers at scale 
- Kubernetes Integration with tools which provide: 
  -- Networking
  -- Storage 
  -- Service Mesh 
  -- Traceability 
  -- more 
- Stakeholders: Those who will consider adoption of cloud-native tooling
- Key points for stakeholders to consider 
  -- technical perspective 
  -- business perspective 
- Tools, Environment & Dependencies

## [1.4 Introduction to Cloud-Native ](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/092ac437-081d-4946-b54d-a2f537931c13/concepts/6197dd89-0c18-4bb1-998d-e7baa69aef65) 
- Cloud-native: is the the set of practices that empowers an organization to build and manage applications at scale. 
- Cloud-native can achieve using private, hybrid, or public cloud providers. 
-- needs to be agile 
-- needs speed
-- integrating customer feedback
-- adapting to technology
* Cloud Native Tooling 
* Cloud Native Applications 
* "Cloud native refers to the set of practices which empowers an organization to build and manage applications at scale, 
 while using private, hybrid, or public cloud providers." 
* the key to cloud native deployment is SPEED and AGILITY 
* this means how quickly an organiation can respond to change
* while increasing its feature velocity 
* containers are closely-associated with Cloud Native terminology 
* containers are SMALL and MANAGEABLE units 
* containers have an application running inside 
* container pros: 
  - can be deployed FAST
  - is RESILIENT 
  - is Easily Managed 
* microservice architecture is often chosen 
* miscroservices represents 
  - small services 
  - independent services 
  - can be easily containerized 

## [1.5 CNCF and Cloud-Native Tooling](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/092ac437-081d-4946-b54d-a2f537931c13/concepts/79ae4fb8-2601-43f5-a879-8470d4a6c21c)
* Tools to manage containers at scale
* Container Orchestrators
  - Docker Swarm 
  - Apache Mesos 
  - Kubernetes 
* Kubernetes took the lead to define. 
* Kubernetes started in 2015 from Borg, a google-open source container orchestrator.
* Kubernetes is now a part of CNCF
* CNCF is Cloud Native Computing Foundation 
* CNCF was founded in 2015
* vendor neutral home to open-source projects 
  - Kubernetes
  - Prometheus 
  - ETCD
  - Envoy
  - more 
* Kubernetes is a container orchestrator that is capable of solutionize the integration of the following functionalities:
  - runtime
  - netowkring
  - storage 
  - service mesh
  - logs and metrics
  - tracking 
* need a tool to manage containers at scale 
* overtime multiple tool appeared 
* Examples: Docker Swarm, Apache Mesos, Kubernetes 
* Kubernetes took the lead. 
* Kubernetes sucecss: 
  - how containerized workloads should be deployed
  - managed
  - configured 
* Kubernetes grew out of Borg 
* Borg was a google open-source software that orchestrated containers 
* Kubernetes was released in 2014. 
* Kubernetes is now maintained by CNCF
* Cloud Native computing Foundation (CNCF)
* Kubernetes is a container orchestrator. 
* Kubernetes automates configuration, management, and scalability of an application. 
* Following, Kubernetest capabilities were extended. 
* Now Kubernetes inegrates wtih other tools 
* Now includes: 
  - runtime for application execution environment 
  - network for application connectivity 
  - storage for application resources 
  - service mesh for granular control of traffic within a cluster 
  - logs and metrics to construct the obervability stack 
  - tracing for building the full request journey 
  - many more 
* most of these tools are maintained under the CNCF umbrella 
* CNCF was founded in 2015
* CNCF provides vendor-neutrol home to open source projects 
 - Kubernetes 
 - Prometheus 
 - ETCD 
 - Envoy 
 - many more (more than 1,300 associated projects) 

## [1.6 Stakeholders](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/092ac437-081d-4946-b54d-a2f537931c13/concepts/a4eb94d3-e658-475d-bffe-04adf05e2776)

## [1.7 Tools Environment and Dependencies](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/092ac437-081d-4946-b54d-a2f537931c13/concepts/41d3074d-ccc2-4fc0-a153-ba7a4ba77b3b)
Intall: 
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/get-docker/)
- [Vagrant](https://www.vagrantup.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) version 6.1.16 or higher 


## [1.8 Recap](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/092ac437-081d-4946-b54d-a2f537931c13/concepts/e9ed564e-e3c6-4052-971c-e64fd8f57052)
Summary

In the first lesson, we went through:

    Introduction to Cloud Native
    CNCF and Cloud Native tooling
    Stakeholders
    Tools, Environment & Dependencies


## [1.9 Good Luck](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/092ac437-081d-4946-b54d-a2f537931c13/concepts/74cf0724-e862-4851-91c3-f9c698c8b63c)
* Adapt quickly
* change as needed
* innovation 
* tech changes 
* containers
* automation 
* cloud-native projects and tech 
* lead a transition to modern infrastrcture 

## Resources:
Fellow students in the scholarship offered these fabulous resources to sumarize this week's study. 

1 - Cloud Native 101:
https://www.youtube.com/watch?v=9Ik96SBaIvs

2 - Container and Kubernetes 101:
https://www.youtube.com/watch?v=gFozhTXOx18

3 - Virtual Machines vs Docker Containers - Dive Into Docker:
https://www.youtube.com/watch?v=TvnZTi_gaNc

4 - Containerization Explained:
https://www.youtube.com/watch?v=0qotVMX-J5s

5 - Introduction to Kubernetes and Docker:
https://www.youtube.com/watch?v=PfRWP60qxPM

6 - Kubernetes vs. Docker: It's Not an Either/Or Question:
https://www.youtube.com/watch?v=2vMEQ5zs1ko

7 - Review:
https://www.youtube.com/watch?v=1xo-0gCVhTU

8 - Vagrant Cheat Sheet: 
https://learn.hashicorp.com/vagrant

9 - Vagrant Cheat Sheet:
https://gist.github.com/wpscholar/a49594e2e2b918f4d0c4


2021-06-13 Today we are to conclude our week one of studies in the course and the course milestone suggestions include we should be done with lesson one by the end of today.  I posted in the student slack seeking to help anyone who hasn't finished.  I'm currently in lesson 3, so I'm good as far as meeting the suggested deadlines. 
