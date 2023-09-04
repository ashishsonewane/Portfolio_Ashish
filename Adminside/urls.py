from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name='login'),
    path('index',views.index,name='index'),
    path('settings',views.settings,name='settings'),
    path('logout',views.adminlogout,name='logout'),
   
    path('gallary_table',views.gallary_table,name='gallary_table'),
    path('add_gallary',views.add_gallary,name='add_gallary'),
    path('delete_gallary/<int:id>',views.delete_gallary,name='delete_gallary'),
    path('gallary_update/<int:id>',views.gallary_update,name='gallary_update'),

    path('about_table',views.about_table,name='about_table'),
    path('add_about',views.add_about,name='add_about'),
    path('delete_about/<int:id>',views.delete_about,name='delete_about'),
    path('update_about/<int:id>',views.update_about,name='update_about'),

    path('projects_table',views.projects_table,name='projects_table'),
    path('projects_add',views.projects_add,name='projects_add'),
    path('project_delete/<int:id>',views.project_delete,name='project_delete'),
    path('project_edit/<int:id>',views.project_edit,name='project_edit'),


    path('contact_table',views.contact_table,name='contact_table'),
    path('contact_add',views.contact_add,name='contact_add'),
    path('contact_delete/<int:id>',views.contact_delete,name='contact_delete'),
    path('contact_edit/<int:id>',views.contact_edit,name='contact_edit'),

    path('skill_table',views.skill_table,name='skill_table'),
    path('add_skill',views.add_skill,name='add_skill'),
    path('skill_delete/<int:id>',views.skill_delete,name='skill_delete'),
    path('skill_update/<int:id>',views.skill_update,name='skill_update'),
   

]