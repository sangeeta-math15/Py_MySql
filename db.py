import psycopg2

# connect to db
conn = psycopg2.connect(
    host="localhost",
    database="player_demo",
    user="postgres",
    password="Sang@123"
)
# cursor
cur = conn.cursor()

cur.execute("insert into team(tid, tname, city) values(1,'rcb','bangaluru')")

# cur.execute("select * from player")
rows = cur.fetchall()

for r in rows:
    print(f"pid:{r[0]}  pname:{r[1]}")

conn.cursor()
# close the connection
conn.close()
