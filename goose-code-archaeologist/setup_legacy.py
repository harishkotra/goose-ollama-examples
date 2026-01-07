# setup_legacy.py
import os

CONTENT = """
import math

def f1(n):
    if n <= 1: return n
    return f1(n-1) + f1(n-2)

def f2(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def p(data):
    m = sum(data) / len(data)
    v = sum((x - m) ** 2 for x in data) / len(data)
    return math.sqrt(v)
"""

with open("legacy_math.py", "w") as f:
    f.write(CONTENT.strip())

print("✅ Created legacy_math.py with undocumented spaghetti code.")
