from database import users
from models import User

def register_user(username, password):
    if username in users:
        return False
    users[username] = User(username, password)
    return True

def login_user(username, password):
    user = users.get(username)
    if user and user.password == password:
        return True
    return False