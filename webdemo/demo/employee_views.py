from django.shortcuts import render
import sqlite3


def get_employees(request):
    con = sqlite3.connect(r"c:\classroom\apr6\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees order by salary")
    employees = cur.fetchall()
    con.close()
    return render(request, 'list_employees.html', {'employees': employees})