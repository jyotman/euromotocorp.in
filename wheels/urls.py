from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'contact/', views.get_name, name='contact'),
    url(r'repair/tyre', views.repairTyre, name='repairTyre'),
    url(r'repair/rim', views.repairAlloy, name='repairAlloy'),
]