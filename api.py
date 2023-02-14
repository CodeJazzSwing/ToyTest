# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/msg")
# def read_root():
#     return {"Hello": "World"}

import sqlite3

connection = sqlite3.connect("toytable.db")


def call_db(query: str):
    print(query)
    connection = sqlite3.connect("toytable.db")
    cursor = connection.cursor()
    res = cursor.executescript(query) #OBS! Changed this to 'executescript' from execute. Executescript is for many. 
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data

# query = """
# CREATE TABLE IF NOT EXISTS college(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     first_name VARCHAR (255),
#     last_name VARCHAR (255),
#     email VARCHAR (100),  
# 	us_state VARCHAR (50), 
# 	birthdate DATE,
# 	major VARCHAR (50)
# );
# """
# data = call_db(query)

query = """
INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES ('Donald', 'Duck', 'donald@aol.com', 'OR', '1995-05-12', 'Philosophy');
INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES ('Mighty', 'Mouse', 'mighty@aol.com', 'WA', '1995-03-23', 'Engineering');
INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES ('Minnie', 'Mus', 'minne@aol.com', 'NV', '1993-12-02', 'Communication');
INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES ('Wendy', 'Testy', 'winnie@aol.com', 'CA', '1992-03-22', 'Philosophy');
INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES ('Betty', 'Boop', 'betty@aol.com', 'OR', '1981-02-25', 'Science');
 
"""

data = call_db(query)


print(data)

# Connect to DB. 2) Get requested data. 3) Return data.
# 