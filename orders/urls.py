from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/', views.create, name='create'),
    url('update/', views.update, name='update'),
    url('remove/', views.remove, name='remove'),
    url('list/', views.list_all, name='list')
]
