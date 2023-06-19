# GaugePetstoreAutomation

This repository contains python-gauge tests for the Petstore project


## Prerequest

* Python3.10.x
* pip (pip3)


## Create and Install Requirements
Here are the steps for Windows to create and install requirements using a virtual environment:

1. Create a virtual environment by running the following command:

   ```shell
   python -m venv venv
   ```

   This command creates a virtual environment named "venv" in the current directory.

2. Activate the virtual environment by running the following command:

   ```shell
   venv\Scripts\Activate.ps1
   ```
    For MAC:

        ```bash
        source venv/bin/activate
        ```

   This command activates the virtual environment. You will notice that the command prompt prefix changes to indicate that you are now inside the virtual environment.

3. Install the project dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

   This command installs the required packages specified in the `requirements.txt` file. Make sure the `requirements.txt` file is present in your project directory and contains the necessary package dependencies.

4. To deactivate the virtual environment and return to the regular command prompt, simply run the following command:

   ```shell
   deactivate
   ```

   This command deactivates the virtual environment.

Install the necessary Gauge Python dependencies by running:
### gauge install python

This command installs the Gauge Python plugin and any other required dependencies.

## Run a Gauge specification with an environment

You can use the -env flag to load an environment when Gauge runs a specification. If -env is not specified, then the `default` environment is loaded during run time.

```bash
gauge run --env <name_of_env> specs
```

<name_of_env> = ["petstore-dev, petstore-int"]
like 
```bash
gauge run --env petstore-dev specs
OR
gauge run --env petstore-int specs
```
For more execution options see [here](https://docs.gauge.org/execution.html)

## To run Gauge automation tests by tags

To run Gauge automation tests by tags, you can use the `--tags` option when executing the Gauge command. The `--tags` option allows you to specify one or more tags to include or exclude during test execution.

Here's an example command to run Gauge tests by tags:

```shell
gauge run --tags=<tag_expression>
```

Replace `<tag_expression>` with the desired tag expression. The tag expression can be a single tag or a combination of tags using logical operators such as `and`, `or`, and `not`. Here are a few examples:

- Run tests with a single tag:
  ```shell
  gauge run --tags=tagname
  ```