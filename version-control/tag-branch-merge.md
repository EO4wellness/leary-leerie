# Lesson 5: Course Notes: Tagging, Branching, and Merging
The content of this lesson will really supercharge your GIT experiene(s) and level of ability to use Git effectively.

## Intro:
* This will level up version control superpowers. 
* Lesson Commands.
      
      git tag: used to add tags to specific commits 
      
      git branch: allows you to develop different features of your project, in parallel without getting confused which commits belong to which feature
      
      git checkout: switch between different branches and tags
      
      git merge: HELPFUL!  allows you to combine different changes on different branches and combine them together 
      

## Tagging:
* tags allow you to label a specific commmit to help it stand out from all of the others in a specific way.
* such as git tag -a v1.0 (for version 1.0)
* the tag stays locked to a specific commit even as more commits are added to the repo. 


         Git Tag Command 
    
         $ git tag -1 v1.0
         
         note: the -a portion of this tells Git to create an annotated flag. 
         if you don't include the "-a" then it will create what is called a lightweight tag
         the code for the lightweight tag is git tag v1.0 
         
         Annotated tags are always recommended, because they include a lot of extra info such as:
            the person who made the tag
            the date the tag was made 
            a massage for the tag 
  
 ### Verify Tag 
* After creating, saving and then quitting the editor, nothing is displayed in the command line. 
* How can we know if a tag was added to our commit within our project? 
* Type "git tag" and it will display all tags that are in the repo. 
* Thus we've verified our tag was created and is in the repo. 
 
        $ git log --decorate
        
 as of version 2.13 you don't need to type the "--decorate" as it is now automatic 
 as of version 2.13 both of the following commands have the exact same output (they didn't use to)

        $ git log --decorate
        $ git log 
        
[version 2.13 release notes](https://github.com/git/git/blob/v2.13.0/Documentation/RelNotes/2.13.0.txt#L176-L177) 

### Deleting A Tag 
* what if you made a mistake, typo, mispelling in something in the tag's message? 
* you can fix it. 
* first delete the tag
* then make a new one, which is correct 
* git tags can be delted with the -d flag (d for delete)

        $ git tag -d v1.0
        
### Adding Tags to Old Commits 
* Running $ git tag -a v1.0 will tag the most recent committ
* what if you want to tag another committ? 
* to do so, all you have to do is provide the SHA of the committ you want to tag. 

Jump to content
Email for accessibility support
Lesson 5: Tagging, Branching, and Merging

1. Intro
2. Tagging
3. Branching
4. Branching Effectively
5. Merging
6. Merge Conflicts

    7. Outro

Tagging

So far in this course, we've been zoomed in on the specific Git commands. We've learned how they work in detail and what it looks like running them on the Terminal.

Let's zoom out a bit to look at how a Git tag fits into a repository.
Where Are We?

You can do these steps in either project, but I'll be doing them in the new-git-project project.

Let's take a look at the log of the project so far:
The Terminal application showing the output from running `git log --oneline`.

The Terminal application showing the output from running git log --oneline.
Git Tag Command

Pay attention to what's shown (just the SHA and the commit message)

The command we'll be using to interact with the repository's tags is the git tag command:

$ git tag -a v1.0

This will open your code editor and wait for you to supply a message for the tag. How about the message "Ready for content"?
Code editor waiting for the tag's message to be supplied.

Code editor waiting for the tag's message to be supplied.

    CAREFUL: In the command above (git tag -a v1.0) the -a flag is used. This flag tells Git to create an annotated flag. If you don't provide the flag (i.e. git tag v1.0) then it'll create what's called a lightweight tag.

    Annotated tags are recommended because they include a lot of extra information such as:

        the person who made the tag
        the date the tag was made
        a message for the tag

    Because of this, you should always use annotated tags.

Verify Tag

After saving and quitting the editor, nothing is displayed on the command line. So how do we know that a tag was actually added to the project? If you type out just git tag, it will display all tags that are in the repository.
The Terminal application showing the output of the `git tag` command. The tag `v1.0` is listed.

The Terminal application showing the output of the git tag command. The tag v1.0 is listed.

So we've verified that it's in the repository, but let's actually see where it is inside the repository. To do that, we'll go back to our good old friend, git log!
Git Log's --decorate Flag

As you've learned, git log is a pretty powerful tool for letting us check out a repository's commits. We've already looked at a couple of its flags, but it's time to add a new one to our toolbelt. The --decorate flag will show us some details that are hidden from the default view.

Try running git log --decorate now!

    💡 --decorate Flag Changes in Git 2.13 💡

    In the 2.13 update to Git, the log command has changed to automatically enable the --decorate flag. This means that you do not need to include the --decorate flag in your command, since it is automatically included, anyway! So the following commands result in the exact same output:

    $ git log --decorate
    $ git log

    Check out the 2.13 release notes.

The Terminal application showing the output of the `git log --decorate` command. The log output now displays the newly created tag.

The Terminal application showing the output of the git log --decorate command. The log output now displays the newly created tag.

The tag information is at the very end of the first line:

commit 6fa5f34790808d9f4dccd0fa8fdbc40760102d6e (HEAD -> master, tag: v1.0)

See how it says tag: v1.0? That's the tag! Remember that tags are associated with a specific commit. This is why the tag is on the same line as the commit's SHA.

    HEAD -> master?

    Did you notice that, in addition to the tag information being displayed in the log, the --decorate also revealed HEAD -> master? That's information about a branch! We'll be looking at branches in Git, next.

Deleting A Tag

What if you accidentally misspelled something in the tag's message, or mistyped the actual tag name (v0.1 instead of v1.0). How could you fix this? The easiest way is just to delete the tag and make a new one.

A Git tag can be deleted with the -d flag (for delete!) and the name of the tag:

$ git tag -d v1.0

The Terminal application showing the removal of a tag by using the `-d` flag. The command that is run is `git tag -d v1.0`.

The Terminal application showing the removal of a tag by using the -d flag. The command that is run is git tag -d v1.0.
Question 1 of 3

By default, a Git tag will not appear in a log. What flag must be used to display the tag information in the output of git log?

    --decorate

Question 2 of 3

Which of the following will delete the tag v-1?

    git tag --delete v-1

git tag -d v-1
Adding A Tag To A Past Commit

Running git tag -a v1.0 will tag the most recent commit. But what if you wanted to tag a commit that occurred farther back in the repo's history?

All you have to do is provide the SHA of the commit you want to tag!

$ git tag -a v1.0 a87984

(after popping open a code editor to let you supply the tag's message) this command will tag the commit with the SHA a87084 with the tag v1.0. Using this technique, you can tag any commit in the entire git repository! Pretty neat, right?...and it's just a simple addition to add the SHA of a commit to the Git tagging command you already know.
Tag Older Commit?

Using the following git log --oneline information, what command would you run to give the commit with the message "style page header" a tag of beta?

2a9e9f3 add breakpoint for large-sized screens
137a0bd add breakpoint for medium-sized screens
c5ee895 add space around page edge
b552fa5 style page header
f8c87c7 convert social links from text to images

2a9e9f3 add breakpoint for large-sized screens
137a0bd add breakpoint for medium-sized screens
c5ee895 add space around page edge
b552fa5 style page header
f8c87c7 convert social links from text to images
Git Tag Recap

To recap, the git tag command is used to add a marker on a specific commit. The tag does not move around as new commits are added.

      $ git tag -a beta

This command will:

     add a tag to the most recent commit
     add a tag to a specific commit if a SHA is passed

Further Research

       [Git Basics - Tagging from the Git Book](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
       [Git Tag from the Git Docs](https://git-scm.com/docs/git-tag)



## Branching:
[Overview](https://youtu.be/ywcOC6CLG4s)


* The command used to interact with branches is the GIT BRANCH command 

            $ git branch
            
* The "git branch" command can be used for
            
            listing all of the branch names in the reop 
            creating new braches
            deleting branches 
            
* when we type "git branch" it will list all of the branches in a repo.

### Create a Branch
* To create a branch, use "git branch" to provide a name for the new branch you want to create.
* Example:  

            Create a new branch named "sidebar"
            
            Solution:
            
            $ git branch sidebar 
            
### Quiz
Remember that there are a number of branches in the reop, but that the command prompt displays the *current branch.*


Now that we just created a new "sidebar" branch, does the command prokmpt displays "sidebar" or "master?"

A:  Master. 

"That's right! Even though you created the sidebar branch, it's not the current branch just yet. We need to switch to it."


### Git Checkout COmmand 
Remember that when a commit is made that it will be added to the current branch. So even though we created the new sidebar, no new commits will be added to it since we haven't switched to it, yet. If we made a commit right now, that commit would be added to the master branch, not the sidebar branch. We've already seen this in the demo, but to switch between branches, we need to use Git's checkout command.

$ git checkout sidebar

It's important to understand how this command works. Running this command will:

    remove all files and directories from the Working Directory that Git is tracking
        (files that Git tracks are stored in the repository, so nothing is lost)
    go into the repository and pull out all of the files and directories of the commit that the branch points to

So this will remove all of the files that are referenced by commits in the master branch. It will replace them with the files that are referenced by the commits in the sidebar branch. This is very important to understand, so go back and read these last two sentences.

The funny thing, though, is that both sidebar and master are pointing at the same commit, so it will look like nothing changes when you switch between them. But the command prompt will show "sidebar", now:


### Branches in the Log

      $ git log --oneline --decorate 
      
 what ever is listed next to "Head" will be the branch where our new commits will go. 
 
 ### The Active Branch 
 
 From what you know about both the GIT BRANCH and GIT TAG commands, what do you think the following command will do?

      $ git branch alt-sidebar--loc 42a69f
      
  My answer:  It will create the alt-sidebar-loc branch and have it point to the commit with the SHA 42a69f

"That's right! It creates a new branch called alt-sidebar-loc and has it pointing at the commit with the SHA 42a69f"

Which branch is active:

            $ git branch
            barbara
            * footer-fix
            master
            richard
            sidebar
            social-icons

"That's right! Because the asterisk is next to footer-fix, that means it's the active branch."

### Delete A Branch

A branch is used to do development or make a fix to the project that won't affect the project (since the changes are made on a branch). Once you make the change on the branch, you can combine that branch into the master branch (this "combining of branches" is called "merging" and we'll look at it shortly).

Now after a branch's changes have been merged, you probably won't need the branch anymore. If you want to delete the branch, you'd use the -d flag. The command below includes the -d flag which tells Git to delete the provided branch (in this case, the "sidebar" branch).

$ git branch -d sidebar

One thing to note is that you can't delete a branch that you're currently on. So to delete the sidebar branch, you'd have to switch to either the master branch or create and switch to a new branch.

Deleting something can be quite nerve-wracking. Don't worry, though. Git won't let you delete a branch if it has commits on it that aren't on any other branch (meaning the commits are unique to the branch that's about to be deleted). If you created the sidebar branch, added commits to it, and then tried to delete it with the git branch -d sidebar, Git wouldn't let you delete the branch because you can't delete a branch that you're currently on. If you switched to the master branch and tried to delete the sidebar branch, Git also wouldn't let you do that because those new commits on the sidebar branch would be lost! To force deletion, you need to use a capital D flag - git branch -D sidebar.

Git Branch Recap

To recap, the git branch command is used to manage branches in Git:

# to list all branches
$ git branch

# to create a new "footer-fix" branch
$ git branch footer-fix

# to delete the "footer-fix" branch
$ git branch -d footer-fix

This command is used to:

    list out local branches
    create new branches
    remove branches

Further Research

[Git Branching - Basic Branching and Merging from the Git Docs](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
[Learn Git Branching](https://learngitbranching.js.org/)
[Git Branching Tutorial from the Atlassian Blog](https://www.atlassian.com/git/tutorials/using-branches)


## Branching Effectively:
after verifying the repo is set up correctly, the coursework offers suggests to work through the process of creating a new branch and then switching back and forth between them to offer practice and also to help visualize all of the concepts studied thus far. 

there are some quiz questions about this--such as, after having created a new branch, and adding some changes to the CSS file in the new branch, why it isn't showing up in the master branch--that original file is empty.  this is because of the branching.  the original file was empty.  the modification was in a new brnach. 

next question is about the commands, which one shows what changes have been saved but not yet committed.  the answer is git diff 

Command to see all of the changes at once

      $ git log --oneline --decorate --graph --all
      
 
## Merging:

## Merge Conflicts 

## Outro

### Study session notes:
* 2021-01-16 I set up this note and linked it. 
* 
