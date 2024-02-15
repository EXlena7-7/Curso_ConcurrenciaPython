import time 
import logging
import requests
import threading


logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def thread():
    logging.info('Hola, soy un thread normal')
    time.sleep(0.5)
    logging.info("El programa finaliza cuando Yo finalizo!")

def daemon_thread():
    while True:
        logging.info('Nos ejecutamos en segundo planon en background!')

if __name__ == '__main__':
    thread = threading.Thread(target=daemon_thread, daemon=True)
    thread.start()   