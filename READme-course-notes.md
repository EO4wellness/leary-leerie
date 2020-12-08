# Intro 
The information presented below are my course notes compiled while taking:
* Udacity Course:  Writing READMEs<br>
* Course Developer: Walter Latimer <br>
* Course Link: https://classroom.udacity.com/courses/ud777<br>
Documentation is an important part of the development process.  Walter begins the course by explaining how a recipe book is like technical documentation.  He states that a Recipe Book exists to help us put to TASTY use the ingredients and tools we have in our kitchens.  Likewise, technical documentation helps us make sense of code. 

## BEST PRACTICES 
The best practice is to write documentation for all of your projects, without exception.  Technical documentation should be written in plain English, easy to read, and can serve the prupose of being a guide or tutorial, as well as refreshing our memory about what a particular segment of code does. Excellent documentation is needed, when working on Open Source coding projects, to find new users and contrbitors to your coding projects.  Further, your project may serve as your coding portfolio and good documentation is essential for finding development related work. 

Anyone using third-party code libraries, must use documentation daily to understand the code to be able to use it. Often when there is no documentation written for the project, we kick ourselves later for the mistakes it creates. Often on older projects, which aren't documented, it is difficult to recall what we were thinking when we wrote it. 

Allow your READme writing skills to grow with your project and evolve over time. 

## READme contents 
README.md files should contain all of the information we need to use the code within the repository.  There are several parts of a README which make it functional. 

1. Title - Description (written for PEOPLE) 
2. Installation or Getting Started (instructions) 
3. Usage (what is needed to understand your code and its function)
4.  Dependancy on other libraries (if needed).
5.  Known Bugs (if any). 

A certain length or format for what needs to be in a README. Communicate clearly what any end-user of your code/project would need to use the code.  Do not make any assumptions about what the user of your code may already know. 

To determine what information to include or exclude in your README are: 
1.  What are the exact steps which need to be taken?
2.  What should someone who is going to use this repository already have installed or configured before beginning with this code? 
3.  What might a user of this repository have a hard time understanding right away? 

## CopyRight and Licensing Information
By default, you retain full rights to your source code. The default copyright laws include that no one else can reproduce, distribute, or create derivative works of your work.  This may or may not suit your project. GitHub has a Terms of Service which can modify your intented copyright or licensing. 

## Contributing Statement 
If you intend to allow others to contribute to your project, you should have both a contribution statement, which describes how others are welcome to contribute, and a licensing statement. 

## Format:
A readme file can be written in Markdown or HTML. Markdown, or some version of it, is widely used throughout the internet.  Using markdown makes your readme easier to skim through for the content the end-user is looking for, or to refresh your own memory.   


## Markdown
* Commonly used for GitHub ReadME files. 
* Has other uses too. 
* Like languge has dialetcs, Markdown has flavors. 

## Markdown Syntax
Feeling Bold?

To make text bold, surround it with double asterisks. So this code:

Isn't today a **wonderful** day?

becomes: Isn't today a wonderful day?

This reads a bit more nicely than a <strong> tag would in HTML, and takes considerably fewer keystrokes to type out.
Italics, I tell you!

To italicize text, surround it with underscores. So this code:

And in that moment I thought to myself: _Did I turn off the stove?_

becomes: And in that moment I thought to myself: Did I turn off the stove?

Much like the previous example, this code reads much more like English, which is great for when you're skimming the original document.
To code, or not to code?

Inline code is useful for indicating that you're writing code and not a regular word. For this, you'll surround text in backticks (`, not a single quote). So this code:

You should use the `strong` tag.

becomes: You should use the strong tag.

...which makes much more sense than "You should use the strong tag."
The Title Sequence

Headings are even simpler! For h1 through h6 tags, all you'll need is a # before your text. The number of #s you include tells Markdown which header tag you're using. For example:

## This is an h2.

### This is an h3.

becomes...
This is an h2.
This is an h3.

