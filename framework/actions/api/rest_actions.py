import requests

class RestActions:
    api_request=None
    status_code=None
    ret_json=None

    def __init__(self) -> None:
        return None

    def get_request(self,url):
        self.api_request=requests.get(url)
        self.status_code=self.api_request.status_code
        self.ret_json=self.api_request.json()
    

    def put_requests(self, header, body, url):
        return self.requests.head(body).put(url)