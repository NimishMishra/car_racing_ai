# Mac OS needs special permissions to access the keyboard inputs. Use sudo to
# run any script that calls the key_check() function defined here

from pynput import keyboard
import threading

keys = []

def on_press(key):
    try:
        if (key.char.upper() not in keys):
            keys.append(key.char.upper())
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        keys.remove(key.char.upper())
    except AttributeError:
        pass

def listen_keys():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

t = threading.Thread(target=listen_keys)
t.daemon = True
t.start()

def key_check():
    return keys
