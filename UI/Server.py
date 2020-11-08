import socket
import csv
from datetime import date, datetime

address = ('127.0.0.1', 1234)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)
sock.listen(10)
while True:
    print("Waiting for connection..")
    connection, client_address = sock.accept()
    with open('log.csv', mode='a') as log:
        log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        log_writer.writerow([client_address[0], date.today().strftime("%b-%d-%Y"), datetime.now().time()])
    connection.close()

