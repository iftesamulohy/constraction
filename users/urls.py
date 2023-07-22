from django.urls import path
from users import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'user',views.Userme,basename="user")
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.RegisterUser.as_view()),
    path('employee/',views.EmployeeView.as_view())
]
