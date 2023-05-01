import requests

class RestActions:
    
    def get_request(self, url):
        requests.get(url)

    def put_requests(self, header, body, url):
        requests.head(body).put(url)