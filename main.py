from time import sleep
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

sense = SenseHat()

broker_address = "192.168.8.108"	# localhost or IP address
thing_id = "2dfd40f9-fe26-4ff8-9da4-4a45771b824a"
thing_key = "24d521e1-5e81-4eec-8236-2bd935e2f852"
channel_id = "3a6bf099-bcb6-402e-9ece-bebede72126a"

client = mqtt.Client()
client.username_pw_set(thing_id, thing_key)
client.connect(broker_address)


while True:

    # Take readings from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Create the message
    # str() converts the value to a string so it can be concatenated
    message = "[{\"n\":\"temperature\",\"v\":" + str(t) + ",\"u\":\"Cel\"}, {\"n\":\"pressure\",\"v\":" + str(p) + ",\"u\":\"mbar\"}, {\"n\":\"humidity\",\"v\":" + str(h) + ",\"u\":\"%RH\"}]"

    # Send SENML message

    client.publish(topic = "channels/" + channel_id + "/messages", payload = message) 
    sleep(1)
