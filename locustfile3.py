from locust import HttpLocust, TaskSequence, seq_task


class MyTasks(TaskSequence):
    @seq_task(1)
    def login(self):
        self.client.post("/login",
                         {"username": "testQA", "password": "12345"})

    @seq_task(2)
    def get_dashboard(self):
        self.client.get("/dashboard")

    @seq_task(3)
    def get_product(self):
        self.client.get("/products/lamps?id=102")


class MyWebsiteUser(HttpLocust):
    task_set = MyTasks
