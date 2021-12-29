from django.urls.conf import include
from users import views
from django.urls import path

urlpatterns = [
    path('users', views.all_users),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('product/<str:pk>/', views.productDetails, name='product'),
    path('cart/', views.carts, name='cart'),
   # path('', views.home, name="home"),

]