import threading
from multiprocessing import Process
LOCK = True

def start_loop_thread():
    while LOCK:
        pass


def cpu_full_load():
    for i in range(9):
        p = Process(target=start_loop_thread)
        p.start()

if __name__ =='__main__':
    cpu_full_load()
