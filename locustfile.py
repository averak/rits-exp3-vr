import random
from locust import HttpUser, task, between


KEYWORDS = [
    '医療',
    '世界史',
    '動物',
    '建築',
    '教育',
    '料理',
    '芸能',
    '音楽',
]


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    def on_start(self):
        pass

    @task
    def search_books(self):
        # request params
        params: dict = {
            'keyword': random.choice(KEYWORDS),
            'max_results': random.randint(30, 50),
        }

        # send request
        self.client.get("/books", params=params)
