from django import forms


class EmployeeForm(forms.Form):
    fullname = forms.CharField(max_length=30, label="Fullname")
    job = forms.CharField(max_length=10, label="Job", required=False)
    salary = forms.IntegerField(label="Salary")

