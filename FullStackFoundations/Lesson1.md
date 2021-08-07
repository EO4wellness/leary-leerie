# Lesson 1: Working with the CRUD 
* Learn about CRUD
* Create Read Update and Delete 
* Implement CRUD operations on a database 
* Use ORM as an alternative to SQL 
* Object-Relational-Mapping 

## 1.1 Course Intro: 
* course instructor: Lorenzo
* This course teaches students to build their own data-driven web application.  
* What is meant by web application? 
* A web application is a web page (or collection of pages) which allows a browser to respond to user input. 
* A web application is similar to an off line piece of software. 
* A web application provides an interactive user experience. 
* What is meant by data-driven? 
* Data-driven is an application which can store and/or retrieve information from a database.
* This is used in delivering customized-content to the user. 
* Most common websites are data-driven web applications 
* Use python to build an interactive web application 
* extract data from a database using python 
* Learn to use a tool called ORM 
* ORM:  Object-Relational Mapping 
* ORM is used to manipulate queries as objects in Python 

## 1.2 Prerequisites and Preparation
### Resources for Pre-Requisites and Preparation
* Udacity offers additional courses that cover the pre-requisites to this course:
* [Object-Oriented Python](https://www.udacity.com/course/ud036)
* [SQL](https://www.udacity.com/course/ud197)
* [HTML & CSS](https://mena.udacity.com/course/intro-to-html-and-css--ud304)

For Python, you should be comfortable:
- Creating Classes
- Writing Methods
- Understand Inheritences 

SQL: 
- Insert Into 
- Select 
- Update 
- Delete 

Install: 
- [Git](https://git-scm.com/downloads)
- [Configure Git](https://www.udacity.com/course/how-to-use-git-and-github--ud775)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it. The version of VirtualBox you should install is 5.1. Newer versions are not yet compatible with Vagrant.
- [Vagrant](the version of VirtualBox you should install is 5.1. Newer versions are not yet compatible with Vagrant.)
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Fetch the Source Code and VM Configuration
Windows: Use the Git Bash program (installed with Git) to get a Unix-style terminal.
Fork the starter repo

Log into your personal Github account, and fork the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) so that you have a personal repo you can push to for backup. Later, you'll be able to use this repo for submitting your projects for review as well.
Clone the remote to your local machine

From the terminal, run the following command (be sure to replace <username> with your GitHub username): git clone http://github.com/<username>/fullstack-nanodegree-vm fullstack

This will give you a directory named fullstack that is a clone of your remote fullstack-nanodegree-vm repository.
Run the virtual machine!

Using the terminal, change directory using the command cd fullstack/vagrant, then type vagrant up to launch your virtual machine.

Once it is up and running, type vagrant ssh. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.

Now that you have Vagrant up and running type vagrant ssh to log into your virtual machine (VM). Change directory to the /vagrant directory by typing cd /vagrant. This will take you to the shared folder between your virtual machine and host machine.
Sharing files between the vagrant virtual machine and your home machine.

Be sure to change to the /vagrant directory by typing cd /vagrant before creating new files or pasting files that you want to be shared between your host machine and the VM. 

CD: \GitHub\leary-leerie\FullStackFoundations

1.3 Project Introduction-CRUD 

1.4 CRUD Quiz 1 Browsing articles in an online newspaper uses READ of CRUD. 
1.5 CRUD Quiz 2 Clearing out your junk mail is a DELETE on a database. 
1.6 CRUD Quiz 3 Making a new profile on a blog is a CREATE of CRUD. 
1.7 CRUD Quiz 4 Changing the number of items in your online shopping cart is an UPDATE of CRUD. 

1.8 SQL 
web application code uses SQL to reach the data base and return the results back into the application 

1.9 SQL Quiz 
There is nearly a 1-to-1 coorespondence between SQL and CRUD. 
for these SQL Quizes match up the displayed SQL command with the correct corresponding CRUD operation it executes. 

SELECT - Read 

1.10 SQL Insert Into 
INSERT INTO - Create 

1.11 SQL Update 
UPDATE - Update 

1.12 SQL Delete 
DELETE - Delete 

1.13 Creating a Database and ORMs 
* When Building a resturant menu web application we have some basics to consider of what is in common between all resturant menus. 
* All menus have menu items.  
- Appetitizer(s)
- Entree(s)
- Dessert(s)
- Beverage(s) 
* List of Different Resturants for which each menu or menu item is associated 
* Price and Description of each Menu Item 
* Early design decision: How to model the database.  
* This desicion is important to the overall function. 
* There is likely more than one way to model the DB. 
* Don't make things over complicated. 

Database Layout Process: 
- restaurantmenu.db 
- Resturant table (representing ALL of the resturants in our DB) 
  includes: 1) corresponding name 
            2) id 
- Menu Item table 
  1) Name 
  2) ID
  3) Description 
  4) Price 
  5) Course (categorizes if the item is a beverage, entree, dessert, or appetizer) 
  6) Resturant ID 


![Chart-L1.13-db-design](#)

Creating our Database 
RAW SQL 

```
import sqlite3
conn = sqlite3.connect('restaurantmenu.db')

c = conn.cursor()
c.exectue('''
	  CREATE TABLE restaurant 
	  (id INTEGER PRIMARY KEY ASC, name varchar(250), price varchar(250),
           description varchar(250) NOT NULL, restaurant_id INTEGER NOT NULL, 
	  ''')

conn.commit()
conn.close()
```

* There is nothing wrong with the above Raw SQL code.  
* However when using Raw SQL queries have to be sent to the database as strings. 
* This works. 
* However the python compiler cannot help if we make a typo, reference a table which doesn't exist, etc. 
* Every other data structure used in python is some type of object. 
* Why not treat our DB quiries, tables, and rows as objects too? 
* Because this concern isn't unique, but common, devlopers created a tool called ORM
* ORM stands for Object-Relational Mapping 
* ORMs works like a translator
* ORMs convert our code from one form to another 

![ORM-two-way-translator](#)

1. We have python code. 
2. We use python code to send a query to the DB. 
3. The ORM translates Python to SQL
4. The DB returns results.
5. The ORM translate the DB results into Python
6. The ORM returns Python to the web application.  

1.14 Introducing SQLAlchemy 
One type of ORM is [SQLAlchemy](http://www.sqlalchemy.org/)
Note: Vagrant already has SQLAlchemy installed. 

1.15 [Creating a Database - Configuration](https://classroom.udacity.com/courses/ud088/lessons/3621198668/concepts/36123887280923)
* Creating a DB with SQL Alchemy 
* database_setup.py 


1.16 Creating a Database - Class 

1.17 Creating a Database - Mapper 

1.18 Putting it all Together 

1.19 Quiz

1.20 Quiz 

1.21 CRUD Create 