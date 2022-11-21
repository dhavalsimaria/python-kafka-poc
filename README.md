[Setting Up and Running Apache Kafka on Windows OS](https://dzone.com/articles/running-apache-kafka-on-windows-os)

***

<h2>[1] Start Zookeeper server</h2>

[1.1] Go to your Zookeeper directory, e.g.: C:\Apache\apache-zookeeper-3.6.2\bin

[1.2] Execute `zkserver` command

***

<h2>[2] Start Kafka Server</h2>

[2.1] Go to your Kafka installation directory: e.g.: C:\Apache\kafka_2.13-2.6.0

[2.2] Open a command prompt here by pressing Shift + right click and choose the “Open command window here” option).

[2.3] To start Kafka broker, execute 

`.\bin\windows\kafka-server-start.bat .\config\server.properties`


[2.4] To create Kafka topic, 

`kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic user-tracker`

