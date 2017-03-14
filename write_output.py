#!/usr/bin/env python
 
import snap7.client as c
from snap7.util import *
from time import sleep
import sys
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def WriteOutput(dev,bytebit,cmd):
     byte,bit = bytebit.split('.')
     byte,bit = int(byte),int(bit)
     data = dev.read_area(0x82,0,byte,1)
     set_bool(data,byte,bit,cmd)
     dev.write_area(0x82,byte,data)

def main():
     plc_ip = ""
     plc_port = 102
     with open('plc_ip') as plc_ip_file:
     	plc_ip_read_data = plc_ip_file.read().split(":")
     	plc_ip = plc_ip_read_data[0]
        plc_port = int(plc_ip_read_data[len(plc_ip_read_data) - 1])
     logging.info("connecting to PLC: %s, port: %s", plc_ip, plc_port)
     plc = c.Client()
     plc.connect(plc_ip,11,11,plc_port)
     logging.info("plc connected: %s", plc.get_connected())
     for x in range(10):
         WriteOutput(plc,'0.0',x%2==0) # turns true every other iteration
         sleep(1)

if __name__ == "__main__":
     main()
