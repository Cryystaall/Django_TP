# event_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),  # Assure-toi que cette ligne existe et que le nom de ton app est correct
]
