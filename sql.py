import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

#create the table name class section marks
table_info="""
create table student(name varchar(20), class varchar(20),
section varchar(20), marks int);
"""

cursor.execute(table_info)

##insert some more data into the table

cursor.execute("insert into student values('John', '10th', 'A', 85)")
cursor.execute("insert into student values('Alice', '10th', 'B', 90)")
cursor.execute("insert into student values('Bob', '9th', 'A', 75)")
cursor.execute("insert into student values('Eve', '9th', 'B', 80)")


##display the all records

print("Inserted records are:")
data=cursor.execute("select * from student")
for row in data:
    print(row)

##close the connection
connection.commit()
connection.close()
