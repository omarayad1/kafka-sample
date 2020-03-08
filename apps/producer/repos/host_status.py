import requests
import re
from datetime import datetime


class HostStatus(object):
    def __init__(self, url):
        self._url = url

    def perform_check(self, re_pattern=None):
        request_datetime = datetime.now().isoformat()
        response = requests.get(self._url)
        content_match = None
        if re_pattern:
            pattern = re.compile(re_pattern)
            content_match = bool(pattern.search(response.text))
        return {
            "status_code": response.status_code,
            "elapsed_time": response.elapsed.total_seconds(),
            "content_match": content_match,
            "url": response.url,
            "created_at": request_datetime,
        }
