from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('billing_app.api.urls')),
    path('accounts/', include('accounts.api.urls'))
]
