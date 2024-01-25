from django.urls import path
from .views import computers,contact,index,mans_clothes,womans_clothes
urlpatterns = [
    path('computers/',computers, name='computers'),
    path('contact/', contact, name='contact'),
    path('index/', index, name='index'),
    path('mans_clothes/', mans_clothes, name='mans_clothes'),
    path('womans_clothes/', womans_clothes, name='womans_clothes')
]