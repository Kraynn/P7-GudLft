from locust import HttpUser, task, between


class ProjectPerfTest(HttpUser):
    wait_time = between(1,3)


    @task
    def index(self):
        self.client.get("/")

    @task
    def showSummary(self):
        self.client.get("/showSummary")
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def book(self):
        self.client.get("/book/Spring Festival/Simply Lift")

    @task
    def purchasePlaces(self):
        self.client.post( "/purchasePlaces", data={
        "club": "Simply Lift", "competition": "Spring Festival", "places": 2})

    @task
    def clubs_display(self):
        self.client.get('/displayClubs')

    @task
    def logout(self):
        self.client.get('/logout')