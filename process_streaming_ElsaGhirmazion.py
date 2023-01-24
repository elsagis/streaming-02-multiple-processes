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
input_file = open("process_streaming_elsaghirmazion.csv", "r")
output_file = open("out9.txt", 'w')
# To get them in chronological order use the builtin sorted() function
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")


writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ['Id', 'IndicatorCode', 'SpatialDim', 'SpatialValueCode', 'TimeDim_year', 'Value', 'NumericValue', 'Date', 'TimeDimensionValue', 'TimeDimensionBegin', 'TimeDimensionEnd']

writer.writerow(header_list)

for row in reader:
    # read a row from the file
    Id, IndicatorCode, SpatialDim, SpatialValueCode, TimeDimyear, Value, NumericValue, Date, TimeDimensionValue, TimeDimensionBegin, TimeDimensionEnd = row 

    # use an fstring to create a message from our data
    fstring_message = f"[{Id}, {IndicatorCode}, {SpatialDim}, {SpatialValueCode}, {TimeDim_year}, {value}, {NumericValue}, {Date}, {TimeDimensionValue}, {TimeDimensionBegin}, {TimeDimensionEnd}]"
    
    # prepare a binary (1s and 0s) message to stream
    output_file.write(fstring_message)
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, ADRESS_TUPLE)
    print (f"Sent: {MESSAGE} on port {port},\n")
    writer.writerow([Id, IndicatorCode, SpatialDim, SpatialValueCode, TimeDim_year, Value, NumericValue, Date, TimeDimensionValue, TimeDimensionBegin, TimeDimensionEnd])


    # sleep for a few seconds
    time.sleep(1)
output_file.close()
input_file.close()


