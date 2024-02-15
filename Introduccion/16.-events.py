import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def thread_1(event):
    logging.info('Estoy a la espera de la señal!')

    event.wait()

def thread_2(event):
    logging.info('La señal fue dada, la bandera es True')

    while event.is_set():
        logging.info('A la espera de la señal')
        time.sleep(0.5)
        
if __name__ == '__main__':

    event = threading.Event()
    # Bandera = True o False
    
    thread1 = threading.Thread(target=thread_1, args=(event, ))
    thread2 = threading.Thread(target=thread_2, args=(event, ))

    thread1.start()
    thread2.start()

    time.sleep(3)
    
    event.set()

    event.clear()