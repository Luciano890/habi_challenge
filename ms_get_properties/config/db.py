"""DB connection configuration"""
from settings import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_SCHEMA,
)

import mysql.connector

config = {
  'host': DB_HOST,
  'port': DB_PORT,
  'user': DB_USER,
  'password': DB_PASSWORD,
  'database': DB_SCHEMA
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
