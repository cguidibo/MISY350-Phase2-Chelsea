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
 