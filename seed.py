import json
import sqlite3


def call_db(query: str, values:list):
    print(query)
    connection = sqlite3.connect("toytable.db")
    cursor = connection.cursor()
    res = cursor.execute(query, values) #OBS! Executescript is for many. 
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data


with open ("seed.json", "r") as seed:
    data = json.load(seed)

    for record in data:
        print("Printing record...")
        print(record)   
        call_db("INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES (?, ?, ?, ?, ?, ?)", 
        [record.get("first_name"), record.get("last_name"), record.get("email"), record.get("us_state"), record.get("birthdate"), record.get("major")])
