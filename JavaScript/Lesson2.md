# Lesson 2: [Data Types & Variables](https://classroom.udacity.com/courses/ud803/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/673e1be5-6c85-4397-8318-192d95d48761)
* In this lesson, we learn to represent real-world data using JavaScript variables, and distinguesh between the different data types in the language. 

      2.1 Intro to Data Types 
      2.2 Numbers 
      2.3 Comments 
      2.4 Quiz: first Expression 
      2.5 Stings 
      2.6 String Concatenation 
      2.7 Variables 
 
# Course Notes:

2.1 Intro to Data Types 
* Data is everywhere. 
* Data helps us understand the world, make future decisions, help us organize information.  
* Data in coding is important too. 
* Information being gathered. 
* What are types in JavaScript. 
* In this lesson, we learn how to define and manimpulate the primitave data types in JavaScript.
* Types of Data: Numbers, Strings, Booleans, Undefined, and Null. 

2.2 Numbers 
* Defining numbers (a data type) in JavaScript is fairly simple. 
* The NUMBER data type includes any positive or negative integer. 
* Decimals are also within the NUMBER data type. 
* Entering a number into the JavaScript console will return it back again to you.  
* Arithmetic Operations: type out any expression in the way you would type in a calculator. 
* Example within the JavaScript Console

            3 + 2.1 
            
            Returns:
            5.1

            QUIZ: 
            
            1. Enter the expressions (one at a time) into the console and determine what each expression evalutes to: 
            
            2 + 10 - 19 + 4 - 90 + 1  --> returns  -92
            
            -20 + -19 - (-10) - (-1) + 24 --> returns -4 
            
            (10/5) * 4 -20 --> returns -12
            
            4096 % 12 --> returns 4
            
* Comparing Numbers - you can compare two numbers to see if one's greaer than, less than, or equal to the other. 

            5 > 10 --> returns false 
            
            5 < 10 --> returns true 
            
            5 == 10 --> returns false 
            
* Comparisons between numbers will always return either "true" or "false" they don't return any other types of answers. 
*  Operator and its Meaning Chart 

                  <   Less than 
                  >   Greater than 
                  <=  Greater than or Equal to 
                  >=  Greater than or Equal to 
                  ==  Equal to 
                  !=  Not Equal to 
                  
                  
                  QUIZ: 
                  Enter each express below, one at a time, into the JavaScript Console and determine what each expression evaluates to.
                  
                  43 > 47 --> False 
                  
                  12==17 --> False 
                  
                  3 <=3 --> True
                  
                  1!=0 --> True 
                  
* TIP: The values true and false have significant importance in JavaScript. These values are called Booleans and are another data type in JavaScript. Later in this lesson, you’ll learn more about why Booleans are so important in programming.


2.3 [Comments](https://classroom.udacity.com/courses/ud803/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/6a4bec50-7caf-4b8b-9685-a4e24346cda0) 
* simple code is easy to read and easy to understand. 
* it is meant to be used/understood by the computer (a machine)
* but people (coders, debuggers, etc) need to read it too
* the more complex the code, the harder and harder it is for people to read it and understand it.
* people use comments to help people read the code and understand what it does 
* comments can be done in two formats within JavaScript

            Single Line Comments in Javascript:
            
            // Any text here would be a comment in JavaScript 
            
            or
            Multiple Line Comments in JavaScript: 
            
            /*
            multiple lines 
            of comments 
            would be typed like this
            within Javascript
            */
            
* Comments are not executed by JavaScript so you can write what you want, but it should be user friendly to read             
* JavaScript comment terminology:

                   double forward-slash //
                   
                   Anything written on the same line after the // will not be executed 
                   
                   To have the comment span multiple lines, mark the start of your comment 
                   with a forward-slash and star, and then enclose your comment inside 
                   a star and forward-slash /* … */.
                   
2.4 Quiz: first Expression 

Directions:

Write an expression that uses at least 3 different arithmetic operators.

The expression should equal 42.

Hint: +, -, *, /, and % are possible arithmetic operators

                  /*
                  * Programming Quiz: First Expression (2-1)
                  * Write an expression that uses at least three, distinct, arithmetic operators
                  * to log the number 42 to the console.
                  */
                  
                  /*
                  * QUIZ REQUIREMENTS
                  * 1. Your code should print the value `42`
                  * 2. You should use at least 3 distinct operators. (`+`, `-`, `*`, `/`, or `%`)
                   * 3. Your code should not be empty
                   */
                   
                   // this expression equals 4, change it to equal 42
                   console.log(1 + 5 - 2);
                   
                   
                   Course Solution : 
                   
                   console.log(10 * 4 + 4 - 2);
                   


2.5 Stings 
* String Data Type 
* strings can be single letters like the character H 
* strings can be numbers or letters 
* strings are signified by quotes. 
* it doesn't matter if your string uses single quotes or double quotes

                  Example:

                  'single quote string' 
                  
                  "double quote string" 
                  
                 
* the quote type you use, do have to match (so either use all double quotes or use all single quotes but dont mix them up) 
* if you try to pass a string to consule, but forget to use the quotes, Console returns an error. 
* if you get an [error message](#) in your JavaScript, you will likely see a hint about what's wrong with it.  
* most bowsers with developer features have tips on debugging error messages such as: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined 
* TIP: It is correct to either use double " or single ' quotes with strings, as long as you're consistent. The [JavaScript Udacity style guide](http://udacity.github.io/frontend-nanodegree-styleguide/javascript.html) for labs and projects suggests using single quotes to define string literals.

2.6 String Concatenation 
* strings are a collection of character data enclosed in a set of double or single quotes.
* strings are best used to represent data like: sentences, names, addresses, email addresses and more. 
* you can add strings together. 
* when adding two (or more) strings together, it isn't mathematical adding
* Javascript calls it Concatenating (combining, non-mathematically, two or more strings)
* Concatenation of Strings:

                  Example:
                  
                  "Hello, "   + "New York City!" 
                  
                  Returns: Hello, New York City!
* later in the course, we will find concatenation with strings other than by using the addition operator but for now we are just looking at + operator. 

QUIZ: 

                  1.  What's the result with "hello" + "world"?
                  
                  My Answer: "helloworld"
                  
                  "If you want to have a space in between two words, you need to explicitly add a space! It will not be added automatically for you."
                  
                  
                  
                  2. What do you think will happen when you type "Hello + 5*10" into the JavaScript console? 
                  
                  My Answer: "Hello + 5*10"
                  
                  "You might have thought that an error would happen. But, remember that strings can be any collection of characters that are surrounded by quotation marks. The + 5*10 are just characters inside the quotation marks, so the interpreter will assume the whole object is a string, and output the result as a string!

                  "Hello + 5*10"

                   output: "Hello + 5*10"
                   
                   
                   3. What do you think will happen when you type "Hello" + 5*10 into the counsole?
                   
                   My Answer:  "Hello50" 
                   
                   You've just discovered some peculiar behavior in JavaScript. It’s called implicit type coercion and it's a feature of JavaScript. JavaScript multiplies the 5*10 to become 50 and then changes the number 50 into the string "50", so you're adding together the same data type. This then gets combined with the string "Hello". You'll learn more about why this happens later in this lesson.



2.7 Variables 
* all of the examples we have looked at previous to now in this course, have been for one time use. 
* we've used the string, printed it, or printed the math results, and then it is gone.  
* we aren't using it again and again. 
* to do that, we need a way to store data. 
* we store data into a variable so it can be used over and over again 
* unlike in math, JavaScript variables can store ANY data into a variable. 
* to create a JavaScript variable use the following syntax:

            var (variable name) (assignment opperator) 
            
 * note: the assignement operator is the equals sign. 
 
            // Examples: One time Use of Strings:

            "Hello"; // Here's a String "Hello"
            
            "Hello" + " World"; // Here's a new String (also with the value "Hello") concatenated with " World"
            
            
            // Examples: Storing as a variable-its like packing it away for later. 
            
            var greeting = "Hello";
            
            Now, if you want to use "Hello" in a variety of sentences, you don't need to duplicate "Hello" strings. You can just reuse the greeting variable. 
            
            greeting + " World!";
            
            Returns: Hello World!
            
            greeting + " Mike!";
            
            Returns: Hello Mike!
 
 * You can also change the start of the greeting by reassigning a new string value to the variable greeting.
 
                  Example Reassigning 
                  
                  greeting = "Hola"; 
                  greeting + " World!";
                  
                  Returns: Hola World! 
                  
                  greeting + " Mike!";
                  
                  Now Returns: Hola Mike!
 
* Naming conventions  

            Variables are named using camelCase 
            
            camelCase means the first word is LOWER case and the following are upper) 
            try to use variable names that succinctly & accurately describe the data 
            
            var totalAfterTax = 53.03; // uses camelCase if the variable name is multiple words
            var tip = 8; // uses lowercase if the variable name is one word
 
* Not using camelCase for your variables names is not going to necessarily break anything in JavaScript. But there are recommended style guides used in all programming languages that help keep code consistent, clean, and easy-to-read. This is especially important when working on larger projects that will be accessed by multiple developers.  
* Read [Google's JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html) here. 
 
                  Quiz: which of these are good variable names? 
                  
                  [1] var thingy =1;
                  
                  [2] var count =1;
                  
                  [3] var postLiked = false; 
                  
                  [4] var firstname = "Richard";
                  
                  My anwswers: 
                  
                  [1] is not a good variable name as it isn't descritive or succinctly describing the type of data it contains. 
                  
                  [2] is a good variable name if what you are doing is counting things.
                  
                  [3] this is a good variable name if it is storing a boolean data type 
                  
                  [4] this variable name isn't using camelCase or it would be a good variable for holding this string. 
                  
                  
                  Their response about my answers:  The variables count and postLiked use lowercase and camelCase appropriately. The postLiked variable has a descriptive name about what it represents. The count variable is questionable and would depend on its surrounding context. If the count variable was supposed to track the number of items in a catalog, then a more descriptive name like catalogCount might be more appropriate. As for the other variables, thingy is a vague name that doesn't really describe what 1 is the value for and firstname should be in camelCase.

2.8 [Quiz: Converting temperatures](https://classroom.udacity.com/courses/ud803/lessons/74007e2e-2a0a-4de3-a8a6-5c2ec4275773/concepts/5f0a00eb-e0c7-4b3f-a24d-400cad12176e)
* Given the formula to covern C into F and what you know about JavaScript; write JS to covert and display what 12 degrees C is in F.
* F=C×1.8+32
* NOTE: the Udacity classroom uses an interface that embeds a JavaScript enviroment into the course work.  I discovered this specific coding interface within the JavaScript Udacity course, displays a TINY (Hard to see) red X at the "lines of code" portion of any code entered into the display.  So even before running the code, you can visually see errors and the hints to resolve the errors.  

                  Example:
                  
                  Type F=Cx1.8+32 into the Udacity interace
                  
                  the line of code next to the above entry will turn red with an x over the number 
                  
                  reason being in JavaScript multiplicatin is * where as x is a variable 
                  
* [Code at W3Schools](https://www.w3schools.com/code/tryit.asp?filename=GNK50QYUYRFE)
                  
2.9 String Index
* You can access individual characters within a string.
* any given characters location within a string is called its INDEX.
* the INDEX for the first character of any string is ZERO 0
* INDEX are indicated inside square brackets
* the INDEX format is [number]
* this INDEX formating is placed right after the string. 
*  For Example:  If you wanted to find the first character stored in a specific string of "James" you would do so in code by typing the following:

                  Example: Find first character in string
                  
                  "James"[0];
                  
                  returns:  "J" 
                  
* More comonly you'd see it with a variable 
                  
                  Example: 
                  
                  var name = "James";
                  name[0]
                  
                  This code returns "J" 

* Characters within a string are indexed starting from 0, where the first character is at position 0, to n-1, where the last character is at position n-1 (n represents the total number of characters within a string).

            Quiz: What character will be printed to the JavaScript console after running the following lines of code? 
            
            CODE:
            
            var quote = "Stay awhile and listen!";
            console.log(quote[6]);
            
            My Answer: w 
            
            Alternatively, you can use the String’s charAt() method to access individual characters. For example, quote.charAt(6) would also return "w". You’ll learn more about methods later in this course.

2.10 Escaping Strings
2.11 Comparing Strings 
2.12 Quiz: Favorite Food 
2.13 Quiz: String Equality for All
2.14 Quiz: All Tied Up 
2.15 Quiz: Yosa Buson 
2.16 Booleans 
2.17 Quiz: Facebook Post 
2.18 Null, Undefined, and NaN
2.19 equality 
2.20 Quiz: Seminolons! 
2.21 Quiz: What is my Name?
2.22 Quiz: Out to dinner
2.23 Quiz: Mad libs
2.24 Quiz One Awesome Message 
2.25 Lesson 2 Summary 
 

NAV: [ReadMe](https://github.com/EO4wellness/leary-leerie/tree/master/JavaScript) | [Lesson 1](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson1.md) | [Lesson 2](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson2.md) | [Lesson 3](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson3.md) | [Lesson 4](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson4.md) | [Lesson 5](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson5.md) | [Lesson 6](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson6.md) | [Lesson 7](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson7.md)
