import hashlib
import sqlite3

sql_file = open("db.sqlite3")

working_cursor = sql_file.cursor()