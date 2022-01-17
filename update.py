import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="my_db", user='postgres', password='Sang@123', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Fetching all the rows before the update
print("content of the employee table:- ")
sql = '''select * from employee'''
cursor.execute(sql)
print(cursor.fetchall())

# Updating the records
sql = "update employee set age = age + 1 where sex = 'F'"
cursor.execute(sql)
print("Table updated...... ")

# Fetching all the rows after the update
print("Contents of the employee table after the update operation: ")
sql = '''select * from employee'''
cursor.execute(sql)
print(cursor.fetchall())

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
