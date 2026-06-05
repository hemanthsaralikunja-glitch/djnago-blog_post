"""
URL configuration for blog_main project.
"""
from django.contrib import admin
from django.urls import path
from myapp.views import about, blog_detail, category_posts, contact, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
