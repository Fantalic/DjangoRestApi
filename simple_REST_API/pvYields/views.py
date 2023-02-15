from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PvYield
from .serializers import PvYieldSerializer

def example_function():
    return {'result': 'Hello from Example Function'}

class PvYieldsViewSet(viewsets.ViewSet):

    def list(self, request):
        result = example_function()
        return Response(result)
    
    def retrieve(self, request, pk=None):
        queryset = PvYield.objects.all()
        state = request.query_params.get('state')
        plz = request.query_params.get('plz')
        capacity = request.query_params.get('capacity')
        
        if state:
            queryset = queryset.filter(state=state)
        elif plz:
            queryset = queryset.filter(plz=plz)
        else:
            return Response({'error': 'Please provide either state or plz parameter'}, status=status.HTTP_400_BAD_REQUEST)
        
        if capacity is not None:
            try:
                capacity = float(capacity)
            except ValueError:
                return Response({'error': 'Invalid capacity value'}, status=status.HTTP_400_BAD_REQUEST)

        if queryset.exists():
            serializer = PvYieldSerializer(queryset.first())
            yield_value = serializer.data['yield_value']
            
            if capacity is not None:
                yield_value = yield_value * capacity
                
            return Response({ "yield": yield_value, "state":state})
        else:
            return Response({'error': 'No matching dataset found'}, status=status.HTTP_404_NOT_FOUND)

        