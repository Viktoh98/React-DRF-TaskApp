from django.urls import path
from .. views import TaskListCreateView, TaskDetailUpdateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', TaskListCreateView.as_view(), name='list-create'),
    path('<slug:slug>/', TaskDetailUpdateView.as_view(), name='detail'),
]
