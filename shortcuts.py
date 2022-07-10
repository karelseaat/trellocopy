#!/usr/bin/env -S pipenv run python

import os
os.environ['DISPLAY'] = ':0'
from pynput import keyboard
from pynput.keyboard import Key, Controller
import clipboard
from trello import TrelloClient
from datetime import datetime, timedelta
import pytz


utc=pytz.UTC

pressed = set()

client = TrelloClient(
    api_key='3cd117a524913b8e457893f9fff7b327',
    api_secret='4fa723f0134f1e2970eae1db9aa1c6b9764c0ccab5a9992906cfa2d64d791da2',
)

copyboard = client.get_board('62c57908ee94d77ab6f39383')
aatlist = copyboard.get_list('62c579171436d928d98792ea')

afterkeys = ""

def on_press(key):
    global afterkeys
    if key != keyboard.Key.enter:
        afterkeys += key.char

def on_release(key):
    global afterkeys

    if key == keyboard.Key.enter:

        return False


def capturekeys():
    with keyboard.Listener(suppress=True,on_press=on_press,on_release=on_release) as listener:
        listener.join()

def do_copy_existing():
        global afterkeys
        text = clipboard.paste()
        capturekeys()

        aatlist.add_card(name = afterkeys, desc = text)
        afterkeys = ""


def do_copy():
    global afterkeys

    backupclipb = clipboard.paste()

    keyboardcontroller = Controller()
    keyboardcontroller.press(keyboard.Key.ctrl)
    keyboardcontroller.press("c")

    keyboardcontroller.release(keyboard.Key.ctrl)
    keyboardcontroller.release("c")

    text = clipboard.paste()

    capturekeys()

    aatlist.add_card(name = afterkeys, desc = text)
    afterkeys = ""
    clipboard.copy(backupclipb)


def do_paste():
    global afterkeys

    thecard = None
    capturekeys()
    for card in aatlist.list_cards():
        newdate = utc.localize(datetime.now() + timedelta(days = 5))
        if card.created_date > newdate:
            card.delete()

        if card.name == afterkeys:
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
        afterkeys = ""


with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+c': do_copy,
        '<ctrl>+<alt>+v': do_paste,
        '<ctrl>+<alt>+x': do_copy_existing,
        }) as h:
    h.join()
