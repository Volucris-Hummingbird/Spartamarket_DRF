from django.urls import path
from .views import CreateUserView, UserProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('api/accounts/', CreateUserView.as_view(), name='create_user'),
    path('api/accounts/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    path('api/accounts/<str:username>/follow/', FollowUserView.as_view(), name='follow_user'),
    path('api/accounts/<str:username>/unfollow/', UnfollowUserView.as_view(), name='unfollow_user'),
]