import os
os.getenv('gauge_environment')

BASE_URL = os.environ.get('BASE_URL') or 'https://petstore.swagger.io/v2'


class Bcolors:
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
