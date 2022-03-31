# CSE210W09
Space Invaders

Space Invaders is a game where enemy ships slowly descend and it is your job to destroy them before they reach the earth. 
Press the space bar to shoott, and use the A and D keys to pilot your ship left and right. 

Running the Game
You need to have Python 3.8.0 or newer installed and running. 
Open the root folder (CSE210W09) in a terminal. To play the game, 
copy and paste the following command into the terminal:

python3 __main__.py
If that fails, try:

py __main__.py


Project Structure
The project files and folders are organized as follows:

SpaceInvaders           (project root folder)
game                    (folder that holds all the classes)
casting                 (folder that holds all the Actor subclasses and parent class)
directing               (folder that holds the Director class)
scripting               (folder that holds the Script class that runs all actions, an 
                         Action parent class, and all the Action subclasses)
sevices                 (folder that holds Keyboard_service class and Video_service class)
shared                  (folder that holds the classes that are shared between: Color class and Point class)
__main__.py             (Builds GUI and starts game)
README.md               (general info)
constants.py            (file that has all the constants that the program will use.)


Required Technologies
Python 3.8.0
Authors
Jake Rammell
Bradley Payne
Codie Snow
Josh Dalton


Audio files for game:
Player laser sounds:
https://freesound.org/people/jeremysykes/sounds/341235/

alien laser?
https://www.the3rdsequence.com/soundb/download/?id=51&ext=ogg

alien death:
https://freesound.org/people/morganpurkis/sounds/394128/
(needs trimmed) https://freesound.org/people/ProjectsU012/sounds/341701/
https://freesound.org/people/qubodup/sounds/442827/
https://freesound.org/people/Jofae/sounds/368511/

player death:
https://freesound.org/people/derplayer/sounds/587174/
https://freesound.org/people/MATRIXXX_/sounds/515005/
https://freesound.org/people/MATRIXXX_/sounds/521105/