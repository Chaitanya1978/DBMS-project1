from django.contrib import admin
from django.urls import path

from application_code.views import member_dashboard, create_new_member_view, update_member_profile,member_profile

from application_code.views import delete_member_profile,add_task,edit_task,delete_task,show_tasks

from application_code.views import add_category,edit_category,delete_category,show_categories

from application_code.views import add_task_category,edit_task_category,delete_task_category,show_task_categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',member_dashboard,name='member_home_page'),
    path('create/member/', create_new_member_view, name='create_member'),
    path('member/dashboard/', member_dashboard, name='member_dashboard'),
    path('profile/', member_profile, name='profile'),
    path('update/member/profile/', update_member_profile, name='update_profile'),
    path('delete/member/profile/',delete_member_profile,name='delete_profile'),

    path('add/task/',add_task,name='add_task'),
    path('edit/task/<int:task_id>/',edit_task,name='edit_task'),
    path('delete/task/<int:task_id>/',delete_task,name='update_task'),
    path('tasks/',show_tasks,name='show_tasks'),

    path('add/category/',add_category,name='add_task'),
    path('edit/category/<int:category_id>/',edit_category,name='edit_task'),
    path('delete/category/<int:category_id>/',delete_category,name='update_task'),
    path('categories/',show_categories,name='show_categories'),

    path('add/task/category/',add_task_category,name='add_task_category'),
    path('edit/task/category/<int:task_category_id>/',edit_task_category,name='edit_task_category'),
    path('delete/task/category/<int:task_category_id>/',delete_task_category,name='delete_task_category'),
    path('show/task/categories/',show_task_categories,name='show_task_categories'),
    path('logout/',create_new_member_view,name='logout'),




]
