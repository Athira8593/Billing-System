from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from accounts.api.views import registration_view, logout_view


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('vendor-register/', registration_view, name='vendor-register'),
    path('buyer-register/', registration_view, name='buyer-register'),
    path('logout/', logout_view, name='logout'),
]
