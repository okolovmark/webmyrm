from django.conf.urls import url
from . import views

app_name = 'trash'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/detail_trash$', views.DetailTrashView.as_view(), name='detail_trash'),
    url(r'^(?P<trashsetting_id>[0-9]+)/file_list$', views.file_list, name='file_list'),
    url(r'^(?P<trashsetting_id>[0-9]+)/delete_files', views.delete_files, name='delete_files'),
]
