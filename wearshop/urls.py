from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls', namespace='order')),
    path('wear/', include('wear.urls', namespace='wear')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include('homepage.urls', namespace='homepage')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)