from django.urls import path
from . import views

app_name='pirostagram'

urlpatterns = [
    path('', views.ajax_list),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path("write_comment/", views.write_comment, name='write_comment'),
    path("del_comment/", views.del_comment, name='del_comment'),

    #path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    #path('<int:pk>/comment/', views.ajax_list, name='ajax_list'),

]
