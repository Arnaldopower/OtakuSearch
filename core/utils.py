import time

import requests


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class APIHandler(metaclass=SingletonMeta):
    def __init__(self):
        self._BASE_URL = "https://api.jikan.moe/v4"
        self._MAX_REQ_PER_SECOND = 3
        self._MAX_REQ_PER_MINUTE = 60
        self._request_per_second = 0
        self._request_per_minute = 0
        self._last_req_time = 0
        self._second_resets = 0

    def _update_timer(self):
        current_time = time.time()
        if self._last_req_time - current_time > 1:
            self._request_per_second = 0
            self._second_resets += 1
            if self._second_resets >= 60:
                self._second_resets = 0
                self._request_per_minute = 0
            self._last_req_time = current_time

    def make_request(self, endpoint, params=None):
        while (self._request_per_second > self._MAX_REQ_PER_SECOND
               or self._request_per_minute > self._MAX_REQ_PER_MINUTE):
            self._update_timer()
        url = f"{self._BASE_URL}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Jikan API: {e}")
            return None
