from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', PostListCreateAPIView.as_view(), name='list-create-post'),
    path('the_finale/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-post'),
]