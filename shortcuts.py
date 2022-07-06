from pynput import keyboard
import subprocess

pressed = set()

COMBINATIONS = [
    {
        "keys": [
            {keyboard.Key.cmd, keyboard.KeyCode(char="w")},
            {keyboard.Key.cmd, keyboard.KeyCode(char="W")},
        ],
        "command": "notepad",
    },
    {
        "keys": [
            {keyboard.Key.cmd, keyboard.KeyCode(char="c")},
            {keyboard.Key.cmd, keyboard.KeyCode(char="C")},
        ],
        "command": "gnome-calculator",
    },
]

def run(s):
    subprocess.Popen(s)

def on_press(key):
    pressed.add(key)
    print(pressed)
    for c in COMBINATIONS:
        for keys in c["keys"]:
            if keys.issubset(pressed):
                run(c["command"])

def on_release(key):
    if key in pressed:
        pressed.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
