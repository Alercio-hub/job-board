"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao Job Board!")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/user/', include('users_app.urls')),
    path('api/contents/', include('contents.urls')),
    path('api/employers/', include('employers.urls')),
    path('api/jobs/', include('jobs.urls')),
]

if settings.DEBUG:

    from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="swagger-ui"),
    ]

    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
