from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})