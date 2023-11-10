import requests
from datetime import datetime
from f_one_core_utilities import date_utils

def get_exchange_rate(date, currency):
    """
    This function gets the exchange rate for a given date and currency.
    """
    response = requests.get(f"https://api.exchangerate.host/convert?from={currency}&to=EUR&date={date}")
    response.raise_for_status()
    return response.json()['rates']['EUR']

def convert_to_eur(amount, exchange_rate):
    """
    This function converts a given amount to EUR using the provided exchange rate.
    """
    return amount * exchange_rate

def calculate_ratio(amount_in_eur, claim_amount):
    """
    This function calculates the ratio between the converted amount and the claim amount.
    """
    return amount_in_eur / claim_amount

def calculate_elapsed_days(first_written_claim, damage_date, fhs_date, reason):
    """
    This function calculates the elapsed days between the first written claim and the damage date.
    If the damage date is None or the reason is 'investigation', it uses the fhs date.
    """
    if damage_date is None or reason == 'investigation':
        damage_date = fhs_date
    return date_utils.days_between(first_written_claim, damage_date)

def get_validation_rules(client):
    """
    This function returns the validation rules based on the client.
    """
    if client == 'Byrd':
        return 'validation_rules_byrd'
    elif client == '7Senders':
        return 'validation_rules_7s'
    else:
        raise ValueError(f"Unknown client: {client}")
