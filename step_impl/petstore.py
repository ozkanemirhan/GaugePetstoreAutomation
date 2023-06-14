# Step implementation for petstore.spec

import requests
from getgauge.python import data_store, step


@step("When I make a GET request to <endpoint>")
def make_get_request(endpoint):
    url = f"https://petstore.swagger.io/v2{endpoint}"
    response = requests.get(url)
    assert not response.ok
    response_body = response.json()

    if "announcements_details" not in data_store.scenario:
        data_store.scenario["response_body"] = {}

    data_store.scenario["response_body"] = response_body
    # success_msg = "{} request is successfully.".format(endpoint)


@step("The response code should be <code>")
def verify_response_code(code):
    response_body = data_store.scenario["response_body"]
    assert response_body.status_code == int(code)


@step("The response body contains <text>")
def verify_response_body_contains(text):
    response_body = data_store.scenario["response_body"]
    assert text in response_body
