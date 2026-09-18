import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the provided URL and return the response body.
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Convert the response body from JSON text into Python data.
        response_body = self.get_response_body()
        return json.loads(response_body)
