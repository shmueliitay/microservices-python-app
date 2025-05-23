# tests/test_movies.py
import unittest
import requests

class TestMoviesService(unittest.TestCase):
    def setUp(self):
        self.url = "https://cinema.com/movies"

    def test_all_movie_records(self):
        ids = [
            "a8034f44-aee4-44cf-b32c-74cf452aaaae",
            "96798c08-d19b-4986-a05d-7da856efb697",
            "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
        ]
        for movie_id in ids:
            res = requests.get(f"https://5.144.49.3/movies/{movie_id}", verify=False)
            self.assertEqual(res.status_code, 200)
            data = res.json()
            self.assertEqual(data["id"], movie_id)
