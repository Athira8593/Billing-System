from rest_framework import generics
from billing_app.models import Bill
from django.contrib.auth.models import User
from .serializers import  BillSerializer, UserSerializer
from .permissions import IsStaffUser,IsBuyer
from rest_framework.permissions import IsAuthenticated


class BillCreate(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsStaffUser]
    

class BillDetail(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsBuyer]
    
    




# class VendorList(generics.ListAPIView):
#     queryset = User.objects.filter(is_staff=True)
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
    

# class BuyerList(generics.RetrieveAPIView):
#     queryset = User.objects.filter(is_staff=False)
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]


# class BillList(generics.RetrieveAPIView):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer
#     permission_classes = [IsAuthenticated]
   