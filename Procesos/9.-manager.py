import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

# Manager -> Namespace -> Contexto
def get_valor(namespace):
    while namespace.codigo is None:
        time.sleep(0.5)
        logging.info('Aqui no se recibe ningun valor!')
    else:
        logging.info(namespace.codigo)
        logging.info(namespace.prueba_de_nueva_variable)
    
def set_valor(namespace):
    time.sleep(4)
    namespace.codigo = 'Aplicando Manager!'

if __name__ =='__main':
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()
    
    namespace.codigo = None
    namespace.prueba_de_nueva_variable = True
    
    process1 = multiprocessing.Process(target=get_valor, args=(namespace, ))
    process2 = multiprocessing.Process(target=set_valor, args=(namespace, ))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()