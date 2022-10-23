import typer
from pynput.keyboard import Key, Listener
from config import *
import action

def on_press(key):
    if key == Key.esc:
        return False
    if key in config_listener_dict:
        eval(config_listener_dict[key])

def on_release(key):
    pass

app = typer.Typer()

@app.command()
def start():
    print(f"Listener started... (Press ESC to exit)")
    action.device_init()
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()