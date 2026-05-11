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