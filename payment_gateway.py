def process_payment(amount, card_number, expiry):
    # Mock payment processing
    if len(card_number) == 16:
        return {"status": "success", "transaction_id": "tx_123456"}
    return {"status": "declined", "reason": "invalid_card"}

def refund_payment(transaction_id):
    return {"status": "success", "message": f"Refund issued for {transaction_id}"}
