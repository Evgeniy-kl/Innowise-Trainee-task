from django.urls import path, include

urlpatterns = [
    path(r'', include('user.urls')),
    path(r'', include('innotter.urls')),
]
