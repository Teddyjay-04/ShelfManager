from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import BookViewSet, UserViewSet, TransactionViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.home, name='home'),
    path('books/', views.view_books, name='books'),
    path('checkout/', views.checkout, name='checkout'),
    path('return/', views.return_book, name='return_book'),
    path('register/', views.register_user, name='register'),
]
