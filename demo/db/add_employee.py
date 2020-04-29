import sqlite3

con = sqlite3.connect(r"c:\classroom\apr6\hr.db")
cur = con.cursor()
name = input("Enter name :")
job = input("Enter job :")
salary = input ("Enter salary :")
cur.execute("insert into employees(fullname,job,salary) values(?,?,?)", (name,job,salary))
con.commit()
cur.close()
con.close()

