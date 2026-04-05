def build_config(service_data, confidence, tenant_id):
    return {
        "service": service_data["adapter"],
        "provider": service_data["provider"],
        "version": service_data["version"],
        "endpoint": service_data["endpoint"],
        "tenant_id": tenant_id,
        "confidence": confidence,

        "execution": {
            "timeout_ms": 5000,
            "retry_policy": {
                "max_retries": 3,
                "backoff": "exponential"
            }
        },

        "metadata": {
            "environment": "sandbox",
            "created_by": "AI_Engine"
        }
    }