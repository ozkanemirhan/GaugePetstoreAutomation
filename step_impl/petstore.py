# Step implementation for petstore.spec

import requests
import logging
from getgauge.python import data_store, step


@step("When I make a GET request to <endpoint>")
def make_get_request(endpoint):
    url = f"https://petstore.swagger.io/v2{endpoint}"
    response = requests.get(url, verify=False)

    if not response.ok:
        logging.error("GET request to {} failed with status code: {}".format(
            url, response.status_code))

    if "response" not in data_store.scenario:
        data_store.scenario["response"] = {}

    data_store.scenario["response"] = response
    # success_msg = "{} request is successfully.".format(endpoint)


@step("The response code should be <code>")
def verify_response_code(code):
    response = data_store.scenario["response"]
    # assert response_body.status_code == int(code)
    if response.status_code != int(code):
        error_msg = "Expected response code: {}, Actual response code: {}".format(code, response.status_code)
        logging.error(error_msg)
        raise AssertionError(error_msg)


@step("The response body contains <text>")
def verify_response_body_contains(text):
    response = data_store.scenario["response"]
    response_json = response.json()
    if text not in response_json:
        error_msg = "Expected response body to contain '{}', but it does not in '{}".format(text, response_json)
        logging.error(error_msg)
        raise AssertionError(error_msg)
