import unittest
from unittest.mock import patch
from repos.consumer import Consumer


@patch("kafka.KafkaConsumer")
class Test(unittest.TestCase):
    def test_mock(self, mock):
        with mock:
            consumer = Consumer(
                uri="",
                topic="",
                client_id="",
                consumer_group="",
                cafile="",
                access_key="",
                access_cert="",
            )
            mock.assert_called_once()

    def test_close(self, mock):
        with mock:
            consumer = Consumer(
                uri="",
                topic="",
                client_id="",
                consumer_group="",
                cafile="",
                access_key="",
                access_cert="",
            )
            consumer.close()
            consumer._consumer.close.assert_called_once_with(autocommit=True)


if __name__ == "__main__":
    unittest.main()
