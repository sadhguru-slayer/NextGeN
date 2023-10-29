from Applications import views
from django.urls import path

urlpatterns = [
    #Home
    path('',views.home,name="home"),
    path('apply',views.apply,name="apply")
]
