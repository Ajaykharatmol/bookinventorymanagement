from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Book_Inventory_APP.urls')),
    path('Book_Inventory_API/', include('Book_Inventory_API.urls')),
    path('admin/', admin.site.urls),
   


]
