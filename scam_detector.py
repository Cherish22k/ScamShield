import re

def analyze_text(text):
    score = 0
    reasons = []

    # Rule 1: Too good offers
    if re.search(r"(free|100%|₹\d{4,}|win|prize)", text.lower()):
        score += 2
        reasons.append("Too good to be true offer")

    # Rule 2: Urgency words
    if re.search(r"(urgent|hurry|limited time|act now)", text.lower()):
        score += 2
        reasons.append("Uses urgency tactics")

    # Rule 3: Sensitive info request
    if re.search(r"(otp|password|bank|account)", text.lower()):
        score += 3
        reasons.append("Asks for sensitive information")

    # Rule 4: Suspicious URL
    if re.search(r"(bit\.ly|tinyurl|\.xyz|\.top)", text.lower()):
        score += 2
        reasons.append("Suspicious link detected")

    # Final Risk Level
    if score >= 5:
        risk = "HIGH RISK 🔴"
    elif score >= 3:
        risk = "SUSPICIOUS 🟡"
    else:
        risk = "SAFE 🟢"

    return risk, reasons
