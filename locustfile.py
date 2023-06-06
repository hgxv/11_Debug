from locust import HttpUser, task
import time

club = "Iron Temple"
competition = "Spring Festival"
class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        time.sleep(1)
        self.client.get("/pointsBoard")
        time.sleep(3)
        self.client.get(f"/book/{competition}/{club}")
        time.sleep(3)
        self.client.post("/purchasePlaces", data={
            'places' : "100",
            'club' : club,
            'competition' : competition,
        })
        time.sleep(1)
        self.client.get("/logout")
        time.sleep(1)
        