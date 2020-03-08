from time import sleep
from config import config
from repos.producer import Producer
from repos.host_status import HostStatus


if __name__ == "__main__":
    producer = Producer(
        hosts=config.get_config("KAFKA_URI"),
        access_cert=config.get_config("KAFKA_ACCESS_CERT"),
        access_key=config.get_config("KAFKA_ACCESS_KEY"),
        cafile=config.get_config("KAFKA_CAFILE"),
        topic=config.get_config("KAFKA_TOPIC"),
    )
    host_status = HostStatus(config.get_config("STATUS_HOST"))

    try:
        # check if bootstrap is connected
        connected = producer.connected()
        while connected:
            print("performing heartbeat check")
            check = host_status.perform_check(config.get_config("REGEX_PATTERN"))

            print("sending to topic")
            producer.send(check)
            sleep(config.get_config("STATUS_INTERVAL"))
    except Exception as e:
        print("exception occured", e)
        raise e
    finally:
        producer.close()
