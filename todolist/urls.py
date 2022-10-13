from django.urls import path
from todolist.views import delete_task, register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import progres
from todolist.views import delete_task
from todolist.views import todolist_ajax
from todolist.views import get_todolist_json
from todolist.views import add


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name ='create-task'),
    path('progres/<int:pk>/', progres, name='progres'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
    path('json/', todolist_ajax, name='show_json'),
    path('get_todolist_json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add, name='add'),
]