import time
import logging
import threading
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,format='%(threadName)s: %(message)s',)

def math_operation(number1, number2):
    time.sleep(1)

    result = number1 + number2
    logging.info(f'Resultado de {number1} + {number2} = {result}')

if __name__ == '__main__':
        executor = ThreadPoolExecutor(max_workers=3, thread_name_prefix='facilitos')

        executor.submit(math_operation, 10, 20)
        executor.submit(math_operation, 50, 40)

        executor.submit(math_operation, 200, 100)
        executor.submit(math_operation, 70, 60)


        """
        1.-Generar Threads computacionalmente es costoso y por eso se debe agregar de forma indescriminada
        # for _ in range(0, 1000):
        #     thread = threading.Thread(target=math_operation, argss=(10,20))
        #     thread.start()

        2.- Pool: Mediante pisinas podemos generar n cantidad de thread que se necesiten bajo demanda
        Si los threads se encuentran ocupados esa tarea se agenda y se va asignar al primer Thread que se libere
        """