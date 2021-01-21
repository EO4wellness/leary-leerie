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
Look at the output from runnnig the "git log" command in your terminal. 
                    
                    the SHA - git log displays the complete SHA for every commit. Each SHA is unique (so we don't need to see the entire SHA). Usually we can see the distinctions just by viewing the first 6-8 characters of each SHA. 
                    the author - git log displays the commit author for each commit. 
                    the date - git log displays the date for each commit. While this may become important, it generally isn't necessary to know it on a day-to-day basis when all things are progressing normally. 
                    the commit message - one of the most important parts of a commit. when looking at a log, generally speaking, this is the reason we are looking.  we want to know this information. 
                    
                    use a flag to narrow the log to the things which are important to view. NOTE: a flag is used to alter the way a program functions. 
                    ls will list all of the files in the current directory
                    ls command has a - l flag
                    recommended digging deeper resource: [Linux Command Line Basics](https://www.udacity.com/course/linux-command-line-basics--ud595)
                
### git log --oneline 
The "git log" command has a flag that can be used to alert how it displays the repo info.  The flag is "--oneline"

                              $ git log -- oneline 
                              
                              
![screen-shot-course-example](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/version-control-screenshot.png)

Quiz: 
* Q: You're deep in the weeds of the git log --oneline command and want to get out of the git log --oneline output and return to the regular command prompt. What do you press on the keyboard to return to the regular command prompt?
* A: "The Q Key. That's it! Remember, the q key gets out of the git log view. We're still using git log but are just passing a flag to change how the information is displayed. So the q key still works and returns the terminal to the command prompt.

### Common Error 
When using the --oneline flag, it is very common for people to typo and type "online" instead of "oneline" which produces the error message: "fatal: unrecognized argument: --online" This is VERY easy to misread/overlook.  Spell and read the code closely--typos are all too common.  

### git log --oneline Recap
* To recap, the --oneline flag is used to alter how git log displays information:
                    $ git log --oneline
This command:

    * lists one commit per line
    * shows the first 7 characters of the commit's SHA
    * shows the commit's message


## Viewing Modified Files 
The "--oneline" flag is great if we want to show just one commit per line, but what if we need more information? 

### QUIZ: 
Q: Search the log for commit SHA " " and find its message "Center content on page." What file or files were changed with this commit? 
A: There is no way to know for certain as it isn't recorded in the commit comment its self. From the log alone, we cannot tell. We'd need to open the files and compare them. This is one reason why a good, descriptive commit message is so important. But even with the commit message, we still don't know for sure what file or files were modified in this commit.

### git log --stat Intro
The "git log" commmand has a flag that can be used to display the files that have been changed in the commit.  This flag is the "--stats" flag.  Stat is short for statistics (not immeidately as it is in medical terms). 
                    $ git log --stat
                    
 
                    
### Using what we've learned, and the course repo, find the SHA "6f04ddd" and answer how many files were modified in the commit? 
A: 2 Files. 

### You did so well with the first one, so here's another! How many files were modified in the commit with the SHA 8d3ea36?
A: 2 Files. 

### Now it's time to look at the other info the --stat flag displays. How many lines of code were deleted in index.html in the commit with the SHA 8d3ea36?
A: 4 lines. 

## 'git log --stat Recap 
* To recap the "- - stat" flag is used to alter how "git log" displays information. 
                              $ git log - - stat
                              -displays the files that have been modified
                              -displays the number of lines which have been added and/or removed
                              -displays a summary line with the total number of modified files and lines that have been added and/or removed
                              

## Viewing File Changes 
* "git-log' shows us the commits in the repo. 
* if we add "--stat" flag, we can see what files were motidied and how many lines of code were added or removed. 
* next, is the best part of the version control system 

### "git log -p
* The "git log' command has a flag that can be used to display the actual changes made to the file. 
* when you run this command, you will see the results say "diff" 
* diff is the same as patch--it is the difference between the first file and the new file. 
* a green + indicates something which was added
* a red - indicates something which was deleted
* git sees formating or editing as a delition of the old (error) and then an addition of the correction (edit) 
* this flag is "--patch" which can be shortened to just "-p"

                    $ git log -p
                    
 ### Annotated git log -p output 
![course-example-image](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/ud123-l3-git-log-p-lines-removed-annotated.png)

    🔵 - the file that is being displayed
    🔶 - the hash of the first version of the file and the hash of the second version of the file
        not usually important, so it's safe to ignore
    ❤️ - the old version and current version of the file
    🔍 - the lines where the file is added and how many lines there are
        -15,83 indicates that the old version (represented by the -) started at line 15 and that the file had 83 lines
        +15,85 indicates that the current version (represented by the +) starts at line 15 and that there are now 85 lines...these 85 lines are shown in the patch below
    ✏️ - the actual changes made in the commit
        lines that are red and start with a minus (-) were in the original version of the file but have been removed by the commit
        lines that are green and start with a plus (+) are new lines that have been added in the commit

### Further Research 
Gererating Patches with -p from the git docs
Using what you've learned so far about git log's -p flag, look at the commit with the SHA 50d835d. What line number in app.css should you start looking at to see what has been changed? Tip - don't forget that while looking at the git log output, the d key will scroll down by half a page while the u key will scroll _up_ half a page. A: 127

Using git log and any of its flags, what code was added in by commit 4a60beb? A: color: #2e3d49; 

git log --stat and git log -p are both really helpful commands. Wouldn't it be great if we could have both of their output at the same time? Hmmm… What happens when git log -p --stat is run?  A: It displays both with the stats info above the patch info. That's right; you can combine flags! git log -p --stat will display the stats info above the patch info. Actually, the order doesn't matter; git log --stat -p will also show the stats info above the patch info. 

In the video above, we looked at a commit that indents a lot of code. The patch output shows all of those lines as having been removed and then added again at their new level of indentation. Showing all of the indent changes makes it hard to tell what was actually added, though.What does the -w flag do to the patch information? For help, check this Git docs page.  A: it ignores whitespace changes 

### git log -p recap
Flags:  -p --patch 
displays files which have been modified.
displays the location of the lines which has been added or removed 
displays the actual changes that have been made. 


## Viewing A Specific Commit 
Too Much Scrolling

The last few quizzes in the previous section had you scrolling and scrolling through the patch output just to get to the right commit so you could see its info. Wouldn't it be super handy if you could just display a specific commit's details without worrying about all of the others in the repo?

There are actually two ways to do this!

    providing the SHA of the commit you want to see to git log
    use a new command git show

They're both pretty simple, but let's look at the git log way and then we'll look at git show.

You already know how to "log" information with:

    git log
    git log --oneline
    git log --stat
    git log -p

But did you know, you can supply the SHA of a commit as the final argument for all of these commands? For example:

$ git log -p fdf5493

By supplying a SHA, the git log -p command will start at that commit! No need to scroll through everything! Keep in mind that it will also show all of the commits that were made prior to the supplied SHA.
New Command: git show

The other command that shows a specific commit is git show:

$ git show

Running it like the example above will only display the most recent commit. Typically, a SHA is provided as a final argument:

$ git show fdf5493

What does git show do?

The git show command will show only one commit. So don't get alarmed when you can't find any other commits - it only shows one. The output of the git show command is exactly the same as the git log -p command. So by default, git show displays:

    the commit
    the author
    the date
    the commit message
    the patch information

However, git show can be combined with most of the other flags we've looked at:

    --stat - to show the how many files were changed and the number of lines that were added/removed
    -p or --patch - this the default, but if --stat is used, the patch won't display, so pass -p to add it again
    -w - to ignore changes to whitespace

Q: How many rulesets are added to the CSS by commit 8d3ea36? A: 2
Q: There's a commit with the message "Convert social links from text to images". How many files were changed by this commit? A: 5 files. 
Q: Look at commit fdf5493. What's the first HTML heading element that's added by this commit? A: an <h2>


##  Lesson 3 Summary 
It is useful, when you are first starting out, to check how things are working so you understand it, as well as helping if you get confused/lost or suffer an "opps" moment (everyone does when they start out). 

## Study session notes.
* 2020-12-25 Created notes outline and linked to it. 
* 2021-01-08 Finished lesson. 


Nav:
[Readme](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/readme.md) | [Overview](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/version-control-course-notes.md) | [Install](https://github.com/EO4wellness/leary-leerie/blob/master/git-install-notes.md) | [Lesson 2](https://github.com/EO4wellness/leary-leerie/blob/master/git-repo.md) | [Lesson 3](https://github.com/EO4wellness/leary-leerie/blob/master/git-history.md) | [Lesson 4](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/add-commits.md) | [Lesson 5](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/tag-branch-merge.md) | [Lesson 6](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/Undo-Changes.md)

