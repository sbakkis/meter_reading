#!/usr/bin/python

import serial 
import time 
import sys
import csv
import os
from aidon_obis import *


TIMEFORMAT = "%a, %d %b %Y %H:%M:%S "
FOLDER_NAME = "maaledata"

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)


def write_to_csv(filename, fields):
	#If file does not exist, create file and write headers
	if not os.path.exists(filename):
			with open(filename, "Ua") as f:
					f.write( ", ".join([key for key in fields.keys()]) )

	with open(filename, "Ua+") as f:
		f.write( ", ".join([key for key in fields.keys()]) )


def aidon_callback(fields):
	return fields





# while(1):
# 	while ser.inWaiting():
# 		a.decode(ser.read(1))
# 	time.sleep(0.01)

def get_meter_info(serial_connection, try_time, aidon):
	meter_info_timer = time.time()

	while serial_connection.inWaiting():
		while time.time() - meter_info_timer <= try_time:
			meter_fields = aidon.decode(serial_connection.read(1))
			if len(meter_fields) > OBJECTS_2P5SEC:
				return {
					"version_id": meter_fields["version_id"],
					"meter_id": meter_fields["meter_id"],
					"meter_type": meter_fields["meter_type"]
				}
			time.sleep(0.01)
					
		print "Unable to get meter info within trial time: " + str(try_time)
		sys.exit(0)




if __name__ == "__main__":

	if len (sys.argv) != 2:
		print "Usage: ... <serial_port>"
		sys.exit(0)

	ser = serial.Serial(sys.argv[1], 2400, timeout=0.05, parity=serial.PARITY_NONE)
	a = aidon(aidon_callback)

	meter_info = get_meter_info( ser, 60, a)

	# run logging forever until stopped.
	while(1):
		while serial.inWaiting():
			start_time = time.time()
			start_time_string = time.strftime(TIMEFORMAT, start_time)
			while time.time() - start_time < 20:
				filename = time.strftime(TIMEFORMAT, start_time) + " " + meter_id
				write_to_csv(filename, )
