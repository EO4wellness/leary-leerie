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

* 

## 2.4 Operators Quiz: 

## 2.5 Building the Aquarium 

## 2.6 Quiz

## 2.7 Strings 

## 2.8 Quiz: Strings 

## 2.9 Quiz: Practice Time 

## 2.10 Arrays and Loops 

## 2.11 Quiz: Arrays and Loops 

## 2.13 Lesson 2 Summary

