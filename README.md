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