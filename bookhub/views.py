from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book, Transaction, CustomUser
from .serializers import BookSerializer, TransactionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def view_books(request):
    return render(request, 'books.html')

def checkout(request):
    return render(request, 'checkout.html')

def return_book(request):
    return render(request, 'return.html')

def register_user(request):
    return render(request, 'register.html')
