from django.contrib import admin
from django.urls import path
from insti import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('attendance/', views.attendance_page, name='attendance'),
    path('payment/', views.payment_page, name='payment'),
    path('role/', views.role_page, name='role'),
    path('report/', views.report_page, name='report'),
    
]
