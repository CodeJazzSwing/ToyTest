import json
import sqlite3

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


data_from_college = call_db("SELECT * FROM college")



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
        call_db(create_table, college["first_name"], college["last_name"], college["email"], college["us_state"], college["birthdate"], ["major"])


