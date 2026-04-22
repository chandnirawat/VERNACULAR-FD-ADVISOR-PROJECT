from bank_api import get_bank_rates

def recommend_fd(amount, duration, risk):
    banks = get_bank_rates()
    best = None

    for bank in banks:
        if bank["risk"] == risk:
            interest = amount * (bank["rate"]/100) * duration

            if not best or interest > best["interest"]:
                best = {
                    "bank": bank["bank"],
                    "rate": bank["rate"],
                    "interest": interest
                }

    return best

