from django.urls import path

from partner.views import PartnerList, PartnerDetail

urlpatterns = [
    path('/', PartnerList.as_view(), name=PartnerList.name),
    path('<int:pk>/', PartnerDetail.as_view(), name=PartnerDetail.name),
]