from django.urls import path
# from .views import CreateUserView, LoginView, LogoutView
from .views import LogoutView, SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    # Django Auth system
    # path('user/signup/', CreateUserView.as_view(), name='signup'),
    # path('user/login/', LoginView.as_view(), name='login'),
    # path('user/logout/', LogoutView.as_view(), name='logout'),

    path('user/login/', SignUpView.as_view(), name='login'),
    path('user/logout/', LogoutView.as_view(), name='logout'),
    path('user/signup/', SignUpView.as_view(), name= 'signup')
]

