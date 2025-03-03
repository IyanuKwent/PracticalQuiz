from django.urls import path
from .views import (
    PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, 
    CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView,
    VehicleListCreateAPIView, VehicleRetrieveUpdateDestroyAPIView,
    BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView,
    LoyaltyProgramRetrieveAPIView
)
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    
    path('posts/', PostListCreateAPIView.as_view(), name='list-create-post'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-post'),
    
    path('comments/', CommentListCreateAPIView.as_view(), name='list-create-comment'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-comment'),
    
    
    path('vehicles/', VehicleListCreateAPIView.as_view(), name='list-create-vehicle'),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-vehicle'),

    path('bookings/', BookingListCreateAPIView.as_view(), name='list-create-booking'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-booking'),

    path('reviews/', ReviewListCreateAPIView.as_view(), name='list-create-review'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-review'),

    path('loyalty/<int:pk>/', LoyaltyProgramRetrieveAPIView.as_view(), name='retrieve-loyalty-program'),
]
