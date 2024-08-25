from pynput.mouse import Listener


def write_in_file(x, y):
    f = open('m_log.txt', 'a')
    f.write("\nCurrent Mouse Co-ordinates :{0}".format((x, y)))


with Listener(on_move=write_in_file) as l:
    l.join()
