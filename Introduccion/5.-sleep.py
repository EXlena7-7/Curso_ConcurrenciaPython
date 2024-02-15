import time
import logging
import threading


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(thread)s %(threadName)s : %(message)s'
# )

# def task():
#     logging.info('Nos encontramos ejecutando una nueva tarea')
#     time.sleep(0.5)
#     logging.info('Tarea finalizada')

# if __name__ == '__main__':
#     thread = threading.Thread(target=task)
#     thread.start()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s : %(message)s'
)

if __name__ == '__main__':
    contador = 0
    while True:
        time.sleep(1)
        contador += 1
        logging.info(f'Tiempo transcurrido: {contador} segundos')
