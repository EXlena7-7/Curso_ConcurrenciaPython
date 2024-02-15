import time 
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

class ThreadEasy(threading.Thread):
    def __init__(self, name, daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)

    def run(self):
        while True:
            logging.info('Aqui deben ir las tareas de forma concurrente')
            time.sleep(1)

if __name__ == '__main__':
    thread = ThreadEasy('Thread-Easy', True)
    thread.start()

    time.sleep(3)
    logging.info('FIN del programa!')