from rest_framework import serializers
from billing_app.models import Bill
from django.contrib.auth.models import User

        

class BillSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.username', read_only=True)
    buyer_name = serializers.CharField(source='buyer.username', read_only=True)

    class Meta:
        model = Bill
        fields = ('buyer', 'buyer_name', 'vendor','vendor_name','date','product','quantity','rate','total')
        


# class UserSerializer(serializers.ModelSerializer):
#     bills = BillSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ('username', 'bills')


class UserSerializer(serializers.ModelSerializer):
    bill = BillSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bill']