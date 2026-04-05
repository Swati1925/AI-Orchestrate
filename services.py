REGISTRY = {
    "KYC": [
        {"provider": "Signzy", "adapter": "KYC_Adapter", "version": "v2", "endpoint": "/kyc/verify"},
        {"provider": "Karza", "adapter": "KYC_Adapter", "version": "v1", "endpoint": "/kyc/basic"}
    ],
    "Payment": [
        {"provider": "Razorpay", "adapter": "Payment_Adapter", "version": "v3", "endpoint": "/payments"},
        {"provider": "Stripe", "adapter": "Payment_Adapter", "version": "v2", "endpoint": "/charge"}
    ],
    "GST": [
        {"provider": "Karza", "adapter": "GST_Adapter", "version": "v1", "endpoint": "/gst/validate"}
    ],
    "Notification": [
        {"provider": "Twilio", "adapter": "Notification_Adapter", "version": "v1", "endpoint": "/send_sms"},
        {"provider": "Firebase", "adapter": "Notification_Adapter", "version": "v1", "endpoint": "/send_push"}
    ],
    "Email": [
        {"provider": "SendGrid", "adapter": "Email_Adapter", "version": "v2", "endpoint": "/send_email"},
        {"provider": "Amazon SES", "adapter": "Email_Adapter", "version": "v1", "endpoint": "/email"}
    ],
    "Auth": [
        {"provider": "Auth0", "adapter": "Auth_Adapter", "version": "v2", "endpoint": "/auth/login"},
        {"provider": "Firebase Auth", "adapter": "Auth_Adapter", "version": "v1", "endpoint": "/login"}
    ],
    "Storage": [
        {"provider": "AWS S3", "adapter": "Storage_Adapter", "version": "v1", "endpoint": "/upload"},
        {"provider": "Cloudinary", "adapter": "Storage_Adapter", "version": "v1", "endpoint": "/upload_image"}
    ]
}

THRESHOLD = 0.6

def get_service_config(service_name, confidence):
    options = REGISTRY.get(service_name, [])

    if not options:
        return None

    if confidence > THRESHOLD:
        return options[0]  # premium
    else:
        return options[-1]  # fallback