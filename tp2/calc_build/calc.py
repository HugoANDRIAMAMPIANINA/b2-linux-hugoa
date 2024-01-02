import socket
import os
from sys import exit
import logging


host = '127.0.0.1'
port = int(os.getenv('CALC_PORT', 13337))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.info(f'Le serveur tourne sur {host}:{port}')

s.listen(1)

while True:
    
    conn, addr = s.accept()
    
    ip_client = addr[0]
    
    logger.info(f"Un client {ip_client} s'est connecté.")

    try:
        calculation = conn.recv(1024).decode()
        
        if not calculation: continue
        
        logger.info(f"Calcul reçu du client {ip_client} : {calculation}.")

        result = eval(calculation)
            
        conn.sendall(bytes(str(result), 'utf-8'))
        
        logger.info(f"Résultat envoyée au client {ip_client} : {result}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()
exit(0)