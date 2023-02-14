

from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response

def example_function():
    return {'result': 'Hello from Example Function'}

class PvYieldsView(views.APIView):

    def get(self, request, format=None):
        # Call the example function here
        result = example_function()
        return Response(result)

        