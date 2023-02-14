import json
import sqlite3

sqlite3 = ("toytable.db")

create_table = """
INSERT INTO college (
first_name VARCHAR (255),
last_name VARCHAR (255),
email VARCHAR (100),  
us_state VARCHAR (50), 
birthdate DATE,
major VARCHAR (50)
) VALUES (
?, ?
)
"""

with open ("seed.json", "r") as seed:
    data = json.load(seed)

    for toytable in data:
        sqlite3.call_db(create_table, college["first_name"], college["last_name"], college["email"], college["us_state"], college["birthdate"], ["major"])


#TKTKTKTKTTKTKTKTK