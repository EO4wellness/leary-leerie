# [Kotlin Bootcamp for Programmers](https://www.udacity.com/course/kotlin-bootcamp-for-programmers--ud9011)
by Google 
* Udacity has a free course for learning Kotlin. https://www.udacity.com/course/kotlin-bootcamp-for-programmers--ud9011 
* this course is broken into six lessons

## Lesson 1: Intro
* intro 
* Instructors: Sean McQuillan (Google Kotlin Expert) and Alex (training and software developer for Google) 
* install Intellij
* IDE used in course 
* outline of benefits 
* [Android Developers Blog Announcing Kotlin](https://android-developers.googleblog.com/2017/05/android-announces-support-for-kotlin.html)
* [Install JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html) if you don't have it
* [Install IntelliJ](https://www.jetbrains.com/help/idea/install-and-set-up-product.html)
```
Install the JDK (for Windows)

Run the downloaded installer (e.g., jdk-10.0.x_windows-x64_bin.exe), which installs both the JDK and the JRE.

By default, the JDK will be installed in the directory "C:\Program Files\Java\jdk-10.0.x", where x denotes the version number; and the JRE in "C:\Program Files\Java\jre-10.0.x".
```
* Add the JDK installation path to PATH (Windows only) 
* Windows searches the current directory and the directories listed in the PATH environment 
* variable (system variable) for executable programs.
```
    Open "Control Panel" -> "System" -> "Advanced system settings" -> "Environment Variables".
    Under "System variables", scroll down to select "Path" and click "Edit...".
    Append to the existing Path value a semi-colon ";" then the JDK's "bin" directory (e.g. ";C:\Program Files\Java\jdk-10.0.0\bin").
```
* More info on IntelliJ setup: https://www.jetbrains.com/help/idea/install-and-set-up-product.html 

```
Verify IntelliJ Installation

Check that your IntelliJ is installed and up-to-date by following these steps below:

    To check whether you need to install JDK, in a terminal window, type:

    java -version
    javac -version

    If you do not have it, or do not have the latest version, download and install JDK.
    Install IntelliJ. This course uses IntelliJ and we recommend you use the same IDE.
    Start IntelliJ.
    Install any updates and additional content you are prompted for.
    Select IntelliJ IDEA -> Check for updates… until there are no more updates.


```
* [Installation tips and first Code](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/Installation.md)

## Lesson 2: [Kotlin Basics](https://github.com/EO4wellness/leary-leerie/blob/master/Kotlin/lesson2.md)
* use the kotlin interpreter 
* get comfortable with the basic features 
* write kotlin statemetents 
* write kotlin expresssions 
* practice using operators 

## Lesson 3: Functions 
* Create functions 
* call functions 
* default or variable arguments 
* pass functions as arguments to filders or lambdas 

## Lesson 4: Classes 
* how object-oriented programming in Kotlin 
* build private classes 
* built public classes 
* abstract classes
* interfaces 
* understand data classes 
* understand special purpose classes 
* PUN: this is the class for everything class 


## Lesson 5: Kotlin Essentials: Beyond the Basics 
* more advanced features 
* pairs 
* annotations
* extension functions 
* understand constants 
* collections
* generics 

## Lesson 6: Functional Manipulation 
* which looks at lambdas and higher-order functions in Kotline 
* learning to write inline functions 
* learn single abstraction method interfaces (SAM) 
