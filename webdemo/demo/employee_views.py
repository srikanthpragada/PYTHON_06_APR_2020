from django.shortcuts import render, redirect
from .forms import EmployeeForm
import sqlite3


def get_employees(request):
    con = sqlite3.connect(r"c:\classroom\apr6\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees order by salary")
    employees = cur.fetchall()
    con.close()
    return render(request, 'list_employees.html', {'employees': employees})


def add_employee(request):
    if request.method == "GET":
        emp_form = EmployeeForm()
        return render(request, 'add_employee.html', {'form': emp_form})
    else:  # POST
        emp_form = EmployeeForm(request.POST)
        if emp_form.is_valid():
            fullname = emp_form.cleaned_data['fullname']
            if 'job' in emp_form.cleaned_data:  # optional field
                job = emp_form.cleaned_data['job']
            else:
                job = None
            salary = emp_form.cleaned_data['salary']

            # insert row into table
            try:
                with sqlite3.connect(r"c:\classroom\apr6\hr.db") as con:
                    cur = con.cursor()
                    cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                                (fullname, job, salary))
                    con.commit()

                return redirect('/demo/employees')
            except Exception as ex:
                print("Error : ", ex)
                return render(request, 'add_employee.html',
                              {'form': emp_form, 'message': 'Sorry! Could not add employee!'})
        else:
            return render(request, 'add_employee.html',
                          {'form': emp_form, 'message': 'Please correct data and resubmit form!'})
