from django.urls import path
from . import views

app_name='review' ##app_name 일단 넣어주기 안넣어주면 오류!!

urlpatterns=[
    path('',views.review_list, name='review_list'),

    path('<int:pk>/',views.review_detail,name='detail'), #상세보기
    
    path('create/', views.review_create, name='create'), #생성하기

    path('<int:pk>/update', view=views.review_update, name='update'), #수정하기

    path('<int:pk>/delete', view=views.review_delete, name='delete') #삭제하기

]