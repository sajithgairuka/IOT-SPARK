import random
import string
import time
import sys
import paho.mqtt.client as mqtt

#Mosquitto - No data in $SYS topics https://stackoverflow.com/questions/45699458/mosquitto-no-data-in-sys-topics
#Mosquitto - QOS https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/
#https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/
#https://book.hacktricks.xyz/pentesting/1883-pentesting-mqtt-mosquitto

name = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(16)))
    #print(result_str)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    er = client.subscribe('#',2)
    er+= client.subscribe('$SYS/#',2)
    #er=client.subscribe("office/led")

    if er[0] == 0:
        print("Successfully subscribed to all system topics")

    else:
        print("Failed to subscribe to all system topics.")

def on_message(client, userdata, message):
	print('Topic: %s | QOS: %s  | Message: %s' % (message.topic, message.qos, message.payload))

def main():
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("192.168.8.200", 1883, 60)
        client.loop_forever()

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
