#!/bin/python3
import RPi.GPIO as GPIO
import bme280
import smbus2
from time import sleep
import requests
import sys
from datetime import datetime

#sys.stderr = object # this shouldn't be required

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

sensorPin = 3
sensorAddr = 0x76
sensorBus = smbus2.SMBus(sensorPin)
sensorCalibrationParams = bme280.load_calibration_params(sensorBus, sensorAddr)

values = sensorPin.read()
GPIO.setup(26, GPIO.OUT)

def get_time_now():     # get system time
    return datetime.now().strftime('    %H:%M:%S')

def getValues():
	#if values.is_valid():
	data = bme280.sample(sensorBus, sensorAddr, sensorCalibrationParams)
	print(get_time_now(), ":")
	print("Current temp:", data.temperature)
	print("Current humidity:", data.humidity)
	requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={'msg': f"Temperature: {data.temperature}C \n Humidity: {data.humidity}%RH"})
	if values.temperature >= 25:
		GPIO.output(26, GPIO.HIGH)
		requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={"msg": "https://media.giphy.com/media/LMC8paGihNTuo/giphy.gif"})
	else:
		GPIO.output(26, GPIO.LOW)
	#else:
	#	print("Return values invalid! Check pinout!!", data.error_code)
	#	requests.post('http://auth.ongakken.com:2005/api/postMsgToUCLchannelDiscord', headers={"Content-Type":"application/json"}, json={"msg": "Return values invalid! Check pinout!!"})
	sleep(600)
while True:
	print("Probing for temperature")
	try:
		getValues()
	except KeyboardInterrupt:
		print("Exiting.....")
		break
	except:
		continue