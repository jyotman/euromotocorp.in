from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'nameform/', views.get_name),
    url(r'repair/tyre', views.repairTyre, name='repairTyre'),
    url(r'repair/rim', views.repairAlloy, name='repairAlloy'),
]