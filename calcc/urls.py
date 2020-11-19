from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name='home'),
        path('adds',views.adds,name = 'adds'),
        path('sub',views.sub,name = 'sub'),
        path('mul',views.mul,name = 'mul'),
        path('div',views.div,name = 'div')
    ]