from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Booking, Menu
from .serializers import UserSerializer,BookingSerializer, MenuSerializer

# Create your views here.
# function based views
def index(request):
    return render(request, 'index.html', {})

# class based views

# class UserRetrieveItem(mixins.RetrieveModelMixin, GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def get(self, request):
#         return self.list(request)

class UserViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return[permission() for permission in permission_classes]

    queryset = User.objects.all()

    def list(self, request):
        serializer = UserSerializer(self.queryset)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

# class bookingview(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many = True)
#         return Response(serializer.data) #JSON

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]