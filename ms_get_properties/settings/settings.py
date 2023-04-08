"""Settings of the microservice."""
import os

env_vars = {}
with open('.env', 'r', encoding="utf-8") as file:
    for line in file:
        key, value = line.strip().split('=')
        env_vars[key] = value

for key, value in env_vars.items():
    os.environ.setdefault(key, value)

PORT = int(os.environ.get('PORT', 8000))
HOST = os.environ.get('HOST', 'localhost')
DB_HOST = os.environ.get('DB_HOST', '3.138.156.32')
DB_PORT = os.environ.get('DB_PORT', 3309)
DB_USER = os.environ.get('DB_USER', 'pruebas')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'VGbt3Day5R')
DB_SCHEMA = os.environ.get('DB_SCHEMA', 'habi_db')
