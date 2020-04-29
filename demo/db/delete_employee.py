import sqlite3

con = sqlite3.connect(r"c:\classroom\apr6\hr.db")
cur = con.cursor()
id = input("Enter Id:")
cur.execute("delete from employees where id = ?", (id,))
if cur.rowcount == 1:
    print("Deleted successfully!")
else:
    print("Sorry! Employee Id Not Found!")

con.commit()
cur.close()
con.close()
