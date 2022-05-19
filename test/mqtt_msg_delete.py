import paho.mqtt.client as mqtt
import time
import logging
logging.basicConfig(level=logging.INFO)

broker = "192.168.8.200"
port = 1883


def on_message(client, userdata, message):
    topic = str(message.topic)
    msgr = str(message.payload.decode("utf-8"))
    logging.info('Deleting Topic: %s | Message: %s' % (topic, msgr))


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        logging.info("connected successfully")

    else:
        logging.info("Bad Connection: return code="+str(rc))
        client.loop_stop()


def on_subscribe(client, userdata, mid, granted_qos):
    logging.info("subscribed")


def on_log(client, userdata, level, buf):
    logging.info(buf)


def on_publish(client, userdata, mid):
    logging.info("In on_pub callback mid=" + str(mid))
    client.suback_flag = True


def reset():
    ret = client.publish("home/light", "", 0, True)
    logging.info(str(ret))


def on_disconnect(client, userdata, rc):
    logging.info("Client disconnected")


mqtt.Client.connected_flag = False
client = mqtt.Client("test")
client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(broker, port)
client.loop_start()

while not client.connected_flag:
    logging.info("In wait Loop")
    time.sleep(1)

time.sleep(3)
client.subscribe("home/light", 2)
reset()
time.sleep(10)
client.loop_stop()
client.disconnect()
