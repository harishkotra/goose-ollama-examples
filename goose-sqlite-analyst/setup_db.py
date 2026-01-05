import sqlite3
import random
from datetime import datetime, timedelta

DB_NAME = "app_logs.db"

def create_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Create Tables
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, role TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY, user_id INTEGER, timestamp TEXT, level TEXT, message TEXT,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')

    # Seed Users
    users = [
        ("Alice Smith", "alice@example.com", "admin"),
        ("Bob Jones", "bob@example.com", "viewer"),
        ("Charlie Day", "charlie@example.com", "editor"),
        ("Dana White", "dana@example.com", "viewer")
    ]
    c.executemany("INSERT INTO users (name, email, role) VALUES (?,?,?)", users)
    conn.commit()

    # Seed Logs
    log_levels = ["INFO", "WARNING", "ERROR"]
    messages = {
        "INFO": ["User logged in", "Page view: /dashboard", "Report generated", "Settings updated"],
        "WARNING": ["Slow query detected", "Disk usage > 80%", "API rate limit approaching"],
        "ERROR": ["Database connection timeout", "NullPointerException", "Payment gateway failure 500", "Failed to load buffer"]
    }

    logs = []
    base_time = datetime.now()
    
    # Generate 100 random logs
    for i in range(100):
        uid = random.randint(1, 4)
        level = random.choices(log_levels, weights=[70, 20, 10])[0]
        msg = random.choice(messages[level])
        time_str = (base_time - timedelta(hours=random.randint(0, 48))).isoformat()
        
        logs.append((uid, time_str, level, msg))

    c.executemany("INSERT INTO logs (user_id, timestamp, level, message) VALUES (?,?,?,?)", logs)
    conn.commit()
    conn.close()
    print(f"✅ Generated {DB_NAME} with dummy data.")

if __name__ == "__main__":
    create_db()
