# 1 trellocopy

A python service (linux only for now) that allows you to copy to a trello list and to paste from a trello list.

With only 2 shortcuts (Crtl+Alt+c and Ctrl+Alt+v)
First Crtl+Alt+c and input the name under which you want to save your copy, and press Enter to copy to trello.

After that Ctrl+Alt+v and input the name of your copy and press Enter to paste from trello.

You do not have to be in the term where you started the program, you can copy paste from any window.

# 2 Structure

No structure with maps, so nothing here

# 3.5 Things used

Here is as good a place as any:
https://pypi.org/project/pyperclip/
also counts for the [clipboard](https://pypi.org/project/clipboard/) package

# 3 How to run it

This software depends on `pipenv` how one does `pipenv` one can find here: [pipenv](https://docs.python-guide.org/dev/virtualenvs/)

Get your trello api key and secret and put those in the secrets.py

API_KEY = 'your api key'
API_SECRET = 'your api secret'

make a new bord on trello (or use one you already have)
make a list on your trello board (or use one you already have)
get the ids of the bord and the list [how?](https://community.atlassian.com/t5/Trello-questions/How-to-get-Trello-Board-ID/qaq-p/1347525)

put the ids also in the secrets.py

BOARD_ID = 'id of your board'
LIST_ID = 'id of your list'

after all that you can run ./shortcuts.py (not a service jet, but a good test)

if ll works you can make it a service by installing the trellocopy.service [more info](https://www.shubhamdipt.com/blog/how-to-create-a-systemd-service-in-linux/)

# 4 Class diagram

It is just one script no class dia here.

# 5 Packages used:

`pynput`
`clipboard`
`py-trello`
`pylint`
