from django.urls import path
from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('new-task', views.new_task, name='new_task'),
    path('edit-task', views.edit_task, name='edit_task'),
    path('show-task', views.show_task, name='show_task'),
    path('agenda', views.agenda, name='agenda'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)