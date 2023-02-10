from django.urls import path
from .views import BillCreate,BillDetail

urlpatterns = [
    path('bill-create/', BillCreate.as_view(), name='bill-create'),
    path('bill-detail/<pk>/', BillDetail.as_view(), name='bill-detail'),    

    # path('vendor-list/', VendorList.as_view(), name='vendor-list'),
    # path('buyer-list/<pk>/', BuyerList.as_view(), name='buyer-list'),
    # path('bill-list/<pk>/', BillList.as_view(), name='bill-list'),
]
