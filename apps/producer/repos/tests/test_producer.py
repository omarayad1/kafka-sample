import unittest
from unittest.mock import patch
from repos.producer import Producer


@patch("kafka.KafkaProducer")
class Test(unittest.TestCase):
    def test_mock(self, mock):
        with mock:
            producer = Producer(
                hosts="", access_cert="", access_key="", cafile="", topic=""
            )
            mock.assert_called_once()

    def test_close(self, mock):
        with mock:
            producer = Producer(
                hosts="", access_cert="", access_key="", cafile="", topic=""
            )
            producer.close()
            producer._producer.flush.assert_called_once_with()
            producer._producer.close.assert_called_once_with()

    def test_conn(self, mock):
        with mock:
            producer = Producer(
                hosts="", access_cert="", access_key="", cafile="", topic=""
            )
            producer.connected()
            producer._producer.bootstrap_connected.assert_called_once_with()

    def test_send(self, mock):
        with mock:
            producer = Producer(
                hosts="", access_cert="", access_key="", cafile="", topic="sample_topic"
            )
            producer.send("message")
            producer._producer.send.assert_called_once_with(
                "sample_topic", value="message"
            )


if __name__ == "__main__":
    unittest.main()
