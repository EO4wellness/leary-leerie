# Lesson 1: [What is JavaScript](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/Lesson1.md)
* In lesson one, we learn the history of JavaScript, learn to open the JavaScript cosole, and then start wriing code immediately using the JavaScript console. 

      1.1 Intro to JavaScript
      1.2 History of JavaScript 
      1.3 The JavaScript console
      1.4 Developer tolls on Different Browsers
      1.5 Console.log 
      1.6 JavaScript Demo
      1.7 Summary 
      
* Course URL: https://classroom.udacity.com/courses/ud803/
* Course Scope: Introductory level
* Course Delivery: Primarily Video and Text content with quiz and code labs. 

# Course Notes: 
1.1 Intro to JavaScript
* JavaScript was created in 1995 by Brandan Eich.
* Was created to make it easier to add interactive and/or dynamic elements to websites. 
* Since then it has evolved into supporting all kinds of additional uses. 
* Examples given: Programming a robot with Arduino; Writing a game script in Unity. Code editors. 
* Opportunities for the use of JavaScript are limitless. 


1.2 History of JavaScript 
* JavaScript was created in 10 days from the mind of Eich. 
* At the time, he was working on Netscape Navigator. 
* Back in the day JavaScript was created, it was common to use HTML and Java.  
* Java and JavaScript have nothing in common.  They aren't the same at all. 
* Originally, it was called LiveScript but it was changed back to its now "JavaScript" name.
* Competiting versions evolved. 
* This caused the need for an official version of the language. 
* There are version numbers such as ES5 or ES6
* It can also be called "ECMAScript" 
* The current naming includes YEARS such as ES2016, etc. 
* [Read More-History of JavaScript](https://en.wikipedia.org/wiki/JavaScript#History)
* JavaScript is considered one of the 3 pillars of FRONT END web development 

TIP: HTML and CSS are markup languages. Markup languages are used to describe and define elements within a document. JavaScript is a programming language. Programming languages are used to communicate instructions to a machine. Programming languages can be used to control the behavior of a machine and to express algorithms

1.3 The JavaScript console
* To start, for this course, we'll be using the BASIC console inside the developer tools in a browser. 
* The course recommends writing your code, for now, in a text file editor.
* Then, use the web-based console to run your cut-n-paste code from your text editor. 
* This will be too slow and cumbersome for the long haul--but it is an excellent way to start. 
* Also, this is a skill you can use, when you have a live website, which needs edits, to text they work correctly. 
* To access Developer Tools: Right-Click on the page, select "INSPECT"; MAC: Command Option J; WINDOWS: Control + Shift + J 
* works with Google Chrome or other browsers 

To write something in JavaScript (such as your name) make it a string by encasing it in quotes. 

'your-name' 

you can also create an alert window for your browser such as 

'alert("Hello, Friend!  How are you?!");'

[Web Developers Tools](https://developers.google.com/web/tools/chrome-devtools/shortcuts)

1.4 Developer tolls on Different Browsers
* Ever modern browser now includes its own set of developers tools. 
* Google Chrome: CONTROL + SHIFT + I 
* Mozilla Firefox: CONTROL + SHIFT + I 
* Internet Explorer:  F12
* Microsoft edge:  F12
* Safari: have to be enabled and then right-click and inspect 
* Opera: CONTROL + SHIFT + I 

1.5 Console.log 
* debug
* test ideas 
* developer tools-sandbox; no long-term consequences 
* code errors, or warnings, are very common. 

        for (var i = 0; i < 10; i++) {
        console.log(i);
        }
        
 * Browser Console gives the "warning" error message of being careful when cut-n-pasting code into the console. 
 * any code written inside the curl brackets in our example code will be repeated 10 times because we have the "< 10> listed in the code. 

1.6 JavaScript Demo
* JavaScript 

      We've seen how to use 'console.log' to print messages in the console 
      We can use it as a sandbox to text new ideas
      We can use it to debug 
      
 * Example Exercise 
 
        Visit: https://daringfireball.net/projects/markdown/ 
        Open the Developers Console 
        Type: document.getElementsByTagName("h1")[0].style.color = "#ff0000"; 
        
        1.  What happened when you ran that line of code int he JavaScript consule?
        
        MY Answer: The heading changes to red text. 
        
        "Yes! That line of code changes the text in the first <h1> tag to red!" 
        
        
        Refresh the page 
        Now cut-n-paste this code into the console 
        
        
        document.body.addEventListener('click', function () {
            var myParent = document.getElementsByTagName("h1")[0]; 
            var myImage = document.createElement("img");
            myImage.src = 'https://thecatapi.com/api/images/get?format=src&type=gif';
            myParent.appendChild(myImage);
            myImage.style.marginLeft = "160px";
        });
        
        2. What happened?  
        
        My Answer:  An image is added to the page. 
        
        A cat image was added to the page! But this only happened after the page was clicked. 
        Take a moment and let this feeling of power sink in.      
      
1.7 Summary 
* All major browers come with Built-in JavaScript Engines 
* JavaScript Console
* Added styles and animations to a web page. 

NAV: [ReadMe](https://github.com/EO4wellness/leary-leerie/tree/master/Intro-to-JavaScript) | [Lesson 1](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson1.md) | [Lesson 2](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson2.md) | [Lesson 3](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson3.md) | [Lesson 4](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson4.md) | [Lesson 5](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson5.md) | [Lesson 6](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson6.md) | [Lesson 7](https://github.com/EO4wellness/leary-leerie/blob/master/Intro-to-JavaScript/Lesson7.md) | [Code Library](https://github.com/EO4wellness/leary-leerie/blob/master/JavaScript/code%20samples/Readme.md)
