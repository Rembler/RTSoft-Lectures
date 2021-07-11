#!/bin/bash
systemctl start kafka
if ~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181 | grep -q "MessagePerThreeSeconds"; then
	echo "Topic --MessagePerThreeSeconds-- already exists. No need to create new."
else
	~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic MessagePerThreeSeconds
fi
echo "Starting consumer script..."
sh ./consumer.sh

	
