from django.urls import path

from .views import BoardList, BoardDetail

urlpatterns = [
    path('/', BoardList.as_view(), name=BoardList.name),
    path('<int:pk>/', BoardDetail.as_view(), name=BoardDetail.name),
]