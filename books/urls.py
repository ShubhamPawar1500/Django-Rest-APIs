from django.urls import path
from .views import BookListView
from rest_framework.authtoken import views

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('api-auth-token/', views.obtain_auth_token)
]