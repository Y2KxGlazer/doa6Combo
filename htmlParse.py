# Each html file has it's own unordered list. that has the names of the class
import os
from bs4 import BeautifulSoup

#TODO: get the table data and save it to another file.

os.chdir("Character Data")
char_list = os.listdir() # names of the folders

for i in char_list:  # i is name of character
    os.chdir(i)
    moves_file = i + " Moves"


    # Read file
    with open(moves_file+".html", "r", encoding="utf-8") as file:


    # get table data
        html = file.read()
        soup_html = BeautifulSoup(html, "html.parser")
        move_list = soup_html.find_all("table")

        for move in move_list:
            print(move)

    os.chdir(os.getcwd() + "/..")
    # display table


# TODO: Still need the icons, make a dict that
# TODO: appends 'key' links(to the icon image), 'value' images saved on disk.
# TODO: 

