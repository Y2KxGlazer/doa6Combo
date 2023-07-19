# Each html file has it's own unordered list. that has the names of the class
import os
import requests
import re
from bs4 import BeautifulSoup

#TODO: get the table data and save it to another file.

os.chdir("Character Data")
char_list = os.listdir() # names of the folders

downloaded_files = {}

for i in char_list:  # i is name of character
    try:
        os.chdir(i)
        moves_file = i + " Moves"
    except NotADirectoryError:
        continue


    # Read file
    with open(moves_file+".html", "r", encoding="utf-8") as file:


    # get table data
        html = file.read()
        soup_html = BeautifulSoup(html, "html.parser")
        move_list = soup_html.find_all("table")

    for table in move_list:
        icons = table.find_all('a', class_="image")
        for icon in icons:
            link = icon['href']
            title = icon['title']
            response = requests.get(link)
            if response.status_code == 200:
                if title in downloaded_files:
                    # Handle duplicate titles
                    print(f"Skipping duplicate title: {title}")
                    continue

                # Sanitize the title to remove invalid characters
                sanitized_title = re.sub(r'[\/:*?"<>|]', '_', title)

                # Add the link to the hashmap
                downloaded_files[sanitized_title] = link

                # Extract the file name from the URL
                file_name = f"{sanitized_title}.png"

                with open(file_name, 'wb') as file1:
                    file1.write(response.content)

                print(f"Image downloaded successfully as {file_name}.")
            else:
                print("Failed to download the image.")

    print(i + " is done.")
    os.chdir(os.getcwd() + "/../..")

print("Task Completed!")




    # check if icons in dict

    # if not, get images

    # append to dict

    # download icons from dict

    # save them in cmdIcons



# TODO: Still need the icons, make a dict that
# TODO: appends 'key' links(to the icon image), 'value' images saved on disk.
# TODO:

