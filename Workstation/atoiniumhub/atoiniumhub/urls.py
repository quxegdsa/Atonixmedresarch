from django.contrib import admin
from django.urls import path, include
from atoiniumapp.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atoiniumapp/', include('atoiniumapp.urls')),
    path('', home),  # Add this line to handle the root URL
]