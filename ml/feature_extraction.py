# Directory: novaTask/ml/feature_extraction.py

import re
from datetime import datetime


def extract_features(payload):
    action = payload.get("action", "")
    data = payload.get("data", {})
    context = payload.get("user_context", {})

    features = {}
    features["action_type"] = hash(action) % 1000
    features["hour_of_day"] = datetime.utcnow().hour

    email = data.get("email", "")
    username = data.get("username", data.get("user_name", ""))
    features["email_length"] = len(email)
    features["username_length"] = len(username)
    features["email_domain"] = hash(email.split('@')[-1]) % 1000 if '@' in email else 0
    features["has_numbers_in_username"] = 1 if re.search(r'\\d', username) else 0

    title = data.get("title", "")
    desc = data.get("description", "")
    features["title_length"] = len(title)
    features["desc_length"] = len(desc)
    features["word_count"] = len(desc.split())

    name = data.get("tenant_name", "")
    features["tenant_name_length"] = len(name)

    ip = context.get("ip", "")
    features["ip_numeric"] = sum(int(x) for x in ip.split('.') if x.isdigit()) if ip else 0
    features["device_length"] = len(context.get("device", ""))

    return features