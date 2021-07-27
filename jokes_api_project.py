# Simple python program to create an API to randomly generate a dad joke using a given keyword
# Modules like 'termcolor' and 'pyfiglet' have been used to modify the display text  


# Importing required modules
from termcolor import colored
from pyfiglet import figlet_format
import requests
from random import randint

# Setting up initial display text 
text = 'Dad Jokes 101 !'
formatted_text = figlet_format(text) # Converting text into cool text
col_text = colored(formatted_text,color='cyan',attrs=['bold']) # Giving color and bold attribute to the cool text
print(col_text)



topic = input('Let me tell you a joke! Give me a topic:') # Taking a keyword as an input from the user


url = 'https://icanhazdadjoke.com/search' # URL of the jokes site
req = requests.get( 
                    url,
                    headers = {'Accept':'application/json'}, # Giving get request with certain search parameters
                    params={'term':topic}
                  )

jokes_dict = req.json() # Returns JSON format response equivalent to a dictionary in python
jokes_list = jokes_dict['results'] # Getting jokes list from the dictionary using key-value pair  
tot_jokes = jokes_dict['total_jokes'] # Total jokes containing entered keyword 

if (tot_jokes == 0):
    print(f'Sorry I have no jokes about {topic}. Please try again!')
elif (tot_jokes == 1):
    print(f"I've got one joke about {topic}. Here it is:")
    print((jokes_list[0])['joke'])  # Printing out the only joke as a text
else:
    print(f"I've got {tot_jokes} jokes about {topic}. Here is one:")
    joke_index = randint(0,tot_jokes-1) # Generating a random int for joke_list index
    print((jokes_list[joke_index])['joke']) # Printing a random joke