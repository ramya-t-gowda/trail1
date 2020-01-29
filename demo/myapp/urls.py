from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('index.html', views.index, name='home-page'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('anomalies.html', views.anomalies, name='anomalies'),
    path('manuals.html', views.manuals, name='manuals'),
    path('spareparts.html', views.spareparts, name='spareparts'),
    path('aboutus.html', views.anomalies, name='anomalies'),
    path('dashboard.html', views.dashboard, name='dashboard'),




]