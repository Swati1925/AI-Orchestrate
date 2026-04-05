from fastapi import FastAPI
from ml import detect_services
from models import Base, Configuration
from db import engine, SessionLocal
from services import get_service_config
from config_engine import build_config
from logger import log_event
import random

Base.metadata.create_all(bind=engine)

app = FastAPI()

def simulate(service):
    base_latency = {
        "Payment": 200,
        "KYC": 150,
        "GST": 180,
        "Notification": 120,
        "Email": 140,
        "Auth": 130,
        "Storage": 220
    }

    latency = base_latency.get(service, 100) + random.randint(-50, 100)

    failure_probability = {
        "Payment": 0.15,
        "KYC": 0.1,
        "GST": 0.12,
        "Notification": 0.08,
        "Email": 0.07,
        "Auth": 0.1,
        "Storage": 0.12
    }

    status = "failure" if random.random() < failure_probability.get(service, 0.1) else "success"

    return {
        "service": service,
        "status": status,
        "latency_ms": latency
    }

@app.post("/generate")
def generate(text: str, tenant_id: str = "default"):

    services = detect_services(text)
    db = SessionLocal()

    final_configs = []

    for s in services:
        service_data = get_service_config(s["service"], s["confidence"])

        if not service_data:
            continue

        config = build_config(service_data, s["confidence"], tenant_id)
        config["priority"] = s["priority"]

        db_entry = Configuration(
            service=s["service"],
            adapter=service_data["adapter"],
            version=service_data["version"]
        )

        db.add(db_entry)
        final_configs.append(config)

    db.commit()

    log_event(text, services)

    return {
        "summary": {
            "total_services": len(final_configs),
            "tenant_id": tenant_id
        },
        "configs": final_configs,
        "simulation": [simulate(s["service"]) for s in services]
    }