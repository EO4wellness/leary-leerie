# TechTrends Project Description 
- This project is an online website used as a news-sharing platform. 
- Website visitors access the latest news within cloud-native ecosystem. 
- Facilitates reading and sharing news articles and creating new media content too. 
- Additionally, this project is my personal work & submission for the Udacity SUSE Scholarship Phase 2 
  [Cloud Native Application Architecture NanoDegree](https://www.udacity.com/course/cloud-native-application-architecture-nanodegree--nd064) program.

## Project Involvement: 
* Design team composed of: 
  - 2 Developers (Developed web application using Python Flask and SQLite)
  - 1 Platform Engineer (my role in this project)
  - 1 Project manager 
  - 1 Manager 

## Project Goal: 
Build an effective, functional, online news sharing platform. 

## Project Status: 
* This project was originally froked from [Udacity Course Repository](https://github.com/udacity/nd064_course_1/tree/main/project)
* This project contributes to earning the Udacity [Cloud Native](https://www.udacity.com/course/cloud-native-application-architecture-nanodegree--nd064) Nanodegree program. 
* This project is the first prototype of the TechTrends website. 
* This project is also the first project in the Udacity Cloud Native ND program.  

## Project Table of Contents 
* this project is entirely contained within this [zip file](*)
* below is a list of files this project contains and the purpose of each file type: 


    - README.md contains the main steps of how to execute the TechTrends application
    - __init__.py is a reserved method used to indicate that a directory is a Python package
    - app.py contains the main logging of the TechTrends application
    - init_db.py is a file that is used to initialize the posts database with a set of articles
    - requirements.txt contains a list of packages that need to be installed before running the TechTrends application
    - schema.sql outlines the posts database schema
    - static/ folder contains the CSS files. subfile include: css and main.css 
    - templates/ folder outlines the HTML structure of the TechTrends application
    - argocd - a folder that contains the ArgoCD manifests
    - helm -  a folder that contains the Helm chart files
    - kubernetes - the folder that contains Kubernetes declarative manifests
    - screenshots - the folder that contains all the screenshots
    - techtrends - overarching project file 
    - docker_commands - the file used to record any used Docker commands and outputs
    - Dockerfile - the file that contains the instructions to package the application
 [?]   - .github - folder containing the configuration for GitHub Actions workflows
 
 ## Steps to Run Application: 
 1. Initialize the database using ```python init_db.py```
 2. Doing step 1 creates (and/or overwrites if the file already existed) the ```database.db``` file.
    Note: the database.db file is used to store and access the available news posts. 
 3. Run the TechTrends application by using the ```python app.py``` command. 
 4. The application is running on port ```3111```
 5. You can access the application by querying the ```http://127.0.0.1:3111/``` endpoint.

## Dependencies: 
* Python [Documentation](https://www.python.org/downloads/)
* Git [Documentation](https://git-scm.com/downloads) 
* Docker [Documentation](https://docs.docker.com/get-docker/)
* Vagrrant [Documentation](https://www.vagrantup.com/downloads)
* VirtualBox (version 6.1.16 or higher) [Documentation](https://www.virtualbox.org/wiki/Downloads)


