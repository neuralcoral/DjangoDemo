from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views
from .views import StreamerLoginView
from django.urls import path
from .views import event_detail, schedule_list, create_event


urlpatterns = [
    path('', schedule_list, name='schedule_list'),
    path('events/<int:pk>', event_detail, name='event_detail'),
    path('create', create_event, name='create_event'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
