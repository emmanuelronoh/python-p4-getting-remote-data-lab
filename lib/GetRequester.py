import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Fetches the raw response body from the URL."""
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content  # Return the raw byte content

    def load_json(self):
        """Loads the JSON response into a Python data structure."""
        json_string = self.get_response_body()  # Get the raw response
        return json.loads(json_string)  # Parse and return the JSON as a Python object
