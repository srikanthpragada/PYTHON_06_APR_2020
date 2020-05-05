from django.urls import path
from . import views, employee_views


urlpatterns = [
    # path("home/", views.home),
    path("employees/", employee_views.get_employees),
    path("interest/", views.interest_calculation),
    path("addemployee/", employee_views.add_employee),
]
