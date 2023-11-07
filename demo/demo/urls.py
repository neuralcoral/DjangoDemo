from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('schedule/', include('streamscheduler.urls')),
    path('', RedirectView.as_view(url='/schedule/', permanent=True))
]
