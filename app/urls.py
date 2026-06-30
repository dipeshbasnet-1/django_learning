
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("student/list", views.student_list, name="students"),
    path("student/<int:id>/", views.student_detail, name="student_detail"),
    path("student/update/<int:id>/", views.update_student, name="update_student"),
    path("student/add", views.add_student, name="add_students"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
