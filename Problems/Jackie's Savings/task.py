def final_deposit_amount(*interest, amount=1000):
    for month in interest:
        percentage = float(f"1.0{month}")
        amount = amount * percentage
    return round(amount, 2)

