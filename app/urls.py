
from django.urls import path
from .views import home, about, contact, login, student_list, student_detail

urlpatterns = [
    path('', home, name='home'),
    path("student/", student_list, name="students"),
    path("student/<int:id>/", student_detail, name="student_detail"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]
