from kafka import KafkaConsumer
from influxdb import InfluxDBClient
import json

print("Kafka to InfluxDB connector is on")

consumer = KafkaConsumer('sample')

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('coordinates')
client.switch_database('coordinates')
client.query('DELETE FROM opencv')

for message in consumer:
	data = json.loads(message.value.decode('utf-8'))
	print("Got a message:", data)
	json_body = [
	{
	"measurement": "opencv",
	"fields":{
		"x_r": data['Real']['x'],
		"y_r": data['Real']['y'],
		"x_f": data['Filtered']['x'],
		"y_f": data['Filtered']['y']
	}
	}]
	if client.write_points(json_body):
		print("Message was successfully written into the database")
	else:
		print("An error occured")
	