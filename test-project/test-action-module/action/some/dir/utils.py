import requests
from datetime import datetime

def get_exchange_rate(date, currency):
    """Function to get the exchange rate from the API"""
    response = requests.get(f'https://api.exchangerate.host/convert?from={currency}&to=EUR&date={date}')
    return response.json()['rates']['EUR']

def convert_to_eur(amount, exchange_rate, claim_amount):
    """Function to convert the estimated amount of damage to EUR and calculate the ratio"""
    converted_amount = amount * exchange_rate
    ratio = converted_amount / claim_amount
    return converted_amount, ratio

def calculate_elapsed_days(date1, date2):
    """Function to calculate the elapsed days between two dates"""
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days

def process_business_rules(client):
    """Function to process the business rules"""
    if client == 'Byrd':
        return 'validation_rules_byrd'
    elif client == '7Senders':
        return 'validation_rules_7s'
    else:
        return 'validation_rules_default'