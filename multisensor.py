#!/usr/bin/python

########################################################
__author__ = "Edward Boal <ed.boal@edwork.org>"
__license__ = "GPL3"
__version__ = "1.0"

### RPI-MQTT-JSON-Multisensor
#
# Setup: Fill in variables under the configuration section 
# See following for more information: https://github.com/edwork/RPI-MQTT-JSON-Multisensor
#
########################################################

import time
import json
import paho.mqtt.publish as publish
import Adafruit_DHT as dht
from gpiozero import MotionSensor

## Configuration
# MQTT Server Information
MQTT_HOST = 'ip-of-your-mqtt-server'
MQTT_PORT = 1883
MQTT_USER = 'noobuser'
MQTT_PASSWORD = 'lamepass'
MQTT_CLIENT_ID = 'pi-sensor-1'
MQTT_TOPIC_PREFIX = 'hass/pisensornode'
## Sensor Information
TEMP_SENSOR_PIN = 17 ## GPIO PIN
MOTION_SENSOR_PIN = 4 ## GPIO PIN

## Setup
sensor_data = {}
pir = MotionSensor(MOTION_SENSOR_PIN)
auth_info = {
  'username':MQTT_USER,
  'password':MQTT_PASSWORD
}
try:
    while True:
        humidity,temperature = dht.read_retry(dht.DHT22,
                                              TEMP_SENSOR_PIN
                                              )
        humidity = round(humidity, 3) ## Round to 3 places
        temperature = round(temperature, 3) ## Round to 3 places
        if pir.motion_detected:
          motion = 1
        else:
          motion = 0
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity
        sensor_data['motion'] = motion
        ## Publish the message to the MQTT Broker
        publish.single('hass/testpi/sensor',
                        json.dumps(sensor_data),
                        hostname = MQTT_HOST,
                        client_id = MQTT_CLIENT_ID,
                        auth = auth_info,
                        port = MQTT_PORT
                       )
        ## Delay before running again
        time.sleep(1)
except KeyboardInterrupt:
    pass
