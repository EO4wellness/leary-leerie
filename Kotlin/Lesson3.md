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
* Learned the error message ```the error message "Expecting a top level declaration ``` means you have too many curly braces in your code. 

Exercise One: 

![my solution](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.3.jpg)

![course-solution](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.3-course-solution.jpg)


Exercise Extension: 
* When I first tried to run this code, I had to wait for the text to load, as the instructor mentioned in the first video.
* Then on a windows computer, i needed to allow the pop out text to appear over the red highlighted "calendar" word
* then i had to use alt+shift+enter to load the calendar library 
* before I could run this code. 
* when I did run it, eventually an error message was returned. 
* i had to google the error message
* find the solution on overstack
* fix the code
* then re-run it. 


![my solution](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.3_extend.jpg)



![course-solution](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.3-extend-solution.jpg)


3.4  [Main Argumements](https://classroom.udacity.com/courses/ud9011/lessons/14fb1ae9-8a2e-48ee-9620-68c87c5f833b/concepts/9b054fd9-dfab-430f-add8-2be2d77167c2)
* This lesson starts with a link to [string templates](https://kotlinlang.org/docs/basic-syntax.html#using-string-templates) in the instructor notes. 
* While the link was valuable it didn't go to information on strings
* Obviously something changed since the instructor notes were writen. 
* I googled it and found this: https://kotlinlang.org/docs/basic-types.html#strings

### How to Run Main with Arguments: 
Step 1: Pass into Main whom to say hello to. 
Step 2: Select RUN
Step 3: Edit Configuration 

![L3.4_run_edit-config](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.4_run_edit-config.jpg) 


Step 4: Type "Kotlin" for the program arguments box. 
Step 5: "okay" to close the configuration window 

![L3.4_kotlin-okay.jpg](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.4_kotlin-okay.jpg)


Step 6: Change your code to use the argument 
Step 7: replace ```world``` with a ```$``` to start a string template 

When using a STRING TEMPLATE instead of placing a string, you put instructions of how to get the string. 
-- from a variable 
-- from an expression 

In our example case, we are going to insert the value from our argument (Kotlin) 
We get this value from ${args{0}}

We use the formating curly brackets around the (parenthesis value for which item--zero means the first position) 
and this is an expression. 

![L3.4_example](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L3.4_example.jpg)

### Statements
* STATEMENTS:  Lines of code which do not have a value. 
* statements are common in other languages. 
* in Kotlin almost everything has a value. 
* even if the value, in Kotlin, is a unit, it is a value 
* so... in Kotlin it is said: 
* Everything in Kotlin is an expression 
* this means you can use the value of an IF expression right away 



3.5  [Greetings: Kotlin:](https://classroom.udacity.com/courses/ud9011/lessons/14fb1ae9-8a2e-48ee-9620-68c87c5f833b/concepts/4e7dd6df-9713-4a05-9d99-959854ecea6e)
```
Greetings, Kotlin
Exercise: Greetings, Kotlin

Create a main() function that takes an argument representing the time in 24-hour format (values between and including 0 -> 23).

In the main() function, check if the time is before midday (<12), then print "Good morning, Kotlin"; otherwise, print "Good night, Kotlin".
Notes:

Remember that all main() function arguments are Strings, so you will have to convert this argument to an Int before you can apply the check.
Advanced

Try to use Kotlin's string templates to do this in 1 line.

```

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
