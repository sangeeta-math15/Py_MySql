import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="my_db", user='postgres', password='Sang@123', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Retrieving single row
sql = '''select * from employee inner join contact on employee.emp_id = contact.c_id'''

# Executing the query
cursor.execute(sql)

# Fetching 1st row from the table
result = cursor.fetchall()
for i in result:
    print(i)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
