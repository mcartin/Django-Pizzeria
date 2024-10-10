from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('signup.html', views.signup, name="signup"),
   path('log_in.html', views.log_in, name="log_in"),
   path('logout', views.logoutUser, name="logout"),
   path('homePage.html', views.homePage, name="homePage"),
   path('previous_orders.html', views.previous_orders, name="previous_orders"),
   path('create_pizza.html', views.create_pizzas, name="create_pizza"),
   path('created.html', views.created, name="created"),
   path('confirmation.html', views.confirmation, name="confirmation")
]