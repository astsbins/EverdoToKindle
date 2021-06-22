import sqlite3
from flask import Flask

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)

    return conn

def xstr(s):
    #Change None type to empty string. Thank you 
    if s is None:
        return ''
    return str(s)

def select_next_tasks(conn):
    """
    Get next tasks that are incomplete
    """
    curr = conn.cursor()
    curr.execute("""
    select title,note from item
    where type == "a" and list == "a" and completed_on IS NULL and parent_id IS NULL
                """)
    rows = curr.fetchall()
    tasks = ""
    for row in rows:
        tasks += f"{row[0]}   {xstr(row[1])} <br>"
    return tasks

app = Flask(__name__)

@app.route("/")
def hello_world():
    conn = create_connection("db")
    with conn:   
        return f"<p>{select_next_tasks(conn)}</p>"



