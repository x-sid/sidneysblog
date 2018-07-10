from django.urls import include,path
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'^accounts/login/$',views.login,name='login'),
    path(r'^accounts/logout/$',views.logout,name='logout', kwargs={'next_page': '/'}),
    path(r'',include('blog.urls')),
]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
