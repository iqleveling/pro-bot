users = {}

def get_user(uid):
    if uid not in users:
        users[uid] = {
            "queue": [],
            "mode": None
        }
    return users[uid]
