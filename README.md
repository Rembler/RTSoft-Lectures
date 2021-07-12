# RTSoft-Lectures
*Several tasks based on lectures material*

## Task 1.1 - udev rule
No configuration required. Just input the USB device.

## Task 1.2 - character device driver
Run the following commands to install driver:
```
$ make
$ sudo insmod Increment.ko
$ sudo mknod /dev/inc c 234 0
```
Run this to check if the driver works:
```
$ gcc test_program.c
$ ./a.out
```

## Task 2.1 - docker
Use this commands to start Firefox browser inside docker container:
```
$ sudo xhost +local:root
$ sudo docker build -t dockerfox .
$ sudo docker run -it --env="DISPLAY" --net=host dockerfox
```

## Task 2.2 - opencv contours detector
Just start program execution via:
```
$ python3 detect_contours.py
```

## Task 3.1 - opencv trajectory drawer + mqtt
To run program and start receiving messages use this:
```
$ python3 draw_trajectory.py
$ mosquitto_sub -h localhost -t video/data
```

## Task 4.1 - kafka
Execute the following commands sequentially (the last two - on behalf of the kafka-user):
```
$ sudo ./move_files.sh
$ sudo ./start.sh
$ ./producer.sh
```

## Task 4.2 - opencv trahectory drawer + mqtt + kafka + influxdb + grafana
Start executing the programs in the following order:
```
$ python3 kafka_to_influxdb.py
$ python3 mqtt_to_kafka.py
$ python3 draw_trajectory.py
```
Open the `grafana_time_series.png` to see the result of using grafana.
