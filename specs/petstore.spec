# Specification Heading

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run

    gauge run specs/petstore.spec


## Ensure pet inventory is available

tags: trusted-device, add-device, parallel

* When I make a GET request to "/store/inventory"

* The response code should be "200"

* The response body contains "available"