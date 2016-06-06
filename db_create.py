# db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as conn:
    c = conn.cursor()

    # drop table, if exists
    c.execute("DROP TABLE if exists tasks")

    # create tasks table
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, due_date TEXT NOT NULL, priority TEXT NOT NULL,
                status INTEGER NOT NULL)""")

    # insert dummy data into table
    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish this tutorial", "6/10/16", 10, 1)'
    )

    c.execute(
        'INSERT INTO tasks (name, due_date, priority, status)'
        'VALUES("Finish Real Python Course 3", "6/17/16", 10, 1)'
    )

