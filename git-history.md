# Version Control Course notes - Lesson 3 - Repo History 
in the previous lessons of this course we've already studied

          Version Control
          * [Overview: Git](https://github.com/EO4wellness/leary-leerie/blob/master/version-control-course-notes.md)
          * [Lesson 1: Installation](https://github.com/EO4wellness/leary-leerie/blob/master/git-install-notes.md)
          * [Lesson 2: Git Init, Git Clone, Git Status](https://github.com/EO4wellness/leary-leerie/blob/master/git-repo.md)
          * Lesson 3: Git History (current study session; outlined below)
          
## Intro to Lesson 3 
The course instructor shares his experience, as a child, of his parents wanting him to keep a daily journal.  As all of us who have had that experience, before coming adults, know a journal is useless if it doesn't have certain details recorded within it.  This is similar to our Git Repos.  If we write in the history of our repositories haphazardly, we likely won't remember much or get much context out of it.  Any communication, even if it is totally awesome in the communicator's skill in crafting the message, can fail if it is out of context!  It is very likely to get misunderstood.  Just like a good journal entry should have the date, an informative title, and appropriate content, so too we must take some (minimal) effort to make the repo history and commits meaningful tomorrow, next week, next month, next year, next decade.

                    Git Commits:
                    * function like a journal entry. it tells us similar information: the date, details, etc. 
                    * commits should be descriptive. 
                    * likewise git commits should be frequent 
                    * make frequent commits with descriptive messages (something to work on achieving consistently) 
                    * this makes it easier to look back at any/all projects and see how they have evolved 
                    
                    Commands Used in This Lesson:
                    git log   |    Displays info about the existing commits.   
                    git show  |    Displays info about the given commit. 
                    
The best way to learn proper formating and style, as well as usefulness of Git Commit History is to read other peeps active repos. 

## Displaying a Repository's Commits 
* Begin by ensuring the "git clone" command we used in Lesson 2 of this course has sucessfully installed the cloned blog project, as we will be using it in this lesson. If you don't have it, open your terminal, and type the command: 
                    
                    $ git clone https://github.com/udacity/course-git-blog-project 
     
                    now use cd to navigate inside this cloned repo
                    use pwd to be certain you are in the (newly cloned if you followed the above instruction) or previosuly created (if you are returning here from having followed the instructions in lesson 2) blog-project repo 
                    
                    You should always run the 'git status' command (once you have navigated to the blog project repo. 
                    This is especially true when you are returning to a project after a period of time.
                    
                    The 'git status' command should let us know there is "nothing to commit, working directory clean." 
                    If we see this, then we are ready to start learning and check out the project. 
                    
                    Open a code editor and take a look at the project before moving on. There are CSS, JavaScript and HTML files. 
                    Step along and answer the quiz questions based on what you are seeing (I took the quiz for lesson 3 and passed 100%. 
                    
                    Type the command 'git log' and see what displays. 
                    Use the display to answer questions and follow the rest of the lesson discussions. 

                    
* Took the quiz for lesson 3 - passed 100%   This is a look at some of my input/output for this lesson

                    User MINGW64 ~
                    $ pwd
                    /c/Users/
                    
                    User MINGW64 ~
                    $ cd ~/course-git-blog-project

                    User MINGW64 ~/course-git-blog-project (master)
                    $ pwd
                    /c/Users/course-git-blog-project
                    
                    User MINGW64 ~/course-git-blog-project (master)
                    $ git status
                    On branch master
                    Your branch is up to date with 'origin/master'.
                    
                    nothing to commit, working tree clean
                    
                    User MINGW64 ~/course-git-blog-project (master)
                    $ git log
                    commit a3dc99a197c66ccb87e3f4905502a6c6eddd15b1 (HEAD -> master, origin/master, origin/HEAD)
                    Author: Richard Kalehoff <richardkalehoff@gmail.com>
                    Date:   Mon Dec 5 16:34:15 2016 -0500
                    Center content on page
                    
                    commit 6f04ddd1fb41934c52e290bc937e45f9cd5949aa
                    Author: Richard Kalehoff <richardkalehoff@gmail.com>
                    Date:   Mon Dec 5 16:30:40 2016 -0500
                    Add breakpoint for large-sized screens
                    
                    commit 50d835d7b53f46deb1365fe7598e0ea7011dbc3e
                    Author: Richard Kalehoff <richardkalehoff@gmail.com>
                    Date:   Mon Dec 5 10:39:19 2016 -0500
                    Add breakpoint for medium-sized screens
                    
                    commit 0768f3dc08a4cb849119cb7388ed2b73018e4851
                    Author: Richard Kalehoff <richardkalehoff@gmail.com>
                    Date:   Mon Dec 5 10:25:22 2016 -0500
                    
                    . . . 
                    


## Navigating The Log

If you're not used to a pager on the command line, navigating in Less can be a bit odd. Here are some helpful keys:

    to scroll down, press
        j or ↓ to move down one line at a time
        d to move by half the page screen
        f to move by a whole page screen
    to scroll up, press
        k or ↑ to move _up_ one line at a time
        u to move by half the page screen
        b to move by a whole page screen
    press q to quit out of the log (returns to the regular command prompt)

## Review of Git Log Command 
* The "git log" command is used to display all of the commits of a specific repository.  
* Use CD to navigate to the repository you want the information for, before, running the "git log" command.  You can then use PWD to validate you are looking inside the correct directory before running the "git log" command. 
* _By default_ the "git log" command displays: 1) the SHA, 2) the author 3) the date 4) the commit message. 
* besides the default info displayed, it can display a whole lot more. 
* Git uses "command line page, Less" to page thru all of the information the log contains. 
* Review the "important keys" of the command line page less to learn how to navigate the log. These include:

                      
                       to scroll down by a line, use j or ↓
                       to scroll up by a line, use k or ↑
                       to scroll down by a page, use the spacebar or the Page Down button
                       to scroll up by a page, use b or the Page Up button
                       to quit, use q
        

* Move on to discover more...


## Changing How Git Log Displays Information 

## Viewing Modified Files 

## Viewing File Changes 

## Viewing A Specific Commit 

##  Lesson 3 Summary 

## Study session notes.
* 2020-12-25 Created notes outline and linked to it. 
