import kafka
from json import dumps


class Producer(object):
    def __init__(self, hosts, access_cert, access_key, cafile, topic):
        self._producer = kafka.KafkaProducer(
            bootstrap_servers=hosts,
            security_protocol="SSL",
            ssl_certfile=access_cert,
            ssl_keyfile=access_key,
            ssl_cafile=cafile,
            value_serializer=lambda x: dumps(x).encode("utf-8"),
        )
        self._topic = topic

    def send(self, message):
        self._producer.send(self._topic, value=message)

    def connected(self):
        return self._producer.bootstrap_connected()

    def close(self):
        self._producer.flush()
        self._producer.close()
