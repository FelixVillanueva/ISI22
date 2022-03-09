#code from https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

from paho.mqtt import client as mqtt_client
from loguru import logger
import random

broker = 'localhost'
port = 1883
topic = "isi/+"
client_id = f'mqtt-sub-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT Broker!")
        else:
            logger.error("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        logger.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    logger.info(client.subscribe(topic))
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()