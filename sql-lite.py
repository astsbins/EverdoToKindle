#%%
import sqlite3
import os

#%%


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

    for row in rows:
        print(f"{row[0]}   {xstr(row[1])}")

def main():
    database = "db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        select_next_tasks(conn)

if __name__ == '__main__':
    main()