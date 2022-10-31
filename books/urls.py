from django.urls import path

from books.views import BookModelListAPIView, BookDetailAPIView

urlpatterns = [
    path('book/', BookModelListAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
