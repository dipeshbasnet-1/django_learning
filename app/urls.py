
from django.urls import path
from .views import home
from .views import about

urlpatterns = [
    path('', home),
    path('/about', about)
]