# use the files and scrape the wiki
import os
import requests
# base cwd is doa6combo

# get the files

os.chdir('Character Data')
for i in os.listdir():
    os.chdir(i)
    # should change to the character folder

#read txt file
    with open(i + ".txt", "r") as url_file:
        url = url_file.read().strip()


    page_html = requests.get(url)

    # save html data to file
    with open(i + " Moves.html", "w", encoding="utf-8") as f:
        f.write(page_html.text)

    # go back a folder
    os.chdir('..')



