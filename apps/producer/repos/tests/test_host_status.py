import unittest
from unittest.mock import patch
from repos.host_status import HostStatus


@patch("requests.get")
class Test(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.example.com"
        self.host_status = HostStatus(self.url)

    def test_url(self, mock):
        self.assertEqual(self.host_status._url, self.url)

    def test_check(self, mock):
        with mock:
            check = self.host_status.perform_check()
            self.assertTrue(
                check.keys()
                >= {"created_at", "elapsed_time", "status_code", "url", "content_match"}
            )
            mock.assert_called_once_with(self.url)


if __name__ == "__main__":
    unittest.main()
