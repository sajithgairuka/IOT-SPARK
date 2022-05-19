import paho.mqtt.client as mqtt
import time
import logging
logging.basicConfig(level=logging.INFO)

broker = "192.168.8.200"
port = 1883


def on_log(client, userdata, level, buf):
    logging.info(buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        logging.info("connected successfully")

    else:
        logging.info("Bad Connection: return code="+str(rc))
        client.loop_stop()


def on_disconnect(client, userdata, rc):
    logging.info("Client disconnected ok")


def on_publish(client, userdata, mid):
    logging.info("In on_pub callback mid=" + str(mid))


def on_subscribe(client, userdata, mid, granted_qos):
    logging.info("subscribed")


def on_message(client, userdata, message):
    topic = str(message.topic)
    msgr = str(message.payload.decode("utf-8"))
    logging.info('Topic: %s | Message: %s' % (topic, msgr))

#def reset():
    #ret=client.publish("home/light","",0,True)


def publishing():

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
    logging.info("publishing")
    ret = client.publish("home/light", "on", 1, True)
    logging.info("publish return="+str(ret))
    time.sleep(3)
    ret = client.publish("home/light", "off", 2, True)
    logging.info("publish return="+str(ret))
    time.sleep(3)
    client.subscribe("home/light", 2)
    #reset()
    time.sleep(10)
    client.loop_stop()
    client.disconnect()

publishing()
