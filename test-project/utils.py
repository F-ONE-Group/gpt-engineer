from f_one_core_utilities.models.communication.email.email import SendEmailPayload

import subprocess

def launch_calculator():
    """
    Launches the calculator.exe in Windows.
    """
    subprocess.Popen('calc.exe')

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def create_email_payload(result):
    """
    Creates a payload for sending an email with the result of the addition.
    """
    email_subject = "Addition Result"
    email_body = f"The result of 3 + 3 is {result}"
    recipients = ["a.mosca@f-one.group"]
    is_html = False

    return SendEmailPayload(email_subject, email_body, recipients, is_html)
