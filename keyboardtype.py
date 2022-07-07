#!/usr/bin/env python


# from pynput import keyboard

# in command prompt, type "pip install pynput" to install pynput.
from pynput.keyboard import Key, Controller

keyboard = Controller()
totype = "megalolzor"


keyboard.type(totype)
# print(dir(keyboard))
#
# keyboard.press(key)
# keyboard.release(key)
