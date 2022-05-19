import random
import string
import time
import sys
import paho.mqtt.client as mqtt
import logging
logging.basicConfig(level=logging.INFO)


dest = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(16)))
    #print(result_str)
def on_log(client, userdata, level, buf):
    print(buf)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    if rc == 0:
        client.connected_flag=True
        print("Connected successfully")
        #client.unsubscribe('#')
    #else:
        #print("Failed to Connect: return code=",rc)
        #client.loop_stop()

#def on_message(client, userdata, message):
    #print('Topic: %s | QOS: %s  | Message: %s' % (message.topic, message.qos, message.payload))

def on_disconnect(client, userdata, rc):
    print("Client Disconnected")

def on_publish(client, userdata, mid):
    print("In on_pub callback mid=",mid)

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed")

def on_message(client, userdata, message):
    topic=str(message.topic)
    msgr=str(message.payload.decode("utf-8"))
    print('Topic: %s | Message: %s' % (topic, message.payload))

client = mqtt.Client(dest)
client.on_connect = on_connect
mqtt.Client.connected_flag=False
client.on_log=on_log
client.on_disconnect=on_disconnect
client.on_publish=on_publish
client.on_message = on_message
#client.connect("192.168.8.200", 1883, 60)
#client.loop_forever()

topics=[("office/light",2),("house/light",2)]
topic_ack=[]
try:
    client.connect("192.168.8.200", 1883, 60)
except:
    print("cant connect")
    sys.exit(1)

client.loop_start()

while not client.connected_flag:
    logging.info("In wait Loop")
    time.sleep(1)

print("subscribing " +str(topics))
for t in topics:
    try:
        r=client.subscribe(t)
        if r[0]==0:
            logging.info("Subscribed to topic "+str(topics)+"return code"+str(r))
            topic_ack.append([topics,r[1],0])

        else:
            logging.info("error on subscribing "+str(r))
            client.loop_stop()
            sys.exit(1)

    except Exception as e:
        print(e)
