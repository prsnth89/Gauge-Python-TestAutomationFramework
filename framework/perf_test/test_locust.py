from locust import HttpUser,task,between

class PerfTest(HttpUser):
    wait_time=between(1,5)
    
    @task
    def run_test(self):
        list_of_page=self.client.get(url="https://reqres.in/api/users?page=2")
        print(list_of_page.status_code)
        assert int(list_of_page.status_code==200)
