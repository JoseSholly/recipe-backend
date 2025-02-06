from django.urls import path
# from .views import CreateUserView, LoginView, LogoutView
from .views import LogoutView, SignUpView, LoginView
from rest_framework_simplejwt.views import  TokenRefreshView


urlpatterns = [
    # Django Auth system
    # path('user/signup/', CreateUserView.as_view(), name='signup'),
    # path('user/login/', LoginView.as_view(), name='login'),
    # path('user/logout/', LogoutView.as_view(), name='logout'),
    path("user/login/", LoginView.as_view(), name="login"),
    path("user/logout/", LogoutView.as_view(), name="logout"),
    path("user/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/signup/", SignUpView.as_view(), name="signup"),
]

