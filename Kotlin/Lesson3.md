# Functions 
* Create and call functions
* use default and variable arguments 
* pass functions as arguments to filters
* and program simple lambdas 

3.1  Introduction 
* mastered the basics
* time to write more useful features 

3.2  Main Function 
* all Kotlin functions start with the key word ```fun``
* next is the name of the function ```helloWorld```
* followed by parenthesis for arguments ```()```
* next is the function body.  
* the body is where things happen. 
* the body is always inside curly braces. ```{}```
* Example: 
``` 
fun helloWorld() { 

}
```
*  the parenthesis can be empty if there aren't any arguments 
*  we would envoke the function by calling its name followed by the parenthesis. 




Let's say instead of using the interpreter we want to write a program in IntelliJ, then we would need to follow these steps: 
1.  In the left hand corner, there is a list of all of our project files and folders. 
2.  Find, then right-click, the SOURCE folder. 
3.  Select "New" "Kotlin File Class" from the pop out menus. 

![image1](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.2_create-new-class-source-file.jpg)

4. Name the file AMS
5. Press Okay. 
6. This now adds the AMS file to the source folder. 

![image2](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.2_AMS.kt_file-to-write-code.jpg)

* Following these steps creates the file in your source folder. 
* Its extension is dot kt 
* We can use this file to write code. 
* We will still use the REPL too 
* We will switch back and forth. 

### Running Code 
* To run a Kotlin program, we need a main program. 
* Main is always the entry point for executing Kotlin code. 
* In Kotlin it looks like this: 
```
fun main(args: Array<String>) {
    println("Hello, world!")
}
```
* it takes an array of strings as its arguments
* followed by the function body in curly braces 
* we print "Hello World" 
* this function does not have a return statement 
* every Kotlin function returns something 
* even when nothing is specified 
* A function like main returns a type unit 
* this is Kotlins way of saying "no value" 
* you don't have to explicitly say you are returning nothing 
* Run this function by clicking on the green arrow, then select AMSkt

![image run program](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.2-run-a-main-function.jpg)


* IntelliJ will take a moment to build and execute the code 
* Then it will show the result in the log window that opens. 

![image-log-window](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.2-results-run-main-function.jpg)

3.3  Quiz: Practice Time 
3.4  Main Argumements 
3.5  Greetings: Kotlin: 
3.6  Random Day 
3.7  Quiz: Practice Time 
3.8  Fish Food 
3.9  Quiz: Practice Time 
3.10 Changing Water 
3.11 Fit More Fish 
3.12 Building the Aquarium 
3.13 Quiz: Practice Time 
3.14 Compact Functions 
3.15 Quiz: Practice Time 
3.16 Kotlin Filters 
3.17 Quiz: Practice Time 
3.18 Kotlin Lambdas 
3.19 Quiz: Practice Time 
3.20 Summary 
