import requests
import logging
import os
import json
from datetime import datetime

log_path = os.path.abspath(
    "F:/Programming/ELK_stack/random_user/log/random_user.log")

# Setup logger
logger = logging.getLogger("random_user_logger")
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

file_handler = logging.FileHandler(log_path, mode='a')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def fetch_random_user():
    try:
        res = requests.get("https://randomuser.me/api/")
        res.raise_for_status()
        data = res.json()["results"][0]

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "status": res.status_code,
            "name": f"{data['name']['first']} {data['name']['last']}",
            "email": data["email"],
            "gender": data["gender"],
            "country": data["location"]["country"]
        }

        json_log = json.dumps(log_entry)
        logger.info(json_log)

    except Exception as e:
        logger.error(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "status": 500,
            "error": str(e)
        }))


fetch_random_user()
