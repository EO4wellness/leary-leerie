# Lesson 1: Introduction to Cloud Observability

### 1.  Meet your instructor: Jay Smith 
* App Modernization Specialist @ Google Cloud 
* Customer Engingeer - help people learn to use Kubernetes
* kNative 
* serverless platforms
* Tekton
* CI/CD pipelines 

### 2. Course Overview 
* Examines Cloud Native Observability
* What does monitoring and observability look like today?  
* Tools to collect: 
   1. system information. 
   2. application information. 
   3. create a dashboard. 
* Learn Best Practices of: 
	1. SLO
	2. SLI
	3. KPI
* to become an observability expert you must learn: 
1.  Intro to Cloud Observability 
2.  Observability tools
3. SLOs SLIs and KPIs 
4. Tracing
5. Building Dashboards 
* Prometheus:  Data collection tool; collects system information. 
* Jaeger: collects application information. 
* Grafana: visualize the information which has been collected. 
* Metrics we want to measure: SLO, SLI, KPI
* SLOs: Service level objectives 
* SLIs: Service level indicators
* KPIs: Key performance indicators 
* Distributed Tracing 
* Create a span to execute a trace on an application 
* Grafan sources, once set up, allows us to collect all the data we need
  to make a dashboard.
* Best Practices to at-a-glance observability
* [Resource: Glossary](https://github.com/EO4wellness/leary-leerie/blob/master/SUSE%20Scholarship/03-MetricsDashboard/Resources/glossary-for-cnand-c4-observability.pdf)

```
Course Outline

Here's an outline of all the lessons and topics in this course, for your reference.
Lesson 1: Introduction to Cloud Observability

In this first lesson, we'll go over the big picture. Why is observability relevant? And what is your role is as an observability engineer? What tools will you need to be able to conduct observability on your cluster?

    Big Picture: Monitoring in Clusters. We'll introduce the big picture of what cloud observability is and how monitoring developed.
    Business Stakeholders. As a cloud observability expert, it's important to understand who the various stakeholders are that you'll be interacting with, so you can understand the sort of events you need to monitor for and how others will be using this information.
    Where to Use Observability. We'll also talk about the conditions under which observability can be applied, and make a distinction between monitoring your system and observing the individual events within an application.
    Prerequisites. We'll briefly go over the skills and concepts you should already have in order to ensure success in this course.
    Tools, Environment and Dependencies. Finally, we'll go over a few technical requirements, along with the software and tools you'll need to install for this course.

Lesson 2: Observability Tools

This lesson will get you set up with the tools you need to start doing observability in your cluster.

    Understanding your components. First, we'll look at the big picture. We'll consider three major needs that we will encounter when trying to do observability: System data, application data, and data visualization. Then we'll discuss why the three tools we're going to use—Prometheus, Jaeger, and Grafana—are great choices for addressing each of these needs.
    Installing Prometheus, Grafana, and Jaeger. Next, we'll get into the details of how to install Prometheus, Grafana, and Jaeger, and how to confirm that the installations were successful.
    Edge Case: Using ELK. Although the tools we are using in this course are excellent, industry-standard tools, it's always good to be aware of other options you may run into during your time as an observability expert. So at the end of the lesson, we will briefly consider ELK or Elasticsearch, Logstash, Kibana, which is a stack that serves as a popular alternative to the one we use in this course.

Lesson 3: SLOs, SLIs, and Error Budgets

This lesson is all about reliability metrics. In order to observe performance, we first need to get clear on how we are defining and measuring it, and that's what we'll cover here.

    Defining performance. The first thing we need to do is define what we mean by site reliability or performance. We will talk about performance in terms of providing a certain level of service, and we'll go over what are called the four golden signals that are used in site reliability modeling.
    Service-Level Objectives (SLOs). We also need a clear objective or goal, and this is where Service-Level Objectives (or SLOs) come in. We will talk about what SLOs are and what factors to consider when setting them.
    Service-level indicators (SLIs) . Once we have a clear definition and objective for the level of performance we want to deliver, we need to consider how we will actually measure this performance. This is done using Service-Level Indicators or SLIs.
    Error Budgets. Since we cannot guarantee 100% performance, we need to plan for errors. For example, if we are OK with 99% reliability on a metric, that means we have an error budget of 1%. We are deciding that if things get any worse than that 1%, this is a signal to us that an improvement is needed.
    Building SLAs. Finally, we will bring this all together and examine Service-Level Agreements or SLAs. While you personally won’t have to worry about SLAs as an SRE, it is important to understand the context of SLAs as it does play a part in the overall SRE model.

Lesson 4: Tracing

This lesson is all about tracing. Tracing will allow us to get performance data on our applications, particularly on the latency of the key processes within them.

    Big Picture: What is tracing? First we will talk about the underlying concept of tracing and how it is different from logs. In particular, we will consider why tracing is increasingly popular in diagnosing latency issues.
    Distributed Tracing. In order to do tracing on our Kubernetes cluster, we need an approach to tracing that can handle microservices. This is called distributed tracing. We will explain what distributed tracing is in the context of Kubernetes applications and why this is such a useful tool.
    Jaeger. Our tool for distributed tracing is Jaeger. We will discuss the key features of Jaeger as well as the main standards it uses, which are the OpenTracing and OpenTelemetry models.
    Python Application Tracing. With Prometheus and Grafana, once we installed them they were pretty much ready to go. In contrast, in order to do tracing with Jaeger, we have to actually add code into the application itself to run a trace. We will walk through how to do this with Python applications.
    Revisiting Logging. Finally, we will revisit logging. Although tracing is incredibly useful for issues involving latency, this doesn't mean that you should abandon logging. We will look at some use cases when you will want to utilize logs and consider how how logs are still useful in tracing.

Lesson 5: Building Dashboards

In this lesson, we'll look at how we can use Grafana to visualize the data we've been collecting with Prometheus and Jaeger, so that we can see the performance of our system and application at a glance.

    Starting with dashboards. First, we'll look at how to set up dashboards with Grafana, and we'll learn the key features of the dashboard UI.
    Panels. Next, we'll create panels. These are essentially containers for charts and graphs within our dashboards.
    Metrics. Then we will discuss how to use the Prometheus Query Language (PromQL) to track metrics on our cluster, and how to use Jaeger to track metrics on our application.
    Edge case: Alternative tools. Finally, we'll look at some alternative tools and learn some of the best practices concerning when we might want to use something other than the Prometheus-Jaeger-Grafana stack for monitoring and observability.


```

### 3. What You'll Build 
* Project: end of course 
* all in one view instead of viewing a bunch of logs 
* build a kubernetes cluster
* create a namespace called monitoring
* install prometheus and grafana tools 
* create a namespace for observability
* install Jaeger
* create a default namespace and install our application in it 
* create your own observability dashboard
* can be used to become an observability engineer

```
For the project at the end of this course, we will create a metrics dashboard. To accomplish this, you'll:

    Build a Kubernetes cluster
    Create a monitoring namespace, in which we will install our monitoring tools, Prometheus and Grafana
    Create an observability namespace, in which we will install our observability tool, Jaeger
    Create a default namespace, where we will install our sample application so we have something to monitor

At the end of this process, you'll have your own observability dashboard!

```

### 4. What is Observability/Why do you need it? 
```
Monolithic Applications vs Microservices

Let's review the distinction between monolithic applications and microservices:

    Monolithic applications. Monolithic applications have all the services bundled together. The user interface, business logic and data layer are all stacked on top of each other, such that making changes to one service can cause all the others to have issues as well.
    Microservices. In contrast, with microservices, all of the functions are separated into standalone services that work asynchronously and are distributed in nature. If one service has issues, this does not necessarily impact the rest of the application. Also, due to their small size and portability, microservices are great for Cloud Native development.

Black Box Monitoring vs White Box Monitoring

There has always been a need to monitor application performance, but the approach to monitoring has changed over time.

    Black box monitoring. Historically, we have used black box monitoring, which involves getting indirect data about the system (such as disk errors, hypervisor resource alerts, or hardware uptime) from the outside and then using this to attempt to infer the cause of a problem (without being able to view the source of the problem directly).
    White box monitoring. In white box monitoring, we look inside and get direct data on the application (such as user utilization, HTTP status errors, and SQL queries); we can directly observe the root cause of the issue.

Observability

    Without observability, we would often have to search through every single service to identify a problem.
    With observability, we can look inside the application and even trace through the execution of the application to gather detailed performance data on its individual components.
```

* Clusters 
* Monolithic services were difficult because they were stacked upon one another 
* if any changes were needed, it was a nighmare
* Microservices fixed this. 
* Easier to scale
* Easier to develope

* Monitoring
* used to use black-box monitoring 
* examples:  disk error report, hypervisor resource alerts, hardware update--all indrect
* indirect indicators 
* white box monitoring: look inside and see what's happening 
* examples: SQL queries, https status errors, user utilization
* life is hectic without oservability 
* if you cannot see what's broken, you don't know what to fix= too much searching just to start to fix it 

![l1.4]()

### 1.5: Business Stateholders 
```
In a business we have a number of stakeholders that are involved in observability:

    Customers and users should be the most important stakeholders when it comes to observability, since serving them is typically the main point of the product in the first place (and the ultimate source of revenue, if it is a paid product). They are the ones using our app and we want to make sure that they're having the best experience that they possibly can.
    Product managers want to ensure that our customers and users are having the best experience, and that our product is represented properly.
    Engineering managers invest a lot of time developing the application and thus have a vested interest in ensuring the product works as intended.
    Release managers want to simplify the release process. Anytime they can use observability data to catch an error upon deployment, this can make it easier for them to rollback any problems that occur.
    Development teams want feedback so they know what they need to fix and observability teams need the same feedback, so that they know what to change when it comes to system adjustments.
    Partners may have pipelines that are integrated with your apps. It's very important to them that both sides of the application are working to ensure that that the pipeline is functioning correctly.
    Investors want to make sure that the application is healthy so that they have confidence in the reliability and performance of the key product driving the business.
    Executives want to ensure that the application is working correctly, especially if it is an application that the business (and the bottom line) are centered around. Executive know that if the customers are having a reliable, high-performance experience with the app, this will contribute to their satisfaction and have a positive impact on revenue.

As you can see, there is a wide variety of stakeholders who all have an interest in observability data. As an observability expert you'll want to keep all of these stakeholders in mind and ensure they are getting the data they need.

```
* We need the right tools to make certain we help everyone.
* Everyone has different points of view and needs 

### 1.6 Monitoring and Observability 
* What is it. 
* WHere are we using it

Monitoring and Observability

Observability has traditionally been broken down into two components: Monitoring and observability. Let's discuss where we would apply each of these approaches and what the distinction is between them.
Monitoring

In monitoring, we are looking at the system or infrastructure itself. In the context of this course, the system would be a Kubernetes cluster. Monitoring is obviously valuable, but does not tell us what is happening inside of our applications. If an app has performance issues, monitoring will not give us insight on the cause of the issue.
Observability

In observability, we can directly see the internal workings of our applications, including the performance of individual functions and processes. This helps us track down any problems that may exist within the app, or simply identify areas where there is room for improvement in the app's performance.

    Remember, we monitor systems and observe applications.

Use Both!

Having both of these tools lets us get a full picture of both the application and the system it's running on. Note that although these are distinct concepts, they are so often used together that you'll commonly hear people say "observability" when they mean monitoring and observability.


### 1.7 Prerequisites
To be successful in this class, you should have:

    Experience writing basic Python scripts
    Working knowledge of Shell / Terminal
    Working knowledge of Vagrant
    Experience using a terminal-based text editor like Vi(m) or Nano
    Experience with Kubernetes & kubectl
    Basic familiarity with REST requests (e.g., GET and POST)

### 1.8 Tools, Environment & Dependencies
Here are all the things we'll need for this course.

    8 GB of Memory (we will use 2–4)
    VirtualBox
    Vagrant
    OpenSuse Image
    Prometheus, Grafana, Jaeger
    K3s

You don't need to worry about all of the installation and setup for these right now—we'll install and configure the items we need as we proceed through the course.


### 1.9 Lesson Review 
Lesson Outline

In this first lesson, we went over the big picture. Why is observability relevant? And what is your role is as an observability engineer? What tools will you need to be able to conduct observability on your cluster?

    Big Picture: Monitoring in Clusters. We introduced the big picture of what cloud observability is and how monitoring developed.
    Business Stakeholders. As a cloud observability expert, it's important to understand who the various stakeholders are that you'll be interacting with, so you can understand the sort of events you need to monitor for and how others will be using this information.
    Where to Use Observability. We also talked about the conditions under which observability can be applied, and made a distinction between monitoring your system and observing the individual events within an application.
    Prerequisites. We briefly went over the skills and concepts you should already have in order to ensure success in this course.
    Tools, Environment and Dependencies. Finally, we went over a few technical requirements, along with the software and tools you'll need to install for this course.

# 2. Observability Tools 
### 1.1 Lesson Overview 
```
Lesson Overview

In this lesson, we'll look at the main tools we need for cluster observability. We'll discuss why we need these tools conceptually and then we'll go through the process of installing them.

Lesson Outline

This lesson will get you set up with the tools you need to start doing observability in your cluster.

    Understanding your components. First, we'll look at the big picture. We'll consider three major needs that we will encounter when trying to do observability: System data, application data, and data visualization. Then we'll discuss why the three tools we're going to use—Prometheus, Jaeger, and Grafana—are great choices for addressing each of these needs.
    Installing Prometheus, Grafana, and Jaeger. Next, we'll get into the details of how to install Prometheus, Grafana, and Jaeger, and how to confirm that the installations were successful.
    Edge Case: Using ELK. Although the tools we are using in this course are excellent, industry-standard tools, it's always good to be aware of other options you may run into during your time as an observability expert. So at the end of the lesson, we will briefly consider ELK or Elasticsearch, Logstash, Kibana, which is a stack that serves as a popular alternative to the one we use in this course.
```
1.  System: Collect any event occurring on our system. 
     Use Case: Kubernetes Cluster 
	 collect all info such as: 
	 -- node health 
	 -- CPU usage 
	 --Memory usage
	 Tool we use: Prometheus
	 --Real time in nature
	 --Learning tools 
	 --data available right away 
2.  Application: Runs on the system.  
	System logs tell you the "What" not the "Why" 
	Examples: 
	--latency issues
	--500 errors 
	--execution errors
	Tool we use: Jaeger 
	Jaeger is a distributed tracing tool
3.  Just having the data doesn't mean it is useful
	Also, you don't have it obserbable until you use a tool to visualize the data 
	It must be understandable data 
	Historical Data 
	--incremental in time 
	--use to see trends 
	Tool we use: Grafana 
	--often bundled with Prometheus
	--open source 
	--visualization tool
	--popular used to build dashboards 
	--all the metrics at a glance 

Tool Context: 
* helps us transfer skills to other tools, when needed.
* Understand why we use them
* understand how to use them 
* other tool sets: 
	* ELK
	* Elasticsearch
	* Logstash
	* Kibana 

### 1.2 Big Picture: 

![tools used]()

Our Tools: 
1.  Our tool to gather system information is Prometheus 
2.  Our tool for getting information about the application is Jaeger. 
3.  And Grafana is our tool for visualizing all of this in a dashboard. 

Prometheus:
* Created by SoundCloud in 2012
* It was donated to CNCF
* Collects system information 
* Time Series Database
* Tags data in chronological order 
* prometheus comes with a querying language
* PromQL: Prometheus query language 
* it is not SQL
* it is intuitive 
* built-in alterting tools (no need for 3rd party tools)
* "not a magic bullet" 
* great for observability but not other cases 

Jaeger
* Created by Uber
* Donated to CNCF 
* Used to collect Application information 
* Distributed tracing system 
* uses the OpenTracing data model
* this is the open source standard
* OpenTracing and OpenSensus recently merged
* OpenTelemetry is the new merged tool 
* Zipkin is another popular solution 
* Zipkin is also open source 

Grafana
* Open source visualization platform
* Used to create open source dashboards 
* supports time-series databases 
* bundled with Prometheus
* customizations
* Plugins
* not part of CNCF 

CNCF
* Cloud Native Computing Foundation 
* Independent governinig body
* Oversees cloud native ecosystem 
* Industry Standard 
* Gold standard for Cloud computing 
* CNCF-Graduated Projects (can stand on their own)
* Silver members (partnered but are private companies) 
* to partner with CNCF members must follow all of the guidelines
* standardized tooling
* tested and verified  

Find the interactive partner chart of the CNCF at: [L.cncf.io](L.cncf.io)
* don't need to know all of these tools
* do need to know where to find the info when you need it 

```
Here are the key points about all three apps, for your reference:
Prometheus

    Created by SoundCloud in 2012
    Belongs to the Cloud Native Computing Foundation (CNCF)
    Collects system information (contrast this with Jaeger, which collects application information)
    Has a time-series database (you can tag with time stamp, making it easier to keep data in chronological order.
    Has its own querying language, called PromQL
    Has built-in alerting tools

Jaeger

    Created by Uber
    Belongs to CNCF
    Collects application information (contrast this with Prometheus, which collections system information)
    Provides a distributed tracing system
    Uses the OpenTracing data model, although it is transitioning to the OpenTelemetry model in future
    Zipkin is very similar and is a popular alternative

Grafana

    Visualization platform that allows you to build open source dashboards
    Supports time-series databases as a backend
    It is often bundled with Prometheus
    Expandable with plugins


```


### 1.3 Installing Prometheus and Grafana 
```
Installing Prometheus and Grafana

On this page, Jay will show you how to install Prometheus and Grafana. For now, we suggest you just watch the video to make sure you understand key points about the installation process. Then, on the next page, you'll have a chance to install it for yourself.
Get the starter code

To follow along with the demonstrations and exercises in this course, you'll need some starter files that we've provided in this GitHub repo.

You'll see that this repo contains two main directories:

    The Exercise_Starter_Files directory contains the files you'll need for the exercises (like this one) found throughout the course.
    The Project_Starter_Files directory contains the files you'll be using for the project at the end of the course.

	-- Clone or download the Repo 
	-- Gp tp tje Exercose_Starter_Files directory to find the files you'll need for all of the exercises. 
	
[YouTube](https://youtu.be/CxjoALZdfds)

Install Prometheus and Grafana:
1.  Create a Namespace
2.  Install CRDs (Custom Resource Definitions) 
3.  Install HELM repo 
4.  Update HELM repo 
5.  Install Operator 
6.  Verify installation 

Installing Helm

    Helm is a popular package manager for Kubernetes. It uses a templating language to make the managing of multiple Kubernetes items in a single application easier to package, install, and update.

Installing Helm is important as this is a common tool used for monitoring and application maintenance. If you get a job as an observability engineer, it is likely you will be asked to install and update applications with Helm. You will also be responsible for patching Prometheus, Grafana and other tools on the cluster so it is good to be familiar with the installation process.

In a real life situation, we would likely be using some kind of ingress to expose the services to the world. There are a variety of them such as Istio, [Gloo from Solo.io](https://github.com/solo-io/gloo/), [NGINX](https://kubernetes.github.io/ingress-nginx/), [Contour](https://projectcontour.io/) and many others. Different companies and different teams use different solutions.

For the purposes of this course, we will be using kubectl port-forward. This is a simple way to forward a Kubernetes service's port to a local port on your machine. This is something you would never do in production but would regularly do in testing.

An example would be if you ran this command:

kubectl port-forward service/my-service 7000:80

Here you are forwarding the Kubernetes service called my-service and using local port 7000, forwarding it to service port 80.

For this course, you can simply follow our commands—but we encourage you to check out more details on best practices in the [Kubernetes documentation here](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/).

Note:
When installing via the Prometheus Helm chart, the default Grafana credentials are:

username: admin 
password: prom-operator

whereas the Grafana documentation states (admin:admin).
Additional Resources

If you would like to learn more about Prometheus and why it is the standard, you can check out [CNCF's website here](https://landscape.cncf.io/selected=prometheus).

```



### 1.4 Exercise: installing Prometheus 

Resume Studies here: https://classroom.udacity.com/nanodegrees/nd064/parts/5265ce05-4867-47b9-9a82-e3965e033555/modules/ef26b73a-22fa-46ed-913c-2a6f0347319c/lessons/e1eb6512-0e09-44dc-88c5-3bc36266b43f/concepts/51a56033-feb4-4d2c-8151-ae1ba40dd8c2 

### 1.5 Installing Jaeger
### 1.6 Exercise: Installing Jaeger 
### 1.7 Using ELK
### 1.8 Lesson Review 




