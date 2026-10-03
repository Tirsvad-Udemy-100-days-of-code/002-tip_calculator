def bill_per_person(bill: float, tip_percent: int, people: int) -> float:
    """Return what each person pays, rounded to two decimal places."""
    if people < 1:
        raise ValueError("people must be at least 1")
    tip_as_percent = tip_percent / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    return round(total_bill / people, 2)
