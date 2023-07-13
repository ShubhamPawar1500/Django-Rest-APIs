from django.urls import path
from .views import BookListAPIView, BookDetailView, CreateAPIView, BookUpdateView, BookDelete

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('book_details/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('create-book/', CreateAPIView.as_view(), name='create-book'),
    path('update-book/<int:pk>/', BookUpdateView.as_view(), name='update-book'),
    path('delete-book/<int:id>/', BookDelete.as_view(), name='delete-book'),
]