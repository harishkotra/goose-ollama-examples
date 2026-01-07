# setup_users.py
import csv
import random

FILENAME = "users.csv"

def generate_csv():
    headers = ["id", "full_name", "email_address", "phone_number", "age", "subscription_tier"]
    
    data = [
        [1, "Alice Wonderland", "alice.w@example.com", "555-0101", 34, "Premium"],
        [2, "Bob Builder", "bob.b@construction.co", "555-0199", 29, "Free"],
        [3, "Charlie Chocolate", "factory_owner@wonka.net", "555-0500", 55, "Premium"],
        [4, "Dana Scully", "trust_no_one@fbi.gov", "202-555-0177", 41, "Standard"],
        [5, "Eve Hacker", "eve@evilcorp.com", "000-000-0666", 25, "Free"]
    ]

    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    
    print(f"✅ Generated {FILENAME} with 5 rows of sensitive data.")

if __name__ == "__main__":
    generate_csv()
