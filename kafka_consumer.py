import json

from confluent_kafka import Consumer
from dacite import from_dict

################
from consumed_data import ConsumedData

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['user-tracker'])


################
def main():
    while True:
        msg = c.poll(1.0)  # timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data: ConsumedData = msg.value().decode('utf-8')
        consumer_msg: ConsumedData = from_dict(data_class=ConsumedData, data=json.loads(data))
        #print(data)
        if consumer_msg.user_name is None \
                or consumer_msg.mu_custom_id is None or consumer_msg.user_name is None \
                or consumer_msg.user_address is None or consumer_msg.signup_at is None \
                or consumer_msg.platform is None:
            print('Key not present!!')
            print(str(consumer_msg))
        else:
            print('Key present!!')



    c.close()


if __name__ == '__main__':
    main()