import uuid
import time
from openai import OpenAI

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
 
    def is_owner(self):
        if self.role == "Owner":
            return True
        return False
 
    def is_employee(self):
        if self.role == "Employee":
            return True
        return False
class Owner(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Owner")
 
class Employee(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Employee")

def find_user(users, username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            found_user = User(u["username"], u["password"], u["role"])
            return found_user
    return None
 
 
def username_taken(users, username):
    for u in users:
        if u["username"] == username:
            return True
    return False