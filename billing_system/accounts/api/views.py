from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from accounts.api.serializers import RegistrationSerializer
from accounts import models
from django.urls import resolve

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        current_url = resolve(request.path_info).url_name
        print(current_url)            
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            if current_url == 'vendor-register':
                account.is_staff = True
                account.save()
            else:
                pass
            data['response'] = "Registration Successfull"
            data['username'] = account.username
            data['email'] = account.email
            data['is_staff'] = True
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
            
        return Response(data)
    
    
