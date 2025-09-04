# Pong But Epilepsy

[![Athena Award Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Faward.athena.hackclub.com%2Fapi%2Fbadge)](https://award.athena.hackclub.com?utm_source=readme)  
This project is called Pong But Epilepsy.   
It is my third submission for Hack Club's Athena Award.   
As the name suggests, this project is designed to be a chaotic pong game with a variety of wacky features. 
Play the game to find out how it works, but be warned that there will be some epilepsy-inducing elements!  
__________________________________________________________
What it is
-
This Python project is a fun game featuring many different technical elements and game modes. Here's a breakdown of the game:

* A simple pong game where you try to score points by using paddles to deflect the ball into the opponent's goal. 
* Different gamemodes: Normal mode and Epilepsy/Chaos mode. Epilepsy mode is like Normal mode, except the fact it is extra chaotic. Includes flashing lights as well as flipped controls (just to make the player rage even more. >:D)
* Options for Singleplayer or multiplayer mode (for more variety!!)
* Random silly sounds to add to the chaos. 
__________________________________________________________
How To Operate
-
1. Go to the "Releases" section and select "App ver. of Pong But Epilepsy"  
2. Download all of the files there, and place them in a folder called "dist" in "Documents"
3. After the download, open the file and a terminal should pop up after a while. Soon, the main menu of the game will appear!   
Note that closing the terminal which pops up with the game will cause the application to close.

 **Alternate operating methods (only if above method fails!)** 
<details>
<summary>Click to open!</summary>

1. Press the green "Code" button. Select "Local" and then "Download ZIP"
   
> ![Step1](https://github.com/user-attachments/assets/f273659e-e287-4748-b895-fa7923775d2d)

2. Unzip/extract the downloaded ZIP folder
   
3. Follow these steps:
 
> Open VS Code, then through VS Code, open the unzipped/extracted folder, click in till you find "pong-but-epilepsy.py", and open that file.
> In the terminal, input the following code:

> ```pip install pygame```    
> ```pip install sys```    
> ```pip install random```    
> ```pip install time ```  

> (These commands are used to install the needed Python Libraries in order for the code to run as it should.)
> You can now play the game! Run the code with the Python Debugger (keyboard shortcut Control + F5). A pygame window should pop up. Enjoy the fun! :P 
> <img width="1857" height="943" alt="Screenshot 2025-09-04 145625" src="https://github.com/user-attachments/assets/6d5b6933-c31d-4092-ae5d-92edc85a27ea" />

</details>  

__________________________________________________________   
Personal Project Evaluation and Reflection
-
I decided to make this project for a fun technology week competition at my school. The theme of the competition was "chaos". Since my projects weren't usually silly, I was sort of stumped on what to do. Eventually, a friend of mine (also participating in the game competition) suggested to give the viewer epilepsy by switching the background colors constantly and by using a wide range of sounds. Genius. Because of this, I decided to create a simple pong game, but with an epilepsy factor. Simple, yet absolutely wacky. Also, I recently learned how to create games using Pygame, so I used it to make my project. Due to the limited time participants had to create their games for the competition, I only managed to add the main epilepsy factor and working pong game elements. At some point after the competition, I found the unfinished game sitting in my computer files. So, I chose to complete it and present the complete version of Pong But Epilepsy, which included a functional game menu, different game modes, and silly music + sound effects. 
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
* Challenge 3: Creating the menu screens. After some research and some trial and error, I found the best way to accomplish this was by making each "screen" a seperate python function, and called each function when a certain button was pressed. I had 4 seperate screens branching off from the main menu: Normal mode, Epilepsy mode, Bot normal mode, Bot Epilepsy mode, How to play, and Quit. 
* Challenge 4: Creating a bot "AI" for singleplayer mode. This wasn't exactly an "AI", but instead just a few if/else statements controlling the paddle movement. If the ball was higher than the bot paddle, the bot would move up, and vice versa if the ball was lower. 
* Challenge 5: Adding music and sound effects. I did this by utilizing Pygame's built-in mixer function. By using different mixer channels, I could overlap background music and sound effects simultaneously!

I think through the creation of this project, I have learned to use a variety of different Python Libraries successfully (especially Pygame), as well as creating simple algorithms and functions. Additionally, I learnt how to create my own physics in Pygame, and play music using the Pygame sound & music mixer.  
__________________________________________________________
Project Stats
-
* Time spent: 12 hrs 7 mins
* Code editor used: VS Code
* Coding language(s): Python
__________________________________________________________
Contact Information
-
Please email **audrey.shi108@gmail.com** for any inquiries, or message **AudreyS108** on Slack. :D
