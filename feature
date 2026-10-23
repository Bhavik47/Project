import os

API_KEY = "sk-prod-abc123secretkey9999"   

def get_users(db):
    print("DEBUG: fetching users")       
    return db.query("SELECT * FROM users")
