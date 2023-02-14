#1) Connect to DB. 2) Create query to run pm DB     3) Execute query    4) Package in a repsonse.

from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel


app = FastAPI()

  
@app.get("/all")
def read_root():
    connection = sqlite3.connect("toytable.db")
    cur = connection.cursor()
    query = """
    SELECT * FROM college
    """
    res = cur.execute(query) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data

@app.get("/california")
def read_root():
    connection = sqlite3.connect("toytable.db")
    cur = connection.cursor()
    query = """
    SELECT * FROM college WHERE us_state = 'CA';
    """
    res = cur.execute(query) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data

@app.get("/state/{state_id}")
def read_root(state_id):
    connection = sqlite3.connect("toytable.db")
    cur = connection.cursor()
    res = cur.execute("SELECT * FROM college WHERE us_state = ?", [state_id]) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data


class College(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    us_state: str
    birthdate: str
    major: str


#OBS! This is to PUT info in ThunderClient. Changed majors on TC.  
@app.put("/update_student")
def update_student(student: College):
    connection = sqlite3.connect("toytable.db")
    cur = connection.cursor()
    res = cur.execute("UPDATE college SET major = ? WHERE id = ?", [student.major, student.id]) 
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return data
    
@app.post("/create_student/")
def create_student(student: College):
    connection = sqlite3.connect("toytable.db")
    cur = connection.cursor()
    res = cur.execute("INSERT INTO college (first_name, last_name, email, us_state, birthdate, major) VALUES (?, ?, ?, ?, ?, ?)", 
        [student.first_name, student.last_name, student.email, student.us_state, student.birthdate, student.major])
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    
    return(student)
 

#To delete in TC write in the website....t.ex.: http://127.0.0.1:8000/delete_student/8
@app.delete("/delete_student/{id}")
def delete_student(id: int):
    connection = sqlite3.connect("toytable.db")
    cur = connection.cursor()
    res = cur.execute("DELETE FROM college WHERE id = ?", [id]) 
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return data
