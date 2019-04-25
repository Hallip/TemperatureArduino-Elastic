from elasticsearch import Elasticsearch
import datetime
import serial
import time

ser = serial.Serial('/dev/tty.usbmodem411', 9600)

temperature = ""

es = Elasticsearch(
	    ["elastic:NY5aRJaOZROF3vmDP0B9VQ16@ce20cb247cec4c50ba3344288ea59e7f.us-east-1.aws.found.io:9243"],
	    scheme="https",
	    request_timeout=30
	)

while  True:
	lect = ser.read()
	if ("r" in str(lect)):

		print(temperature)

		data = {
	    "@timestamp": regTime,
	    "temperature": float(temperature)
		}

		es.index(index='temperature', doc_type='people', body=data)

		temperature = ""

	if ((not "r" in str(lect)) and (not "n" in str(lect))):
		temperature = temperature + str(lect).replace("b","").replace("'", "")
		


	regTime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")



	


	
	

	