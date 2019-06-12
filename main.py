from flask import Flask, request
import requests
import datetime
import os

host = os.getenv("LOKI_HOST","loki")
port = os.getenv("LOKI_PORT","3100")
url = f"http://{host}:{port}/api/prom/push"

app = Flask(__name__)

def is_label(key,value):
    # TODO: choose labels carefully
    if key in ["message","@message","extra_data"]:
        return False
    if isinstance(value,str) and len(value) > 50:
        return False
    return True

def make_labels(msgs):
    labels=[]
    for msg in msgs:
        for key in msg.keys():
            value = msg.get(key)
            if is_label(key,value):
                label=f"{key}=\"{value}\""
                labels.append(label)
    return "{"+",".join(labels)+"}"

@app.route("/push",methods=["POST"])
def push():
    logs = request.get_json()
    headers = { 'Content-type': 'application/json' }
    # TODO: add timezone
    curr_datetime = datetime.datetime.now().isoformat('T',timespec='microseconds')
    entries=[]

    for log in logs:
        entry= { 'ts': curr_datetime+'+00:00', 'line': log.get("message")}
        entries.append(entry)

    payload = {
        'streams': [
            {
                'labels': make_labels(logs),
                'entries': entries
            }
        ]
    }

    requests.post(url, json=payload, headers=headers)
    return "ok",200

