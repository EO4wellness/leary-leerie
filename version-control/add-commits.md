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
    
    
## What to Include in a Commit
* How do you know WHEN to do a commit?  
* What do you include in a commit? 
* The GOAL is that each commit has a single focus. 
* Each commit should record a SINGLE unit of CHANGE. 
* It is subjective. 
* Each commit should make a change to just one aspect of the project. This takes practice. 
* there is no LIMIT to the number of lines or of code changed. 
* added/removed/modified are all different changes. 
* Example:
        
            Say for example you are changing a side bar.
            Normally, you'd want to make a commit when:
                - you add a new image to the project files.
                - you alter any of the HTML
                - add or modify CSS to incorporate the new image 
            Yes, a committ which records ALL of these changes 
            (vs. 2-4 commits for each element of it) would be equally fine.
            
            However the same commit shouldn't contain changes on two different elements 
            for example- change in side bar image and rewording of page content 
            in that example, each change should be a seperate commit 
            
* Excellent commit test is to think: what would happen if everyting in this commit was erased by accident? If a commit were erased, it should idealy only remove one thing (not a lot of work to replace.) 
* as a side note, in an upcomming lesson, we learn how to "undo" so don't worry--this is just a way of thinking about what is and what is not a new commit (or should be). 

## Git Committ Recap 
* The Git Commit command takes the files from the staging inex and saves them in the repo. 
        $ git commit 
* commit is spelled with ONE T not two.
* the git commit command will open the code editor that is specified in my config 
* inside the code editor:
        a commit message must be supplied
        lines that start with a "#" are comments and will not be recorded
        save the file after adding a commmit message 
        close the editor to make the commit
        then use 'git log' to review the commit you just made
        verify everything or correct any mistakes 

## Suggested Further Reading 
[Associating text editors with Git from GitHub Help Docs](https://docs.github.com/en/free-pro-team@latest/github/using-git/associating-text-editors-with-git)<br>
[Getting Started - First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) from Git book<br>
 
4. Commit Messages 
How do I write a good commit message? And why should I care?
* Keep the message short (less than 60ish characters)
* do explain what the commit does
* do not explain how it does it
* do not explain why it does it 
* do not use the word "and" 
* note the use of "and" indicates it should be TWO commits 
  such as the example: 
   commit message: change bg color AND increase sidebar size
* Finish this phrase with your commit message: "This commit will..." 


## Commit Quiz
1.  Q: Reviewing the guidelines on what makes a good commit message, is the following commit message good?
"Update the footer to copyright information"
    A: Yes. "Great job! This commit is short. It explains what was changed but doesn't explain how it was changed or why."


2. Is the following a good commit message?
"Add a
tag to the body"
    A: No. "The commit message should not contain specifics on how the change was made. This information can be found by running git log -p."
    
    
3. Is the following a good commit message?
"Add changes to app.js"
    A: No. "That's right! Make sure to explain what was changed. Don't just state that changes were made or where they were made."

## Explain the Why

If you need to explain why a commit needs to be made, you can!

When you're writing the commit message, the first line is the message itself. After the message, leave a blank line, and then type out the body or explanation including details about why the commit is needed (e.g. URL links).

This details section of a commit message _is_ included in the git log. To see a commit message with a body, check out the Blog project repo and look at commit 8a11b3f.

## Commit Style Requirements
* each group or place you work with are likely to have their own unique requirements/commit styles
* Udacity Commit Style Guide: https://udacity.github.io/git-styleguide/ 
* 50/72 Rule: https://preslav.me/2015/02/21/what-s-with-the-50-72-rule/ 
* How to Write a Git Committ Message: https://chris.beams.io/posts/git-commit/ 

5. Git Diff 
* We've seen a bit of this, already, while looking at the previous lesson--it shows up in the History. 
* If you are working, get interupted and come back to your project, which you haven't finished then what?
* If you use "git status" it will tell you which files have been changed, and how recently they have been changed, but it won't show the actual changes. 
* get diff is the command which does show the actual changes. 
* get diff can be used to see changes that have been made but haven't been committed yet. 

        $ git diff
        
### RECAP: 
* the git diff command allows us to see changes that have been made but haven't been committed yet. 
* the command displays files that have been modified
* the location of the lines that have been added and/or removed 
* the actual changes which have been made

### More Info:
* Look at the [git diff documentation](https://git-scm.com/docs/git-diff) from the from the Git Docs

6. Having Git Ignore Files 
During the "git add" section, we learned a period (.) is a special character which inidcate the current director and all of its subdirectories

When using the "period." to include all files, you can not add one or more file(s) (filetypes) 

When you list your files, if you have a few you don't want in the repo, use .gitignore 

.gitignore will keep a file in the file structure directory, but make certain it isn't committed to the project. 


Globbing Crash Course

Let's say that you add 50 images to your project, but want Git to ignore all of them. Does this mean you have to list each and every filename in the .gitignore file? Oh gosh no, that would be crazy! Instead, you can use a concept called globbing.

Globbing lets you use special characters to match patterns/characters. In the .gitignore file, you can use the following:

    blank lines can be used for spacing
    # - marks line as a comment
    * - matches 0 or more characters
    ? - matches 1 character
    [abc] - matches a, b, _or_ c
    ** - matches nested directories - a/**/z matches
        a/z
        a/b/z
        a/b/c/z

So if all of the 50 images are JPEG images in the "samples" folder, we could add the following line to .gitignore to have Git ignore all 50 images.

[WikiPedia GLOB (programming)](https://en.wikipedia.org/wiki/Glob_(programming))

QUIZ:
Which of the following files will be ignored if *.png is entered into the .gitignore file?

        ocean.jpg
        [trees.png]
        png-format.pdf
        not-a-png.jpeg
        [bg-pattern.png]
        logo.gif
        [LOUDFILE.PNG]
        
That's right! Adding *.png will cause Git to ignore all PNG images.       

If you ask GIT to ingore "be?rs" which of the following files will be ignored?

        [bears] 
        beavers 
        BeArS
        [beers]
        boars 

Git Ignore Recap

To recap, the .gitignore file is used to tell Git about the files that Git should not track. This file should be placed in the same directory that the .git directory is in.
Further Research

    [Ignoring files from the Git Book](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Ignoring-Files)
    [gitignore from the Git Docs](https://git-scm.com/docs/gitignore#_pattern_format)
    [Ignoring files from the GitHub Docs](https://docs.github.com/en/github/using-git/ignoring-files)
    [gitignore.io](https://www.toptal.com/developers/gitignore)



7. Outro-Lesson 4 Recap

### Session Notes:
* Set this lesson up 2021-01-08
