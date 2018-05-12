from django.urls import path

from event.views import EventList, EventDetail

urlpatterns = [
    path('/', EventList.as_view(), name=EventList.name),
    path('<int:pk>/', EventDetail.as_view(), name=EventDetail.name),
]