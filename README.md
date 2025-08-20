# Pong But Epilepsy

This project is called Pong But Epilepsy.   
It is my (third/fourth) submission for Hack Club's Athena Award.   
As the name suggests, this project is designed to be a chaotic pong game with a variety of wacky features. 
Play the game to find out how it works, but be warned that there will be some epilepsy-inducing elements!  
__________________________________________________________
What it is
-
This Python project is a fun game featuring many different technical elements and game modes. Here's a breakdown of the game:
__________________________________________________________
Personal Project Evaluation and Reflection
-
I decided to make this project for a fun technology week competition at my school. The theme of the competition was "chaos". Since my projects weren't usually silly, I was sort of stumped on what to do. Eventually, a friend of mine (also participating in the game competition) suggested to give the viewer epilepsy by switching the background colors constantly and by using a wide range of sounds. Genius. Because of this, I decided to create a simple pong game, but with an epilepsy factor. Simple, yet absolutely wacky. Also, I recently learned how to create games using Pygame, so I used it to make my project. Due to the limited time participants had to create their games for the competition, I only managed to add the main epilepsy factor and working pong game elements. At some point after the competition, I found the unfinished game sitting in my computer files. So, I chose to complete it and present the complete version of Pong But Epilepsy, which included a functional game menu and toggles. 
__________________________________________________________
This project was made by using the coding language Python and many different Python Libraries.
 
* Python: The coding language used to make this project.   
* PyGame: The primary Python Library used for this project. This library helped in creating the main structure of the pong game. It allowed for me to display various sprites on the game's screen, as well as creating physics for the objects created.  
* Sys (System): Python module used for interacting with Python runtime environment. Also helped in debugging the code.
* Random: The Python module used for areas involving randomising. In my project, I used it to generate random RGB colors to contribute the "epilepsy" effect in my game. Also, I used the "random.choice" function to set random speeds for the ball with each rebound, just to make it extra chaotic and unpredictable!
* Time: Python library which, as the name states, is a library to do with time. Specifically, I used the "Sleep" function, which helped for count-downs to begin the game. 
__________________________________________________________
While making this project, I was faced with different challenges.   
* Challenge 1: Creating the physics of the game elements: paddles and balls. This was probably one of the most difficult parts of the project. Pygame doesn't come with its own physics, unlike other game development platforms such as Unity. I used some if/else loops to let the ball change direction when certain criteria (e.g. if the top of the ball touches the top of the screen) was met. 
* Challenge 2: Small bug I had to fix. Occasionally, the ball wouldn't rebound properly off the top and bottom, and would disappear. I found the reason for this bug was because of an inaccuracy in some of my random.choice functions. Originally, when the ball touched the top of the screen, the ball had the possibility to move in a positive or negative gradient, which would cause the ball to ocassionally disappear off the screen. To fix it, I removed the positive gradients for when the ball touched the top of the screen, and vice-versa for when the ball touched the bottom of the screen.

I think through the creation of this project _____
__________________________________________________________
Project Stats
-
* Time spent: __hrs __ mins
* Code editor used: VS Code
* Coding language(s): Python
__________________________________________________________
Contact Information
-
Please email **audrey.shi108@gmail.com** for any inquiries, or message **AudreyS108** on Slack. :D
