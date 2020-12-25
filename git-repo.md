# Version Control Course
Review of terms and concepts learned in lesson #1: Installing Git.<br>
<br>
## Lesson 2
Now that Git is installed, configured, and ready to work with we will be learning 3 things you can do with your newly installed Git comand line prompt. <br>
1.  Repo.  Repo is short for repository.  You cannot work with Git if you don't have a repo (repository) to work with.  "Repo" is short for Repository and therefore they can be used interchangably.
2.  Clone. <br>
3.  Satus. <br>

## Commands Used in this lesson 
* git init<br>
* git clone <br>
* git status <br>

## Git Init 
* Is a command to create brand-new repositories on your computer. <br>
* Before you can make a committ or do anytihng else, you need to have a place to work.  That place is called a repo, or repository.<br>
* The "init" part of this command stands for initialize.  
        
        ls - used to list files and directories
        mkdir - used to create a new directory
        cd - used to change directories
        rm - used to remove files and directories
        pwd - used to print working directory and rediscover where you are at if you get lost as to which directory you are in, currently. 
        
* It is recommended to make a specific repo for this course work and use the GIT commands to do so.

        create a directory called udacity-git-course
        inside that, create another directory called new-git-project
        use the cd command to move into the new-git-project directory
        
        SOLUTION: 
        1. Open a terminal window (if you don't already have one open)
        2. use the 'cd' command to change the directory within the terminal to point at the correct location
        3. If you aren't certain about which directory you are in, type the 'pwd' command (Print Working directory) to view the current directory. 
        4.  Finally at the $ prompt type "mkdir -p udacity-git-course/new-git-project && cd $_" which will prepare the space.  NOTE: You can verify it before continuing by examing the files on your computer.  You can view the files which were created, but do not delte anything. 
        5.  Finally type the "git init" command to create the repo.   
        6. Verify this occurred by looking at the terminal prompt.  It should now include "Master" in the text about the current directory. 

## (dot)git directory or ".git"
What are the items in the .git directory? Here is a brief list and description:
                * config file - these are the configuration settings for this specific project repository you are using (.git/config)
                * description file - this file is only used by the GitWeb program. 
                * hooks directory - this directory would host client-side or host-side scrips we may want to run. 
                * info directory - gobal excludes file 
                * objects directory - stores all of the commits we make
                * refs directory - holds pointers to cmmits (basically "branches" and "tags")
                * [Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain) 
                * [Custom Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
 
### Git Init Summary 
Use the "git init" commmand to create a new, empty repository in the current directory.
Further info Links:  [Initializing a Repository in an Existing Directory](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#Initializing-a-Repository-in-an-Existing-Directory), [Git Init Docs](https://git-scm.com/docs/git-init), [Git Init Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository),

## Git Clone 
Is a command which will exactly copy files from somewhere else to your computer. The "Clone" command, makes an exact copy.  <br>

###  WHY CLONE?
Example--Well, when I work on a new web project, I do the same set of steps:

    create an index.html file
    create a js directory
    create a css directory
    create an img directory
    create app.css in the css directory
    create app.js in the js directory
    add starter HTML code in index.html
    add configuration files for linting (validating code syntax)
        HTML linting
        CSS linting
        JavaScript linting
    configure my code editor

Clone can help with "template" like scenarios, and more. 

Cloning is accoplished by using the "git clone" command.

Prereqs to clone: 
1. be certain you are located in the correct directory on the command line. 
2. be in a clean directory. 
3. you cannot have nested Git repos. 
4.  recall to use "pwd" (print the working directory) and "cd" change drives when and as needed 

ASSIGNMENT: 
Use the following command in your Git with the proper current working directory
"$ git clone https://github.com/udacity/course-git-blog-project"
This will clone the contents of the above URL into your empty repository.

                        Solution: this creates a new directory named "course-git-blog-project" inside your current directory and clones the exact content of this URL's location to your device. 

ASSIGNMENT: 
What if you wanted to rename the file, instead of using the exact clone-copy of the original file name?  How would you accomplish this? 
                
                Solution: There isn't enough information in the course lesson to gather this information on your own (unless you're not a git beginner and already know.  Instead, you need to take the initiative and go read the user documentation the course gave us in the previous lesson, in order to read and study it, looking for the correfct command and syntax to make this work.  "git clone https://github.com/udacity/course-git-blog-project blog-project" will accomplish what's needed to rename the file "blog-project" 
                
## Warning
* Beginners often overlook the current working directory and this can mess them up as it will clone inside an existing folder.  That's not going to work.  Experience teaches us--but let's avoid the problem and be certain we are in the proper working directory before cloning to avoid issue. 
* If you are in a git repository, the name of the repo will display in parentheses. 
* Use PWD to test, if you aren't certain, which directory you are in and CD to change the directory as needed. 

### Git Clone 
* A summary of the main points:
* The proper formating for Git Clone is "$ git clone <path-to-repository-to-clone>"
* The "git clone" command take the path to an existing repo.
* By default will create a directory with the same name as the repository that's being cloned.
* can be given a second argument that will be used as the name of the directory
* will create a new repo inside the currrent working directory
        
## Helpful Links
[Cloning an Existing Repp](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#Cloning-an-Existing-Repository)
[git clone docs](https://git-scm.com/docs/git-clone)
[git clone tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
[zip file] havedn't uploaded this file yet to "link" to it. 

## Git Status 
Is a command you can use to check the status of a repo and during this lesson we learn the importance of knowing the status, as well as the importance of checking the status.

In our coursework, we've used the previous commands we've learned to 1) Create an empty repo with the "git init" command. and 2) clone a second repository via the "git clone" command. If we want information about waht Git knows about your two repos, we need to learn and use the "git status" command.  This function is EXTREMELY important and should be practiced/learned. 

# Digging Deeper 
* The [Udacity Shell Workshop](https://www.udacity.com/course/shell-workshop--ud206) is available if you need more help, or a refresher on how to use command level. 

2020-12-15 [left off this course at](https://classroom.udacity.com/courses/ud123/lessons/437a88fc-15f5-48b8-a6a5-0cf3347e6183/concepts/fa8f761a-d0a2-4be1-a5b9-60116ea4ecd1)resume here next study session

2020-12-25 Reuming studies thru and until I left off with [Lesson 2.4 Determine a Repos Status](https://classroom.udacity.com/courses/ud123/lessons/437a88fc-15f5-48b8-a6a5-0cf3347e6183/concepts/ce648229-7d6c-4ad3-805e-af6a77f38fd0)
