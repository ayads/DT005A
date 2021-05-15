# ec2-54-93-225-255.eu-central-1.compute.amazonaws.com
# localhost: http://127.0.0.1:8089
from locust import HttpLocust, TaskSet, task, between


class UserTasks(TaskSet):    
    # but it might be convenient to use the @task decorator
    @task
    def forcasting_classification(self):
        #self.client.get("/forecasting-classification?temperatures=23,24,25")
        self.client.get("/")
    
class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://127.0.0.1:8089"
    wait_time = between(0.2, 0.5)
    task_set = UserTasks