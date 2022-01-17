import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="my_db", user='postgres', password='Sang@123', host='localhost', port='5432'
)
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Doping employee table if already exists.
cursor.execute("drop table if exists employee")

# Creating table as per requirement
sql = '''create table employee(
   emp_id serial primary key,   
   f_name char(20) not null,
   l_name char(20) not null,
   age int,
   sex char(1),
   income float
)'''
cursor.execute(sql)
print("Table created successfully........")

# Populating the table
insert_stmt = "insert into employee(emp_id,f_name,l_name,age,sex,income) values(%s, %s, %s, %s, %s, %s)"
data = [(6, 'keerthi', 'math', 23, 'F', 4000)]

cursor.executemany(insert_stmt, data)

# Retrieving specific records using the where clause
cursor.execute("SELECT * from EMPLOYEE WHERE AGE <25")
print(cursor.fetchall())

conn.commit()
# Closing the connection
conn.close()
