import kafka
from json import loads


# this is just a dummy wrapper
class Consumer(object):
    def __init__(
        self, uri, topic, client_id, consumer_group, cafile, access_key, access_cert
    ):
        self._consumer = kafka.KafkaConsumer(
            topic,
            auto_offset_reset="earliest",
            bootstrap_servers=uri,
            client_id=client_id,
            group_id=consumer_group,
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode("utf-8")),
            security_protocol="SSL",
            ssl_cafile=cafile,
            ssl_certfile=access_cert,
            ssl_keyfile=access_key,
        )

    def itermessages(self):
        return self._consumer

    def close(self):
        self._consumer.close(autocommit=True)
