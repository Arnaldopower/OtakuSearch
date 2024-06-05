import math
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
        self._MAX_REQ_PER_SECOND = 2
        self._MAX_REQ_PER_MINUTE = 59
        self._requests_per_second = []
        self._requests_per_minute = []

    def _update_time(self):
        current_time = time.time()
        self._requests_per_second = [t for t in self._requests_per_second if current_time - t < 1]
        self._requests_per_minute = [t for t in self._requests_per_minute if current_time - t < 60]

    def _wait(self):
        while True:
            self._update_time()
            if len(self._requests_per_second) < self._MAX_REQ_PER_SECOND and len(
                    self._requests_per_minute) < self._MAX_REQ_PER_MINUTE:
                break
            time_sleep = 0
            if len(self._requests_per_second) >= self._MAX_REQ_PER_SECOND:
                time_sleep = 1 - (time.time() - self._requests_per_minute[0])
            elif len(self._requests_per_minute) >= self._MAX_REQ_PER_MINUTE:
                time_sleep = 60 - (time.time() - self._requests_per_minute[0])
            if time_sleep > 0:
                print(f'Waiting {time_sleep} seconds before next request')
                time.sleep(time_sleep)

    def make_request(self, endpoint, params=None):
        self._wait()
        current_time = time.time()
        self._requests_per_second.append(current_time)
        self._requests_per_minute.append(current_time)
        url = f"{self._BASE_URL}/{endpoint}"
        retries = 1
        while retries <= 10:
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from Jikan API: {e}")
                print(f'Retry {retries}...')
                print('Waiting 1 second before next retry...')
                time.sleep(1)
                retries += 1
        return None
