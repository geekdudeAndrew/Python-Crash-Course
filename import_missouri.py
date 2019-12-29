""" 8-16 page 159 in pdf
Importing Modules
Imports a module holding the function for searching to see if a city you
named is in missouri (that I made for chapter excercise 8-2) in various 
ways. also imports the game request module. I probalby should
funcitonafy more of my code and then put them into modules so this code 
can have more modules to import.
"""

import missouri
from missouri import in_missouri
from missouri import in_missouri as city_search
import pg154_ch8_12_game_request as game_request
#importing a script with code in it runs the code. This is why modules
#only contain functions and not extranious code.
from missouri import *

print("\n")


missouri.in_missouri("Columbia");


