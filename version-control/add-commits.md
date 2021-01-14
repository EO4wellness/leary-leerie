# Lesson 4: Adding Commits to a Repo

1. Intro
We've laid the ground work to now know how to make our own first commit.  We need the available course "[cheatsheet](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/Common-Terms-GIT-cheatsheet.pdf)" to complete this lesson--have it available.

    GROUND WORK (foundation we already know) 
    git init - create a new repo
    git clone - copy an existing repo 
    git log - review existing commands 
    git status - see the status of a repo 
    
    BUILDING WITH:
    git add - Add files from the working directory to the staging index. 
    git commit - Take files from the staging index and save them to the repo. 
    git diff - Displays the difference between two versions of a file. 
    

2. Git Add
[continue studies here](https://classroom.udacity.com/courses/ud123/lessons/5f584ce7-1b7b-4848-80c1-b559739ea363/concepts/85cd2f5e-a3a9-467f-9043-96d8b627787b)
Much of this lesson is "set up" to be able to do a commit. So we follow along with the instructions within the course to create certain files and folders.  Then we type the command:

      $ git status 
      
      
      On branch master

Which returned:

      No commits yet
      
      Untracked files:
        (use "git add <file>..." to include in what will be committed)
        
            css/
            index.html
            js/
            
            nothing added to commit but untracked files present (use "git add" to track)

Git Add Recap

The git add command is used to move files from the Working Directory to the Staging Index.

$ git add <file1> <file2> … <fileN>

This command:

    takes a space-separated list of file names
    alternatively, the period . can be used in place of a list of files to tell Git to add the current directory (and all nested files)


3. Git Commit

    $ git commit
    
 Now opens our code editor we set up in the beginning of the course (in my case it is notepad ++

Terminal Hangs

If you switch back to the Terminal for a quick second, you'll see that the Terminal is chillin' out just waiting for you to finish with the code editor that popped up. You don't need to worry about this, though. Once we add the necessary content to the code editor and finally close the code editor window, the Terminal will unfreeze and return to normal.

Our terminal is chilling displaying the message:

     $ git commit
       hint: Waiting for your editor to close the file... 

And our code editor contains the text:

        # Please enter the commit message for your changes. Lines starting
        # with '#' will be ignored, and an empty message aborts the commit.
        #
        # On branch master
        #
        # Initial commit
        #
        # Changes to be committed:
        #	new file:   css/app.css
        #	new file:   index.html
        #	new file:   js/app.js
        #
        
Type out your commit message on the first line of the code editor. 


Save the file. 


Close the file. 


Switch back to the terminal. 

        $ git commit
        [master (root-commit) ee19a8e] Initial Commit
        3 files changed, 14 insertions(+)
        create mode 100644 css/app.css
        create mode 100644 index.html
        create mode 100644 js/app.js


 That's all there is to it. At first, version control seems like this overwhelming obstacle that one must overcome to become a true programmer/developer/designer/etc. But once you get a handle on the terminology (which I think is the most challenging part), then actually using version control isn't all that challenging.
 
 
 
    Bypass The Editor With The -m Flag

    TIP: If the commit message you're writing is short and you don't want to wait for your code editor to open up to type it out, you can pass your message directly on the command line with the -m flag:
    
    $ git commit -m "Initial commit"
    
    
    Be aware that you can't provide a description for the commit, only the message part.
    
    
    

 
4. Commit Messages 

5. Git Diff 

6. Having Git Ignore Files 

7. Outro-Lesson 4 Recap

### Session Notes:
* Set this lesson up 2021-01-08
