import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="postgres", user='postgres', password='Sang@123', host='localhost', port='5050'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = '''CREATE database my_db''';

# Creating a database
cursor.execute(sql)
print("Database created successfully........")

# Closing the connection
conn.close()
