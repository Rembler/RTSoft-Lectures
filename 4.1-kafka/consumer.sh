#!/bin/bash
echo "Consumer starts receiving messages..."
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic MessagePerThreeSeconds
