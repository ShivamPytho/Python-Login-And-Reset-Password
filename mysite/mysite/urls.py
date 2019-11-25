from django.contrib import admin
from django.urls import path,include

from mysite.myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')), 
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),


]
