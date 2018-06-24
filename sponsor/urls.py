from django.urls import path

from sponsor.views import SpnosorList, SpnosorDetail

urlpatterns = [
    path('', SpnosorList.as_view(), name=SpnosorList.name),
    path('<int:pk>/', SpnosorDetail.as_view(), name=SpnosorDetail.name),
]
