import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004",
    database="my_first_db"
)
if mydb.is_connected():
    print("the cntn has been established")
    c=mydb.cursor()
    query="select * from students"
    c.execute(query)
    rows=c.fetchall()
    for i in rows:
        print("id is {}".format(i[0]))
        print("name is {}".format(i[1]))
        print("age is {}".format(i[2]))
        print("--------------------")