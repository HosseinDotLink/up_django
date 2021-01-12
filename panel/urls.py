from django.contrib.auth import views as auth_views
from django.urls import path, include
from panel import views

urlpatterns = [
    path('',views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='panel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='panel/logout.html'), name='logout'),
    path('message/', views.msgList, name='message'),
    path('message/<userID>/', views.msgs, name='chatroom'),
    path('project/', views.projectsList, name='project'),
    path('project/add/', views.addProject, name='addproject'),
    path('project/accept/<prjID>/', views.acceptProject, name='acceptproject'),
    path('project/decline/<prjID>/', views.declineProject, name='declineproject'),
    path('project/remove/<prjID>/', views.deleteProject, name='deleteproject'),
    path('project/edit/<prjID>/', views.editProject, name='editproject'),
    path('project/select/<prjID>/', views.selectProject, name='selectproject'),
]