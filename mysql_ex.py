import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Sang@123',
                             database='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('sngt@gmail.com', '1234'))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `user` WHERE `email`=%s"
        cursor.execute(sql, ('sngt@gmail.com',))
        result = cursor.fetchone()
        print(result)