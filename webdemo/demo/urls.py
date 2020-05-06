from django.urls import path
from . import views, employee_views, class_views


urlpatterns = [
    # path("home/", views.home),
    path("employees/", employee_views.get_employees),
    path("interest/", views.interest_calculation),
    path("addemployee/", employee_views.add_employee),
    path("ajaxdemo/", views.ajax_demo),
    path("message/", views.message),
    path("about/", class_views.AboutView.as_view()),
]
