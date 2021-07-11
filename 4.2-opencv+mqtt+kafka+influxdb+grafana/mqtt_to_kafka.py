import paho.mqtt.client as mqtt
from kafka import KafkaProducer

def on_message(client, userdata, message):
	received = message.payload.decode("utf-8")
	print("Received message:", received, "via MQTT")
	producer.send('sample', received.encode('ascii'))
	producer.flush()
	print("Successfully send this message via Kafka")

print ("MQTT to Kafka transfer is on")

producer = KafkaProducer(bootstrap_servers='localhost:9092')

client = mqtt.Client("noname")
client.connect("localhost")
client.subscribe("program_to_connector")
client.on_message = on_message
client.loop_forever()
