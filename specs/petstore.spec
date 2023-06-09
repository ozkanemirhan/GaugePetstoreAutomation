# Specification Heading

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run

    gauge run specs/petstore.spec


## Scenario: User Login
tags: login, admin
* When I login with back office user

* The response code should be "200"


## Scenario: Ensure pet inventory is available
tags: pet-inventory, sanity
* When I make a "GET" request to "/store/inventory"

* The response code should be "200"

* The response body contains "available"

* The response body contains "sold"

* The response body contains "unavailable"

* The response body contains "ready to deliver"


## Scenario: Ensure pet inventory is not empty
tags: pet-inventory, sanity
* When I make a "GET" request to "/store/inventory"

* The response code should be "200"

* The response body should not be empty


## Scenario: Verify getting pet details
* When I make a "GET" request to "/pet/88"

* The response code should be "200"

* The response body should not be empty

* The response body contains "TestPet1"