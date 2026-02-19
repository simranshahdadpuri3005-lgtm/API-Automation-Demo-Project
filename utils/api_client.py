import json

class APIClient:
    def __init__(self, base_url, request_context):
        self.base_url = base_url
        self.request_context = request_context

    def get(self, endpoint):
        return self.request_context.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, payload=None):
        return self.request_context.post(
            f"{self.base_url}{endpoint}",
            data=json.dumps(payload) if payload else None,
            headers={"Content-Type": "application/json"}
        )

    def put(self, endpoint, payload=None):
        return self.request_context.put(
            f"{self.base_url}{endpoint}",
            data=json.dumps(payload) if payload else None,
            headers={"Content-Type": "application/json"}
        )

    def patch(self, endpoint, payload=None):
        return self.request_context.patch(
            f"{self.base_url}{endpoint}",
            data=json.dumps(payload) if payload else None,
            headers={"Content-Type": "application/json"}
        )

    def delete(self, endpoint):
        return self.request_context.delete(f"{self.base_url}{endpoint}")