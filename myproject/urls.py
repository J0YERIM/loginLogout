from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
import myapp.views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home,name="home"), 
    path('accounts/', include('accounts.urls')),
]
