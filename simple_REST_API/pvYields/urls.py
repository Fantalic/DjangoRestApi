from django.urls import path
from .views import PvYieldsView

urlpatterns = [
    path('example/', PvYieldsView.as_view(), name='example'),
]