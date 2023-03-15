from django.urls import path
from . import views

app_name='common' # for redirection purpose

urlpatterns=[
    path('calculator',views.calculator,name='calculator')
]