import sqlite3

conn = sqlite3.connect("netflix.db")  
cur = conn.cursor()


cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cur.fetchall()]
print("Tables:", tables)


for table in tables:
    print(f"\n--- {table} ---")
    cur.execute(f"SELECT * FROM {table}")
    for row in cur.fetchall():
        print(row)

conn.close()