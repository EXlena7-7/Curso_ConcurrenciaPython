import logging

#
logging.basicConfig(
    level=logging.DEBUG,#10
    format='%(message)s %(processName)s',
    # format='%(message)s %(funcName)s',
    # format='%(message)s %(funcName)s', # modulo, name, pathname
    # format='%(filename)s fecha: %(message)s',
    # datefmt='%H:%M:%S',
    # filename='messages.txt'

)

def mis_mensajes():
    logging.debug('Este es un mensaje de tipo Debug')
    logging.info('Este es un mensaje tipo Info')
    logging.warning('Este es un mensaje tipo Warning')
    logging.critical('Este es un mensaje tipo Critical')


if __name__ == '__main__':
   mis_mensajes()