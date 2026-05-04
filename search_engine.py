import payment_gateway
import email_service
import analytics

def execute_search(query):
    results = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Smartphone"}
    ]
    analytics.track_event(None, "search_performed", {"query": query})
    return results

def checkout(user_id, amount, card_number):
    res = payment_gateway.process_payment(amount, card_number, "12/25")
    if res["status"] == "success":
        email_service.send_welcome_email("user@example.com", "User")
        analytics.track_event(user_id, "checkout_success", {"amount": amount})
    return res
