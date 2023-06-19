# Step implementation for petstore.spec

import requests
import logging
from getgauge.python import data_store, step
from util.constants import BASE_URL


@step("When I make a <method> request to <endpoint>")
def make_get_request(method, endpoint):
    url = f"{BASE_URL}{endpoint}"
    method = method.upper()

    if method == "GET":
        response = requests.get(url, verify=False)
        pass
    elif method == "POST":
        response = requests.post(url, verify=False)
        pass
    elif method == "PUT":
        response = requests.put(url, verify=False)
        pass
    elif method == "DELETE":
        response = requests.delete(url, verify=False)
        pass
    else:
        raise ValueError("Invalid HTTP method specified")

    if not response.ok:
        error_msg = ("{} request to {} failed with status code: {}".format(
            method, url, response.status_code))
        logging.error(error_msg)
        raise AssertionError(error_msg)

    if "response" not in data_store.scenario:
        data_store.scenario["response"] = {}

    data_store.scenario["response"] = response
    # success_msg = "{} request is successfully.".format(endpoint)


@step("The response code should be <code>")
def verify_response_code(code):
    response = data_store.scenario["response"]
    # assert response_body.status_code == int(code)
    if response.status_code != int(code):
        error_msg = (
            "Expected response code: {}, Actual response code: {}".format(
                code, response.status_code))
        logging.error(error_msg)
        raise AssertionError(error_msg)


@step("The response body contains <text>")
def verify_response_body_contains(text):
    if "response" not in data_store.scenario:
        error_msg = "No response found. Make a request first."
        logging.error(error_msg)
        raise AssertionError(error_msg)

    response = data_store.scenario["response"]
    response_json = response.json()
    if text not in response_json:
        error_msg = (
            "Expected response body to contain '{}', "
            "but it does not in '{}'".format(text, response_json)
        )
        logging.error(error_msg)
        raise AssertionError(error_msg)
