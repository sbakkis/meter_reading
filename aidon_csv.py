#!/usr/bin/python

import serial, time, sys, csv, os
#from aidon_obis import *

# if len (sys.argv) != 2:
# 	print "Usage: ... <serial_port>"
# 	sys.exit(0)
timeformat = "%a, %d %b %Y %H:%M:%S "
folder_name = "maaledata"

if not os.path.exists(folder_name):
	os.makedirs(folder_name)


def write_to_csv(filename, fields):
	if not os.path.exists(filename):
		with open(filename, "a+") as f:
			f.write([key for key in fields.keys()])

	with open(filename, "a+") as f:
		f.write([fields[key] for key in fields.keys()])


def aidon_callback(fields):
	return fields


#ser = serial.Serial(sys.argv[1], 2400, timeout=0.05, parity=serial.PARITY_NONE)

#a = aidon(aidon_callback)

# while(1):
# 	while ser.inWaiting():
# 		a.decode(ser.read(1))
# 	time.sleep(0.01)

if __name__ == "__main__":
	start_time = time.time()

	while time.time() - start_time < 20:
		with open("test.csv", "a+") as csv_file:
			csv_writer = csv.DictWriter(csvfile, fieldnames=test.keys())

			writer.writeheader()
			writer.writerow()

