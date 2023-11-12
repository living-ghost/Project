from django.urls import path
from .views import index, sign_up, login_view

urlpatterns = [
    path('', index, name='index'),
    path('registration/', sign_up, name='registration'),
    path('sign_in', login_view, name='login_view')
]