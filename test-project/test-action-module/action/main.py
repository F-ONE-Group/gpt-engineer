from .utils import get_exchange_rate, convert_to_eur, calculate_ratio, calculate_elapsed_days, get_validation_rules

def process_payload(payload):
    """
    This function processes the payload.
    """
    exchange_rate = get_exchange_rate(payload.fhs_date, payload.currency)
    amount_in_eur = convert_to_eur(payload.estimate_amount_of_damage, exchange_rate)
    ratio = calculate_ratio(amount_in_eur, payload.claim_amount)
    elapsed_days = calculate_elapsed_days(payload.first_written_claim, payload.damage_date, payload.fhs_date, payload.reason)
    validation_rules = get_validation_rules(payload.client)

    return {
        'exchange_rate': exchange_rate,
        'amount_in_eur': amount_in_eur,
        'ratio': ratio,
        'elapsed_days': elapsed_days,
        'validation_rules': validation_rules,
    }
