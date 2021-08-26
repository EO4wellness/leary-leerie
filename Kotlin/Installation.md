# Course Installation Tips: 
* Verify IntelliJ Installation
* Check that your IntelliJ is installed and up-to-date by following these steps below:

    1. To check whether you need to install JDK, in a terminal window, type:
```
    java -version
    javac -version
```

my results: 
![results-image](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L1.5.jpg)


    2. If you do not have it, or do not have the latest version, download and install JDK.
    3. Install IntelliJ. This course uses IntelliJ and we recommend you use the same IDE.
    4. Start IntelliJ.
    5. Install any updates and additional content you are prompted for.
    6. Select IntelliJ IDEA -> Check for updates… until there are no more updates.



# Steps to Set up a Project: 
JDK (java developoment kit) 

1.  If you don't already ahve a JDK insalled, first install a JDK. 
2.  When you first start IntelliJ for the very first time, you have to set it up--> follow the on screen prompts. 
3.  Next, on the Welcome Screen select to create a new Kotlin Project.  To do so, click to add a new project. 
4.  Wait for the screen to change. 
5.  Select: Kotlin in the left-hand menu (Kotlin JVM) 
6.  Name your project (for this course we're naming the first one "HelloKotlin" 
7.  Click Finish 

The above steps have created our first project which is set up to run Kotlin. 

### REPL: 
* Now that you are in a project, you have access to the Kotlin REPL. 
* Kotlin REPL: Read-Eval-Print loop 
* a REPL evaluates the code you are typing right after you hit the enter comand.  
* a REPL is not a compliler; it doesn't run the code 
* Locate it from IntellJ IDEA --> Tools --> Kotlin --> Kotlin REPL 
* type or paste our code (block below) into the REPL 
```
fun printHello () {
   println ("Hello World")
}

printHello()
```
* Type Control + Enter to execute the code 
* Wait
* You should see "Hello World" (in green, in the default setup theme) 

My Result: 
![result](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L1.6.jpg) 


Kotolin Documentation: https://kotlinlang.org/docs/home.html  

### CODE DESCRIPTION: 
* fun designates a function 
* the bit which follows "fun" is the name of the function 
* this is followed by a set of parenthesis where the arguments go.  
* the PrintHello function doesn't include any arguments so the () are blank 
* Next are a set of curly braces
* the curly braces frame the function body 
* inside the function body, we can make calls. 
* this function makes the println call 
* this function prints one line of text. namely the string: Hello World 
(note: no punctuation at the end; no need to specify a return in this case) 


these are the only installed tools we're going to be using in this course. 
