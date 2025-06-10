#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os

# Define and resolve absolute path to the database
db_relative_path = "Database.db"
db_path = os.path.abspath(db_relative_path)

# Delete existing database file if it exists
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Deleted existing database at: {db_path}")
else:
    print(f"No existing database found at: {db_path}")

# Show where the new DB will be created
print(f"Creating new database at: {db_path}")

# Connect to the (new) database
con = lite.connect(db_path)

with con:
    cur = con.cursor()

    # Create data for the user table
    cur.execute("CREATE TABLE users(UserId INTEGER PRIMARY KEY AUTOINCREMENT, UserName TEXT, Password TEXT)")
    cur.execute("INSERT INTO users VALUES(1,'admin','admin')")
    cur.execute("INSERT INTO users VALUES(2,'user','user')")

    # Create some data for pageinformation
    cur.execute("CREATE TABLE notes(MessageId INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Body TEXT, UserId INT)")
    cur.execute("INSERT INTO notes VALUES(1,'First note','This is a secret message that should not be shown to ordinary folks',1)")

    # Create password reset table
    cur.execute("CREATE TABLE passwordForget(UserName TEXT, ResetToken TEXT)")

    con.commit()
