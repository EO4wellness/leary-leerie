# [Kotlin Basics](https://classroom.udacity.com/courses/ud9011/lessons/605a8cec-a22b-4778-a682-39b35cf8467b/concepts/5336c2ca-7a4f-4566-bc90-0a922b5e44c5)

![image-logo](https://video.udacity-data.com/topher/2018/March/5ab4e951_screen-shot-2018-03-23-at-1.47.03-pm/screen-shot-2018-03-23-at-1.47.03-pm.png)


## 2.1 Introduction 
* the course is designed to "follow along" coding with the examples to learn 
* compares to an aquarium 

## 2.2 Kotlin Documentation 
* Throughout the course, refer back to the documentation
* Recommended to do this EACh time we learn new code 
* https://kotlinlang.org/docs/home.html 

## 2.3 Operators: 
* To follow along, select Kotlin REPL from the TOOLS menu of IntelliJ in our Hello World project. 
* Type ``` 1+1``` and then ```control + enter```
* Output is: 
```
1+1
res0: kotlin.Int = 2
```
* type 53-3 and control+enter to see the output of: 50 
* Next type 50/10 to divide the group.  
* Note dividing an integer by an integer always returns an integer
* thus our input: 
```50/10```
returns: 
```5```
* likewise 1/2 returns "0" and 1.0/2.0 returns 0.5 

My Follow Along: 

![L2.3](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.3.jpg) 

* You aren't just stuck with basic operators
* You can define your own groups (such as fish) and give them abilities to multiply
* Example: 
```
fish * 2 
```
* Kotlin keeps numbers as primatives 
* PRIMATIVES: the same number types your CPU uses 
* Kotlin will let you call methods on them, like they are objects 
Examples given: 
```
val fish = 2 
fish.times( other:6)
fish.div( other: 10) 
fish.plus( other: 3) 
fish.minus( other: 3) 
```
* things to note about basic types: 
  -  you can use numbers as if they were objects 
  -  use primitive "int" as an object 
  -  Kotlin also supports object wrappers for numbers 
  -  1.toLong() 
  -  all of the numerical types in Kotlin have a super type called number 
  -  or, put int in a box 
  -  val boxed: Number = 1 
     boxed.toLong()
     1
  -  BOXING: if you try to store the value one, 
     in a variable type of number, 
     it will need to be placed in an object wrapper 
     (this is called boxing) 
  -  it will be implicitely done when ever it is needed in your program 
  -  as a developer, you can avoid boxing object wrapers by not storing numbers in objects 

* To write useful code, you have to be able to store values. 
* Store in varriables: 
  1.  Changeable 
  2.  Unchangeable 
* Use the code ``` val ``` to assign a value once 
* you will get an error if you try to assign a value again later.  

![Lesson 2.3 Val error message example](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.3-val-error-message.jpg) 


* however with the code ```var``` you can change it: 
example: 

![var image](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.3-var.jpg) 

* The "type" is inferred. 
* This means the compiler can figure out the type from the context. 
* The type becomes FIXED at compile time 
* you cannot change a variable's type in Kotlin once its type has been determined 
* (this means once its compiled if you try to change the type of variable it will give an error message) 
* Example: 
after compiling our above code (where fish was assigned first var 2 and then 50, which is the type of "number" ) 
if you then type: 
```
fish = "Bubbles" 
```
it will return this error: 
```
error: type mismatch: inferred type is String but Int was expected
fish = "Bubbles" 
```
* You can use varriables in operations.  
* There is no punctuation at the end 
* Examples: 
```
val plants = 5 
val fish = 5 
fish + plants 
7 
```

* Implicit: 
* Number types won't implicity convert to other types. 
* so you cannot assign a short value to a long variable 
* you cannot assign a byte to an int 
* Kotlin does this because implicity numberical conversion is a common source of errors in programming. 
* If needed, instead, you can always assign them by basting.  
* Casting looks like this example: 
```
val i: Int = b.toInt() 

```
* Kotlin supports underscores in numbers 
* this is so you can specify long constants in a format that makes sense to you 
* examples: 
```
val oneMillion = 1_000_000
val socialSecurityNumber = 999_99_9999L 
val hexBytes = 0xFF_EC_DE_5E 
val bytes = ob11010010_01101001_10010100_10010010 
```

### Nullability: 
* "Really Kotlin" 
* Kotlin helps avoid null pointer exceptions 
* when you declare a variable's type explicity, then by default its value cannot be null. 
```
var rocks : Int = null 
error: null can not be a value of a non-null type Int
var rocks : Int = null 
```
* use the question mark operator to indicate that a variable cann be null. 
```
var marbles : Int? = null 
```

### Complex Data types 
* such as a list 
* you can allow for the list to be null 
* but if the list is not null, its selements cannot be null 
* or you can allow both the list or the elements to be null 
``` Examples: 

var lotsOfFish: List<String?> = listOf(null, null) 
var everMoreFish: List<String>? = null 
var definitelyFish : List<String?>? = null 
definitelyFish = listOf(null, null) 
```

Really love no pointer exceptions?  
Kotlin will let you keep them 
How?  
Use the "not null" assertion operator
it forces your way past a nullable type 

Example: 
```
goldfiesh!!eat()
```

however, this will still throw an exception when it is null. 

### PROGRAMMING SLANG:  
* An Excelamation Mark is called BANG 
* [Bang Wiki Article](https://en.wikipedia.org/wiki/Exclamation_mark#Computers)
* Double bang is easier to say than "not null" but it means the same as !! 
* generally it is a bad idea to use the double bang operator 


Check if a variable is non-null before accessing one of its methods 
This saves time 
```
return fishFoodTreats?.dec() ?: 0 
```
Meaning: "If fishFoodTreats is not null, remove one treat and return the new value, or otherwise return the value after the colon, which is zero." 

if it is null, we stop the evaluation so that the dec (decrease function) is not called on a null object. 

Elvis Operator:  ``` ?: ``` 
* it looks like a smilely on its side


## 2.4 Operators Quiz: 
Select all of the statements below written with correct syntax. There may be more than one correct answer. Try them in REPL.

``` 
val address : String = null 

val amount : Double? = 10.0  

var list:  List<String?>? = listOf(null, null) 

list?.size
```
all but line 1 are correct kotlin syntax 


## 2.5 [Building the Aquarium](https://classroom.udacity.com/courses/ud9011/lessons/605a8cec-a22b-4778-a682-39b35cf8467b/concepts/4b9f4745-ca94-4436-876a-1a0e3ecb963b) 
no new content--just view of how far we've come in our knowledge base towards building an acquarium 

## 2.6 [Practice Quiz](https://classroom.udacity.com/courses/ud9011/lessons/605a8cec-a22b-4778-a682-39b35cf8467b/concepts/336fff8c-1cab-4243-92b0-384d8493080b)

Practice Basic Operations in Kotlin

When it comes to basic operations, it's a good thing for this to become automatic, something less to think about while you are trying to figure out the solution to your actual programming challenge. There is only one road to automaticity, and that's practice. The following are some starting points for playing in REPL with the operations and concepts introduced in this lesson.
Practice Time: Basic Operations

Solve the following using the operator methods in one line of code.

If you start with 2 fish, and they breed twice, producing 71 offspring the first time, and 233 offspring the second time, and then 13 fish are swallowed by a hungry moray eel, how many fish do you have left? How many aquariums do you need if you can put 30 fish per aquarium?

    Hint: You can chain method calls.
    Hint: You can call the methods on numbers, and Kotlin will convert them to objects for you.
    Bonus question: What is special about all the numbers of fish?
    
![Image2.6-basic-operators](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.6-basic-operators.jpg)    


Practice Time: Variables

    Create a String variable rainbowColor, set its color value, then change it.
    Create a variable blackColor whose value cannot be changed once assigned. Try changing it anyway.

![Image2.6-color-practice](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.6-colors-variable-practice.jpg)  


Practice Time: Nullability

    Try to set rainbowColor to null. Declare two variables, greenColor and blueColor. Use two different ways of setting them to null.

![Image2.6-null-practices](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.6-null-practice.jpg)  

Practice Time: Nullability/Lists

    Create a list with two elements that are null; do it in two different ways.
    Next, create a list where the list is null.
    
![Image2.6-list-practice](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.6-list-practice.jpg)  


Practice Time: Null Checks

    Create a nullable integer variable called nullTest, and set it to null. Use a null-check that increases the value by one if it's not null, otherwise returns 0, and prints the result.

Hint: Use the Elvis operator. [reminder: elvis operator is ?:]

![Image2.6-elvis-practice](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.6-elvis-practice.jpg)  

## 2.7 Strings 
* Kotlin has strings
* they work pretty much like strings do in any other language 
* concatenate with PLUS + 
* you can use string templates to use with strings 
* the dollar value name is replaced by the string text representing its value 
* Example of: 
  Template: "I have $numberOfFish fish and $numberOfPlants." 
  Ouptut: I have 5 fish and 12 plants. 
* You can also do this: 
```
Template Example Code: "I have $(numberOfFish + numberOfPlants) fish and plants." 
Output of above code: I have 17 fish and plants. 
```
in the above code example, the two variable numbers get added before being output 
* Boolean data type and operators 
* two equal signs equals a value comparison in Kotlin 
* likewise greater than, smaller than, equal to, not equal to etc 
* now we can test for conditions:  ``` if else and when```
* if else is for comparing values 
* you can use ranges 
* ```when``` is Kotlin's way of doing switching.  
* you can also nest all of these in one another 
* [Kotlin Language Documentation](http://kotlinlang.org/docs/reference/)
* [Kotlin Koans](https://try.kotlinlang.org/#/Examples/Hello,%20world!/Simplest%20version/Simplest%20version.kt)

![2.7-examples of above concepts](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.7-ranges-conditionals-ifelse-when.jpg) 

## 2.8 Quiz: Strings 
* This lesson's assignment was to read some code and reply what the outcome was
* I did that.  
* Then I checked it by running it 
* typing and running practice. 

![Lesson2.8 image](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/images/L2.8.jpg) 

## 2.9 Quiz: Practice Time 
* Do the Following Tasks in REPL: 
* Practice time: 
  1. Create three String Variables for trout, haddock, and snapper 
  2. use a tring template to print whether you do or do not like to eat those kinds of fish. 

* Practice Time: 
when statements in Kotlin are like case or switch statements in other languages.

Create a when statement with three comparisons:

    If the length of the fishName is 0, print an error message.
    If the length is in the range of 3...12, print "Good fish name".
    If it's anything else, print "OK fish name".

* NOTES: because i'm using the REPL over and over again, it gets junked up / off screen in length.  
* while you can just close the window and reopen it via Tools->Kotlin->REPL
* i also found you can use the onscreen (in the REPL) tools 
* you can also end up with more than one "tab" open and need to close them to find your code 

## 2.10 [Arrays and Loops](https://classroom.udacity.com/courses/ud9011/lessons/605a8cec-a22b-4778-a682-39b35cf8467b/concepts/d66ed4d8-83bf-4017-82ef-98c3868248c1)
* [Kotlin Language Documentation](http://kotlinlang.org/docs/reference/)
* [Kotlin Koans](https://try.kotlinlang.org/#/Examples/Hello,%20world!/Simplest%20version/Simplest%20version.kt)
* 


## 2.11 Quiz: Arrays and Loops 

## 2.13 Lesson 2 Summary
* Resource:  Learn Kotlin by Example: https://play.kotlinlang.org/byExample/overview  
