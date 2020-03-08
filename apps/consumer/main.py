from config import config
from repos.db import DB
from repos.consumer import Consumer


if __name__ == "__main__":
    consumer = Consumer(
        topic=config.get_config("KAFKA_TOPIC"),
        uri=config.get_config("KAFKA_URI"),
        client_id=config.get_config("KAFKA_CLIENT_ID"),
        consumer_group=config.get_config("KAFKA_CONSUMER_GROUP"),
        cafile=config.get_config("KAFKA_CAFILE"),
        access_cert=config.get_config("KAFKA_ACCESS_CERT"),
        access_key=config.get_config("KAFKA_ACCESS_KEY"),
    )

    db_repo = DB(config.get_config("PSQL_URI"))

    try:
        # this should be a seperate schema migration process instead
        db_repo.create_hb_table()
        # Short polling here
        # Consider long-polling
        for message in consumer.itermessages():
            message_value = message.value
            try:
                db_repo.insert_hb(**message_value)
            except Exception as e:
                print(f"failled to insert record {message_value}, err: {e}")
    except Exception as e:
        print(f"exception occured: {e}")
        raise e
    finally:
        consumer.close()
        db_repo.close()
