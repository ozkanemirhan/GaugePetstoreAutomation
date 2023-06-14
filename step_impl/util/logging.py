import logger_lib.logger as log
from util.constants import Bcolors
import datetime

logger = log.getLogger(__name__)


def error_and_throw_exception(msg, **kwargs):
    error_str = ""
    if "response" in kwargs:
        response = kwargs["response"]
        fail_name = str('{} {} {}'.format(
            response.status_code,
            response.request.method,
            response.request.url))
        fail_name_error = (
            Bcolors.FAIL + fail_name + Bcolors.ENDC)
        error_str += (fail_name_error + "\n")

        if response.request.headers is not None:
            request_headers = str(response.request.headers)
            headline = "REQUEST HEADERS : "
            message = request_headers
            error = (
                Bcolors.OKBLUE + headline +
                Bcolors.WARNING + message + Bcolors.ENDC)
            error_str += (error + "\n")

        if response.request.body is not None:
            request_body = str(response.request.body)
            headline = "REQUEST BODY : "
            message = request_body
            error = (
                Bcolors.OKBLUE + headline +
                Bcolors.WARNING + message + Bcolors.ENDC)
            error_str += (error + "\n")

        if response.headers is not None:
            response_headers = str(response.headers)
            headline = "RESPONSE HEADERS : "
            message = response_headers
            error = (
                Bcolors.OKBLUE + headline +
                Bcolors.WARNING + message + Bcolors.ENDC)
            error_str += (error + "\n")

        if response.text is not None:
            response_text = str(response.text)
            headline = "RESPONSE TEXT : "
            message = response_text
            error = (
                Bcolors.OKBLUE + headline +
                Bcolors.WARNING + message + Bcolors.ENDC)
            error_str += (error + "\n")

        headline = "RESPONSE TIME : "
        message = str(datetime.datetime.now().time())
        error = (
            Bcolors.FAIL + headline +
            Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (error + "\n")

        headline = "Message : "
        message = msg
        logger_text = (
            Bcolors.FAIL + headline +
            Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (logger_text + "\n")
    else:
        if kwargs:
            headline = "Message : "
            response_headline = "\nResponse : "
            message = msg
            logger_text = (
                Bcolors.FAIL + headline +
                Bcolors.WARNING + message + Bcolors.FAIL +
                response_headline + Bcolors.WARNING +
                str(kwargs) + Bcolors.ENDC)
        else:
            headline = "Message : "
            message = msg
            logger_text = (
                Bcolors.FAIL + headline +
                Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (logger_text + "\n")
    logger.error_and_throw_exception(error_str)


def info(msg, **kwargs):
    logger.info(msg, **kwargs)


def warn(msg, **kwargs):
    logger.warn(msg, **kwargs)


def print_request(response):
    error_str = ""
    fail_name = str('{} {} {}'.format(
        response.status_code,
        response.request.method,
        response.request.url))
    fail_name_error = (
        Bcolors.OKBLUE + fail_name + Bcolors.ENDC)
    error_str += (fail_name_error + "\n")

    if response.request.headers is not None:
        request_headers = str(response.request.headers)
        headline = "REQUEST HEADERS : "
        message = request_headers
        error = (
            Bcolors.OKBLUE + headline +
            Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (error + "\n")

    if response.request.body is not None:
        request_body = str(response.request.body)
        headline = "REQUEST BODY : "
        message = request_body
        error = (
            Bcolors.OKBLUE + headline +
            Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (error + "\n")

    if response.headers is not None:
        response_headers = str(response.headers)
        headline = "RESPONSE HEADERS : "
        message = response_headers
        error = (
            Bcolors.OKBLUE + headline +
            Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (error + "\n")

    if response.text is not None:
        response_text = str(response.text)
        headline = "RESPONSE TEXT : "
        message = response_text
        error = (
            Bcolors.OKBLUE + headline +
            Bcolors.WARNING + message + Bcolors.ENDC)
        error_str += (error + "\n")

    headline = "RESPONSE TIME : "
    message = str(datetime.datetime.now().time())
    error = (
        Bcolors.OKBLUE + headline +
        Bcolors.WARNING + message + Bcolors.ENDC)
    error_str += (error + "\n")
    print(error_str)
