# [Lesson 4- Open Source PaaS](https://classroom.udacity.com/nanodegrees/nd064-1/parts/30cb07da-8fd4-4438-a209-b3457adb5d82/modules/7b21dfa4-aac8-4d24-82c5-65325e6dc691/lessons/cda0124d-cb33-48d8-9f47-abc73e627243/concepts/9f7137fa-31c1-45b9-83a6-8d67014aeb2f)
* Beginning study of lesson 4: 2021-06-20
* PaaS - Platform as a Service 

## 4.1 Introduction 
* PaaS Mechanisms 
* Cloud Foundry 
* Function as a Service (FaaS)

## 4.2 Cluster Management 
* Kubernetes Functionalities/Capabilities
```
Automation
Portability 
Extensibility 
Flexibility
Self-Healing
More...
```
* Managing at scale is challenging. 
* Management is especially a hassle when it is self-hosts or in private clouds. 
* Requires a lot of engeineering effort. 
* cluster management: 
```
Sandbox 
Staging 
Production 
```
* Run in different regions 
* Market Proximity
* Distribute this in: US, Europe, Asia. 
* this market proximity helps with speed of deliverability 
* Need your own infrastruction and capability or delegate this to a PaaS solution 

## 4.3 PaaS Mechanisms 
* PaaS: Cloud computing mechanism application management is delegated to a 3rd party.
* Functionality PaaS provides: 
* Application Management Mechanisms include:
```
On Prem - full control over platform and responsiblity for maintenance of everything. 
IaaS - team consumes computer, network and storage services from a vendor who manages the hardware.
Paas - team focuses on application only, the infrastructure is fully managed by a provider. 
```
* Platform: 
```
Networking layer 
Storage 
Servers
Virtualization
O/S
Middleware
RunTime
Data
Applications 
```
* Networking: communication between internal and external systems
* Networking examples: internet connection, firewall, routers, cables 
* Storage: collect and store digital data
* Stoarge examples: files, blocks, objects 
* Servers: The physical machines which provide compuete services for a platform
* Virtualization: Abstracts physical servers, storage, and networking 
* Virtualization examples: hypervisors virtual servers 
* O/S operating system
* the OS connects the software to the physical serouses 
* OS examples include Linux Ubuntu windows etc 
* Middleware: developers build an application
* Middleware makes it easy to consume platform capabiilities
* Middleware examples include messaging API data management 
* Runtime: execution context for an application
* Runtime examples: using JVM as a Java runtime 
* JVM: Java Virtual Machine 
* Data: tools for collection and storage of data which is required by the application during its execution
* Data Tool Examples: MySQL, MongoDB, CockroachDB
* Applications the business logic for a product 
On-premise

On-premise represents a cloud-computing offering where the engineering team has full control of the platform services (from networking to applications). This solution is suitable for organizations that have sufficient engineering power and regulations that demand full control of their technology stack and operations within it.
IaaS

IaaS solutions provide the abstraction of networking, storage, server, and virtualization layers. As a result, these services are consumed on-demand by the engineering teams. Additionally, IaaS provides a suitable abstraction for the management of self-hosted Kubernetes clusters, which depend on compute, network, and storage components for a successful bootstrap process.

The most common IaaS solutions are delivered by public cloud providers such as AWS, GCP, Microsoft Azure, and many more.
PaaS

PaaS is a cloud-computing offering that enables an engineering team to fully focus on application development. It abstracts all services except the application and the data associated with it. As a result, the team is required to manage the code base and any database service that the product needs to be fully operational.

Popular PaaS solutions are App Engine from GCP, Heroku, Cloud Foundry, Beanstalk from AWS, and many more. 

Advantages:
- Time Efficiency 
- Engineering focus towards development rather than infrastructure management 
- Scalability 
- High availability
- on demand resource consumption
- applications easily scale
- fail over 
- rich applicatio catalog
- integration of external services (db) with minimal effort 

Disadvantages:
- Vendor Lockin 
- Interchange PaaS providers without service distruption 
- Data security
- managed by 3rd party makes secuirty more complex 
- hard to ensure data confidentiality 
- Operationals limitations 
- service catalog is limited to services offered by the integraded cloud provider 

Who manages what?  for OnPrem | IaaS | PaaS
- Applications  you|you|you
- Data          you|you|you
- Runtime       you|you|service provider (SP) 
- Middleware    you|you|sp
- O/S           you|you|sp
- Virtualization you|SP|SP
- Servers       you|SP|SP
- Storage       you|SP|SP
- Networking    you|SP|SP


    The fewer components are delegated to external providers, the more control there is over available functionalities
    The more ownership there is across the stack, the more complexity is introduced in managing and delivering the product
    The fewer components are managed by an engineering team, the quicker is the usability of the stack. As such, with a PaaS offering the engineering team can deploy their application immediately. While if choosing an on-premise solution, the release of a product is possible only after the platform is built.

There is a trade off....the more control and complexity vs. quicker usability for each cloud computing type offered 
New terms

    On-premise - cloud-computing service, where a team owns the entire technology stack.
    IaaS - cloud-computing service that offers the abstraction of networking, storage, server, and virtualization layers.
    PaaS - cloud-computing service, where the infrastructure components are managed fully by a 3rd party provider, and a team manages only the application and the data associated with it.

Further Reading

Read more about on-premise, IaaS, and PaaS solutions:

 [On Premise Vs Cloud](https://www.ebcgroup.co.uk/news-insights/on-premises-vs-cloud)
 [Infrastructure as a Service](https://susedefines.suse.com/definition/infrastructure-as-a-service/)
 [Platform as a Service](https://susedefines.suse.com/definition/platform-as-a-service/)
 [Cloud Computing in 2021: What You Should Know about Public, Private, Hybrid, PaaS, SaaS and FaaS](https://www.suse.com/c/cloud-computing-in-2021-what-you-should-know-about-public-private-hybrid-paas-saas-and-faas/)



## 4.4 Quizzes: PaaS Mechanisms 


1. What services do you have to manage if you are using an on-prem solution? 
My answer:  servers, networking, application, middleware (of the available choices)

2. What services do you have to manage if you are using IaaS solution? 
Choices: Servers, middleware, data, applications.  
My answer:  middleware, data, applications

3. What services do you have to manage if you are using a PaaS solution? 
choces: storage, application, data, os
My answer: application, data 

4. Which of the following cloud-computer offerings provide the most of the infastructure services? 
choices: on-prem, iaas, paas
My answer: On-Prem 

5. Which of the following cloud-computing offerings provide quicker usability of intrastructure services: 
choices: on-prem, iaas, paas
My answer: PaaS

6. Which of the following cloud-computing offerings provides a suitable abstraction level for a team to build and run their own Kubernetes clusters?
choices: on-prem, iaas, paas
My answer: IaaS



## 4.5 Exercise: PaaS Mechanisms 
scenario: small team web-store application 
Describe what PaaS functionalities will be explicitly beneficial for this project and why
One of the main advantages of choosing PaaS is the easy integration with available services from a provider.


## 4.6 Solution: PaaS Mechanisms
As such, the web-store project will benefit from the following PaaS capabilities:

    database - for storing the customer details, orders, and products details
    compute - accessible scalability for the application to serve millions of customers
    networking - hosting and serving the requests with no downtime
    analytics - an add-on to collect data and provide metrics and logs about customer interaction with the web-store



## 4.7 Cloud Foundry 
Cloud Foundry consists of multiple components that provide these core capabilities:

    Routing - handle the incoming external traffic and route it to applications
    Authentication - identity management to user accounts
    Application lifecycle - controls the application deployments, monitors their status, and reconciles any new changes to reach the desired state of the application.
    Application storage and execution - handle the availability of artifacts to applications
    Service - use service brokers to provisions on-demand the dependency services for an application, such as a database or third-party APIs
    Messaging - ensure the communication between Cloud Foundry components
    Metrics and logging - aggregates the system and application metrics and logs

In the following sections, we will explore Cloud Foundry using [SUSE Cloud Application Platform Developer Sandbox](https://developer.suse.com/capsandbox/). However, you can explore Cloud Foundry's functionalities using the following offerings as well:

[IBM Cloud Foundry](https://www.ibm.com/cloud/cloud-foundry)
[SAP Cloud Platform](https://www.sap.com/products/cloud-platform/get-started.html)
[Anynines](https://paas.anynines.com/)


    Marketplace and Services - research the service catalog and explore any integrated services
    Organizations - used to manage multi-tenancy, quotas, and access to applications
    Routes - list all available endpoints used to access deployed applications
    Build Packs - explore available buildpacks packages used to build an application
    Security groups - configure the endpoints that the application can communicate with

Further Reading
Explore Cloud Foundry and the Stratos Console in more detail:

[Cloud Foundry Overview](https://docs.cloudfoundry.org/concepts/overview.html)
[Introduction to Stratos](https://gettingstarted.cap.explore.suse.dev/stratos/)
[Cloud Foundry: Deploying with App Manifests](https://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html)
[Moving a Cloud Foundry Hello World App to Kubernetes - how hard can it be?](https://www.suse.com/c/moving-a-cloud-foundry-hello-world-app-to-kubernetes-src/)


## 4.8 Quizzes: Cloud Foundry 
1. Why an engineering team can avoid vendor lock-in by using Cloud Foundry? 
Answer: Cloud Foundry is an open-source PaaS, Cloud foundry can be deployed on top of existing cloud providers 

2. Cloud Foundry offers services as part of its core functionalities. It will use service brokers to provision on-demand the dependency services for an application. What kind of dependency services does it cover?
Answer: 3rd party APIs, databases 

3. Which of the following sources you can use to deploy an application using Cloud Foundry?
My Answer: Public GitHub repo, Docker image, Public GitLab repo, Upload source code directly 

4. True or False: Cloud Foundry provides routing to applications from external users.
My Answer: True 


## 4.9 Exercise: Cloud Foundry 
Imagine the following scenario: you are part of the team that needs to assess the benefits and drawbacks of using Cloud Foundry versus Kubernetes.

Considering that the application code is available, reflect on what operations and steps are necessary to adopt each solution (Cloud Foundry and Kubernetes) for a successful application deployment. What are the main drawbacks of each solution?
What are the steps to adopt Kubernetes for a successful application deployment?
Reflect on Cloud Foundry versus Kubernetes adoption -What are the steps to adopt Cloud Foundry for a successful application deployment?
Reflect on Cloud Foundry versus Kubernetes adoption -What are the main drawbacks of each solution?

Pivotal [Cloud Foundry vs Kubernetes](https://www.overops.com/blog/pivotal-cloud-foundry-vs-kubernetes-choosing-the-right-cloud-native-application-deployment-platform/): Choosing The Right Cloud-Native Application Deployment Platform
Cloud Foundry vs Kubernetes [Which One Should you Choose](https://softwarehut.com/blog/tech/cloud-foundry-vs-kubernetes)
Cloud Foundry vs. Kubernetes: [Which is Best for Your Needs](https://medium.com/@odedia/comparing-kubernetes-to-pivotal-cloud-foundry-a-developers-perspective-6d40a911f257)?
CF vs K8s
[Game of cloud technologies](https://developer.ibm.com/technologies/containers/blogs/game-of-cloud-technologies-kubernetes-vs-cloud-foundry/): Kubernetes vs. Cloud Foundry



## 4.10 Solution: Cloud Foundry 
Solution: Cloud Foundry

It is pivotal to understand the application functionalities and available resources. This is especially the case when a microservice-based design is chosen, and solutions suck as IaaS (Infrastructure as a Service), PaaS (Platform as a Service), SaaS (Software as a Service) are available from a multitude of vendors. Choosing the most suitable deployment tooling will lead to the efficient delivery of the product.

Considering that the application code is available, these are the steps to adopt each proposed solution:

    Kubernetes
        create an OCI (Open Container Initiative) compliant image, usually created by using Docker
        deploy a Kubernetes cluster with a valid ingress controller for the routing of requests
        deploy an observability stack, including logs and metrics
        create the YAML manifests for the application deployment
        create a CI/CD pipeline to push the Kubernetes resources to the cluster

    Cloud Foundry
        write a manifest file to provide main application deployment parameters
        deploy Cloud Foundry or use Cloud Foundry PaaS solutions from 3rd part vendors
        deploy the application to Cloud Foundry (via CLI or UI)
        Note: Cloud Foundry will create the OCI compliant image by default, and it will provide the routing capacities as well.

Cloud Foundry provides a better developer experience for application deployment, as it offers a greater level of component abstraction (no need to manage the underlying infrastructure). However, a PaaS solution locks-in the customer to a specific vendor. On the other side, Kubernetes offers full control over the container orchestration, providing more flexible management of the application.


## 4.11 Edge Case: Function as a Service  
New Terms
FaaS or Function as a Service - event-driven cloud-computing service that requires only the application code to execute successfully.

Further Reading
Explore FaaS in more detail:
[What is Function-as-a-Service (FaaS)?](https://www.redhat.com/en/topics/cloud-native-apps/what-is-faas?source=searchresultlisting)



## 4.12 Exercise: Function as a Service  
Imagine the following scenario: you are working for a media (newspaper) company and was assigned to develop a microservice responsible for the life-cycle of customer accounts. The principal operations include account creation and deletion.

Considering the above, reflect on what mechanisms you would choose to deploy the microservice, PaaS, or FaaS. Elaborate on your reasoning. 
What mechanism would you choose to deploy the customer account management microservice? Explain your reasoning. 

https://www.americanpressinstitute.org/publications/reports/survey-research/newspaper-vs-other-subscribers/
https://www.americanpressinstitute.org/publications/reports/survey-research/news-subscriber-types/

## 4.13 Solution: Function as a Service 
For this particular exercise, choosing either a PaaS or FaaS would reach the end goal: making the service available to customers.

In most cases, in a newspaper context, the readers are more focused on the news content rather than managing their accounts. Also, the number of requests to get an article can be a thousandfold higher than the number of requests to create or delete an account. As such, you can assume that the microservice should not be running at all times consuming available resources, and instead invoke it on demand-only.

Conclusively, a FaaS solution would be more suitable for the management of customer account microservice.


## 4.14 Lesson Conclusion  
Overall, throughout this lesson we explored:

    PaaS Mechanisms
    Cloud Foundry
    Function as a Service

Glossary

    On-premise - cloud-computing service, where a team owns the entire technology stack.
    IaaS or Infrastructure as a Service - cloud-computing service that offers the abstraction of networking, storage, server, and virtualization layers.
    PaaS or Platform as a Service - cloud-computing service, where the infrastructure components are managed fully by a 3rd party provider, and a team manages only the application and the data associated with it.
    Cloud Foundry - an open-source PaaS offering, that can be hosted on any available infrastructure
    FaaS or Function as a Service - event-driven cloud-computing service that requires only the application code to execute successfully.


