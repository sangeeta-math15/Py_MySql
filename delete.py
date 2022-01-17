import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="my_db", user='postgres', password='Sang@123', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Retrieving contents of the table
print("Contents of the table: ")
cursor.execute('''select * from employee''')
print(cursor.fetchall())

# Deleting records
cursor.execute('''delete from employee where age>28''')

# Retrieving data after delete
print("Contents of the table after delete operation ")
cursor.execute("select * from employee")
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
