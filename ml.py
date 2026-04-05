from transformers import pipeline

classifier = pipeline("zero-shot-classification")

LABELS = ["KYC", "Payment", "GST", "Notification", "Email", "Auth", "Storage"]

KEYWORDS = {
    "KYC": ["aadhaar", "pan", "identity", "verification"],
    "Payment": ["payment", "transaction", "gateway"],
    "GST": ["gst", "invoice", "tax"],
    "Notification": ["otp", "sms", "notify"],
    "Email": ["email", "mail", "confirmation"],
    "Auth": ["login", "signup", "authentication"],
    "Storage": ["upload", "file", "document"]
}

def keyword_boost(text, service):
    text = text.lower()
    for word in KEYWORDS.get(service, []):
        if word in text:
            return 0.2
    return 0

def detect_services(text):
    result = classifier(text, LABELS)

    services = []
    total_score = sum(result["scores"])

    for label, score in zip(result["labels"], result["scores"]):
        normalized = score / total_score
        boosted = normalized + keyword_boost(text, label)

        if boosted > 0.25:
            services.append({
                "service": label,
                "confidence": round(boosted, 2),
                "priority": "HIGH" if boosted > 0.6 else "MEDIUM"
            })

    return services