import datetime

def log_event(text, services):
    with open("logs.txt", "a") as f:
        f.write("\n---\n")
        f.write(f"Time: {datetime.datetime.now()}\n")
        f.write(f"Input: {text}\n")
        f.write(f"Detected: {services}\n")