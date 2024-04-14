import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO prompts (initial, msg, answer) VALUES (?, ?, ?)",
            ('This is a test initial prompt', 'This is a test message', 'This is a test answer')
            )

connection.commit()
connection.close()