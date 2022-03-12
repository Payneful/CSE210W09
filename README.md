# CSE210W09
Cycles Game!

Cycles is a game where players try to force each other to crash into their growing tails. The game ends once one player crashes and the other is declared the winner!

Running the Game
You need to have Python 3.8.0 or newer installed and running. 
Open the root folder (CSE210W09) in a terminal. To play the game, 
copy and paste the following command into the terminal:

python3 __main__.py
If that fails, try:

py __main__.py


Project Structure
The project files and folders are organized as follows:

root                    (project root folder)
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