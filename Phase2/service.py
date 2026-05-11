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

def register_user(users, username, password, confirm):
    if username == "" or password == "" or confirm == "":
        return None, "Please fill in all fields."
    if password != confirm:
        return None, "Passwords do not match."
    if len(password) < 4:
        return None, "Password must be at least 4 characters."
    if username_taken(users, username):
        return None, "That username is already taken."
 
    new_user = {"username": username, "password": password, "role": "Employee"}
    users.append(new_user)
    return new_user, "Account created successfully."

def find_item_by_id(inventory, item_id):
    for item in inventory:
        if item["item_id"] == item_id:
            return item
    return None
 
 
def add_item(inventory, name, price, stock, category):
    if name == "":
        return None, "Please enter a product name."
 
    for item in inventory:
        if item["name"].lower() == name.lower():
            return None, "A product with that name already exists."
 
    if len(inventory) == 0:
        new_id = 1
    else:
        new_id = max(item["item_id"] for item in inventory) + 1
 
    new_item = {
        "item_id": new_id,
        "name": name,
        "price": round(price, 2),
        "stock": stock,
        "category": category,
        "flagged": False
    }
    inventory.append(new_item)
    return new_item, "Product added."
 
 
def update_item(inventory, item_id, price, add_stock, category):
    item = find_item_by_id(inventory, item_id)
    if item is None:
        return False, "Item not found."
 
    item["price"] = round(price, 2)
    item["stock"] = item["stock"] + add_stock
    item["category"] = category
 
    if item["stock"] >= 5:
        item["flagged"] = False
 
    return True, item["name"] + " updated."

def delete_item(inventory, item_id):
    item = find_item_by_id(inventory, item_id)
    if item is None:
        return False, "Item not found."
 
    inventory.remove(item)
    return True, "Product removed."
 
 
def toggle_flag(inventory, item_id):
    item = find_item_by_id(inventory, item_id)
    if item is None:
        return False
    if item["flagged"] == True:
        item["flagged"] = False
    else:
        item["flagged"] = True
    return True
 
 
def place_sale(inventory, sales, item_id, quantity, username):
    item = find_item_by_id(inventory, item_id)
    if item is None:
        return None, "Item not found."
    if item["stock"] < quantity:
        return None, "Not enough stock. Only " + str(item["stock"]) + " available."
 
    item["stock"] = item["stock"] - quantity
 
    if item["stock"] < 5:
        item["flagged"] = True
 
    total = round(item["price"] * quantity, 2)
 