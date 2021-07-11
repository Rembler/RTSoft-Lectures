#!/bin/bash
echo "Producer starts sending messages..."
i=1
for (( ; ; ))
do
	echo "Message with number $i" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic MessagePerThreeSeconds > /dev/null
	((i=i+1))
	sleep 3 
done
