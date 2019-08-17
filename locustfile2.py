from locust import HttpLocust, TaskSet, task

class MyTasks(TaskSet):
    @task(2)
    def get_carpets(self):
        self.client.get("/products/carpets")

    @task(3)
    def get_lamps(self):
        self.client.get("/products/lamps")

class MyWebsiteUser(HttpLocust):
    task_set = MyTasks