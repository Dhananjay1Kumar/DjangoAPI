from django.urls import path
from .views import EmployeeList, EmployeeDetail


app_name = 'apiview_app'

urlpatterns = [
         path('emp/', EmployeeList.as_view()),
         path('emp/<int:id>/', EmployeeDetail.as_view())
]
