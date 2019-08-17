from locust import HttpLocust, TaskSet, task

class MyTasks(TaskSet):
    @task
    def load_user_profile(self):
        self.client.get("/profile")

class MyWebsiteUser(HttpLocust):
    task_set = MyTasks