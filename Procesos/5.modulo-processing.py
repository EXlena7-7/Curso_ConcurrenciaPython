import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

if __name__ == '__main__':
    current_process = multiprocessing.current_process()
    
    logging.info(f'El proceso actual es: {current_process}')