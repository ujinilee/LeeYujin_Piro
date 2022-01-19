from django.urls import path
from . import views


app_name='swidea'

urlpatterns=[
    path('',views.idea_list,name="idea_list"), #리스트 페이지

    path('plus_interest/', views.plus_interest, name="plus_interest"), ###AJAX
    path('minus_interest/', views.minus_interest, name="minus_interest"), ###AJAX


    path('<int:pk>/',views.idea_detail,name='idea_detail'), #디테일페이지

    path('new/', views.idea_new, name='idea_new'), #생성

    path('<int:pk>/edit/',views.idea_edit,name='idea_edit'), ##수정
    path('<int:pk>/delete', views.idea_delete, name='idea_delete'), #삭제하기



    path('dev/',views.dev_list, name="dev_list"), #리스트 페이지
    path('dev/<int:pk>/',views.dev_detail,name='dev_detail'), #디테일페이지

    path('dev/new/',views.dev_new,name='dev_new'), #생성


    path('dev/<int:pk>/edit/',views.dev_edit,name='dev_edit'), ##수정
    path('dev/<int:pk>/delete', views.dev_delete, name='dev_delete'), #삭제하기


]