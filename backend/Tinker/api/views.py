from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import InventoryItemSerializer
from base.models import InventoryItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from base.forms import UserRegisterForm
from django.shortcuts import get_object_or_404

class DashboardAPI(APIView):
    def get(self, request):
        items = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)

class SignUpAPI(APIView):
    def post(self, request):
        form = UserRegisterForm(request.data)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class AddItemAPI(APIView):
    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditItemAPI(APIView):
    def put(self, request, pk):
        item = get_object_or_404(InventoryItem, pk=pk)
        serializer = InventoryItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteItemAPI(APIView):
    def delete(self, request, pk):
        item = get_object_or_404(InventoryItem, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
