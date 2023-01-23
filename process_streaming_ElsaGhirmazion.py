# Module 02- code by Elsa Ghirmazion
# TODO: with open() as f
import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from a file to get some fake data
input_file = open("ElsaGhirmazion.csv", "r")

# create a csv reader for our comma delimited data
reader = csv.reader(input_file, delimiter=",")

output_file_name = "out9.txt"
output_file = open(output_file_name, "w", newline='')

writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ['Id', 'Value', 'NumericValue', 'TimeDim/year', 'SpatialDim']
writer.writerow(header_list)

for row in reader:
    # read a row from the file
    Id, Value, NumericValue, SpatialDim = row 

    # use an fstring to create a message from our data
    fstring_message = f"[{Id}, {Value}, {NumericValue}, {SpatialDim}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    print (f"Sent: {MESSAGE} on port {port}.")

    # sleep for a few seconds
    time.sleep(3)
output_file.close()
input_file.close()


