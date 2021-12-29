from django.urls.conf import include
from users import views
from django.urls import path

urlpatterns = [
    path('users', views.all_users),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
   # path('', views.home, name="home"),

]