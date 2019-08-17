from locust import HttpLocust, TaskSet, task


class MyTasks(TaskSet):
    @task(2)
    def invalid_product(self):
        with self.client.get("/products/moths") as response:
            if response.status_code == 404:
                response.success()

    @task(3)
    def get_lamps(self):
        self.client.get("/products/lamps")


class MyWebsiteUser(HttpLocust):
    task_set = MyTasks
