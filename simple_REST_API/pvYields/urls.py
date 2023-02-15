from django.urls import path, include

urlpatterns = [
    path(r'', include('simple_REST_API.urls')),
]