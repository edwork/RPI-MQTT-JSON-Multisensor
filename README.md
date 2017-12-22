# RPI-MQTT-JSON-Multisensor
Raspberry Pi MQTT JSON Multisensor for Home Assistant. Supported sensors include the AM312 PIR, DHT11/22 temperature/humidity sensors.

## Requirements
* paho-mqtt (install using [pip](https://pypi.python.org/pypi/paho-mqtt/1.1))
* Adafruit_DHT (install via their [git repo](https://github.com/adafruit/Adafruit_Python_DHT))
* gpiozero (installed by default on Raspi - [link to docs](https://gpiozero.readthedocs.io/en/stable/))

## Configuring
Under the 'Configuration' section of the script replace the appropriate variables. If you don't use authentication with a private MQTT server just leave it with null information. Using a DHT11 instead of a DHT22? Just change line 43.

## Running
You can simply run the file with `./multisensor.py` (after configuring) in a terminal and go on your merry way or run it as a service.

## Running as a service
### Systemd
* Copy rpi-sensor.service to `/etc/systemd/system/`
* Run (as root) `systemctl enable rpi-sensor.service`
* Run (as root) `systemctl start rpi-sensor.service`