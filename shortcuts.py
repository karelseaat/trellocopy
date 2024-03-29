#!/usr/bin/env -S pipenv run python

import os
from datetime import datetime, timedelta
from pynput import keyboard
from pynput.keyboard import  Controller
import clipboard
from trello import TrelloClient
import pytz
from secrets import API_KEY, API_SECRET, BOARD_ID, LIST_ID


os.environ['DISPLAY'] = ':0'
utc=pytz.UTC

pressed = set()


AFTER_KEYS = ""

def get_mylist():
    client = TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
    )
    copyboard = client.get_board(BOARD_ID)
    return copyboard.get_list(LIST_ID)

def on_press(key):
    """on key pressed add key to pressed key list"""
    global AFTER_KEYS
    if key != keyboard.Key.enter:
        AFTER_KEYS += key.char

def on_release(key):
    """on key release return true else return false"""

    if key == keyboard.Key.enter:
        return False

    return True


def capturekeys():
    with keyboard.Listener(suppress=True,on_press=on_press,on_release=on_release) as listener:
        listener.join()



def do_copy():
    """copy selected in copy buffer and put it on trello, after restore buffer"""
    global AFTER_KEYS
    AFTER_KEYS = ""

    mylist = get_mylist()

    backupclipb = clipboard.paste()
    clipboard.copy('')

    keyboardcontroller = Controller()
    keyboardcontroller.press(keyboard.Key.ctrl)
    keyboardcontroller.press("c")

    keyboardcontroller.release(keyboard.Key.ctrl)
    keyboardcontroller.release("c")

    text = clipboard.paste()

    capturekeys()

    mylist.add_card(name = AFTER_KEYS, desc = text)

    clipboard.copy(backupclipb)


def do_paste():
    """get text fro  trello and put it in copy buffer, after that paste it"""
    global AFTER_KEYS

    thecard = None
    capturekeys()

    mylist = get_mylist()

    for card in mylist.list_cards():
        newdate = utc.localize(datetime.now() - timedelta(minutes = 5))

        if card.created_date < newdate:
            card.delete()

        if card.name == AFTER_KEYS:
            thecard = card

    if thecard:
        backupclipb = clipboard.paste()
        clipboard.copy(thecard.desc)
        keyboardcontroller = Controller()
        keyboardcontroller.press(keyboard.Key.ctrl)
        keyboardcontroller.press("v")
        keyboardcontroller.release(keyboard.Key.ctrl)
        keyboardcontroller.release("v")

        clipboard.copy(backupclipb)

    AFTER_KEYS = ""


with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+c': do_copy,
        '<ctrl>+<alt>+v': do_paste,
        }) as h:
    h.join()
