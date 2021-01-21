# Undoing Changes Intro
What if i  made a mistake?  What if I want to end a trial beacuse I'm positiive no one will ever use it?  

This is what we are looking at in this lesson.  We will look at these through the following commands:

    git committ --amend 
    this command is used to alter the most recent commit 
    
    git revert 
    to use this command we need to provide the SHA of the commit we want revered. 
    
    git reset 
    you can delet committs but you have to do them in order 
    this is DANGEROUS so use it wisely 



## Modifying the Last Commit 
If you have made changes and notice a typo on your most recent commit you can fix it with the 

    $ git committ --amend 
    
command.  NOTE: This command only fixes the most recent commit. 

Is your Working Directory clean?  
This means there aren't any uncommitted changes in the repo. 

If so, you are now ready to run the git committ --amend command. 
Running it will allow you to provide a new commit message 
Your code editor will open, displaying the original commit message. 
You can fix it and save it and close the editor. 

## Add Forgotten Files to a previous commit. 
this command also allows adding files. 


## Reverting a Commit 
* Revert Recap
To recap, the git revert command is used to reverse a previously made commit:

      $ git revert <SHA-of-commit-to-revert>
      This command:
      
      will undo the changes that were made by the provided commit
      creates a new commit to record the change

Further Research

    [git-revert from Git Docs](https://git-scm.com/docs/git-revert)
    [git revert Atlassian tutorial](https://www.atlassian.com/git/tutorials/undoing-changes)


## Reseting commits 
***** Resetting Can be DANGEROUS ******* 
the quiz questions give a log and ask questions about which SHA represent each of the different commit and branch points
as that is not easy to replicate here, i skipped it in my notes but my answers were given and the lesson completed 

        [git-reflog](https://git-scm.com/docs/git-reflog)
        [Rewriting History](https://www.atlassian.com/git/tutorials/rewriting-history)
        [reflog, your safety net](http://gitready.com/intermediate/2009/02/09/reflog-your-safety-net.html)


      $ git reset <reference-to-commit>
      
      can be used to 
      
      move the HEAD and current branch pointer to the referenced commit
      erase commits
      move committed changes to the staging index
      unstage committed changes

      
Git Reset's Flags

The way that Git determines if it erases, stages previously committed changes, or unstages previously committed changes is by the flag that's used. The flags are:

    --mixed
    --soft
    --hard
    
[https://youtu.be/UN7ki2G2yKc](https://youtu.be/UN7ki2G2yKc)

The course instructor recommends, out of an abundance of caution, if you are going to use GIT RESET
to first create a backup branch on the most recent commit so it can be returned to if needed. 

    $ git branh backup 
    
   
Given 

      * e014d91 (HEAD -> master, footer) Add links to social media
      * 209752a Improve site heading for SEO
      * 3772ab1 Set background color for page
      * 5bfe5e7 Add starting HTML structure
      * 6fa5f34 Add .gitignore file
      * a879849 Add header to blog
      * 94de470 Initial commit
      
1. What will happen to the changes from the 3772ab1 commit if git reset --hard HEAD~3 is run? Will the changes be in the Staging Index, in the Working Directory, or complete erased?
A: erased. Yep! If the --hard flag is used, the changes are thrown out!

2. What will happen to the changes from the 209752a commit if git reset --soft HEAD^^ is run? Will the changes be in the Staging Index, in the Working Directory, or complete erased?
A: Staging Index. Yep! If the --soft flag is used, the changes are moved to the Staging Index! 

Reset Recap

To recap, the git reset command is used erase commits:

$ git reset <reference-to-commit>

It can be used to:

    move the HEAD and current branch pointer to the referenced commit
    erase commits with the --hard flag
    moves committed changes to the staging index with the --soft flag
    unstages committed changes --mixed flag

Typically, ancestry references are used to indicate previous commits. The ancestry references are:

    ^ – indicates the parent commit
    ~ – indicates the first parent commit

Further Research

    [git-reset from Git docs](https://git-scm.com/docs/git-reset)
    [Reset Demystified from Git Blog](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)
    [Ancestry References from Git Book](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#Ancestry-References)
    

## Lesson OUtro 
Timeless info and useful! 
 
## Course Outro 
I learned a lot! 
In this course I learned how to:
* Make Commits
* Review Changes 
* Develop on Branches 
* Merge branches and resolve any conflicts 
* Undo changes as needed 

Recommended next steps:
Expand On Your Git Skills

    take the companion GitHub course
    create a repo to track your computer's settings - https://dotfiles.github.io/
    develop the next, awesome feature for your personal project
    try tackling some Git challenges with the Git-it app


![Course-completion](https://github.com/EO4wellness/leary-leerie/blob/master/version-control/2021-01-20-Completed-udacity-coursework-Version-Control-GIT.png)
