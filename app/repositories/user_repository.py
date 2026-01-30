import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import Optional

USERS_FILE = Path("data/users.json")


def _read_data():
    if not USERS_FILE.exists():
        return {"users": []}

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_data(data: dict):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_user_by_email(email: str) -> Optional[dict]:
    data = _read_data()
    email = email.lower()

    for user in data["users"]:
        if user["email"] == email:
            return user

    return None


def get_user_by_id(user_id: str) -> Optional[dict]:
    data = _read_data()

    for user in data["users"]:
        if user["id"] == user_id:
            return user

    return None


def create_user(email: str, hashed_password: str) -> dict:
    data = _read_data()
    email = email.lower()

    new_user = {
        "id": str(uuid.uuid4()),
        "email": email,
        "hashed_password": hashed_password,
        "created_at": datetime.utcnow().isoformat()
    }

    data["users"].append(new_user)
    _write_data(data)

    return new_user
