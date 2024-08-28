"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin , flatpages
from django.urls import path, include, re_path
from django.conf.urls import handler404, handler500
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse
# from django.contrib.sitemaps.views import sitemap
#
# from tastypie.api import Api
# from expense.api import ExpenseResource, UserResource
#
# v1_api = Api(api_name='v1')
# v1_api.register(UserResource())
# v1_api.register(ExpenseResource())
#


urlpatterns = [

    path('admin/', admin.site.urls),

    path((''), include('expense.urls')),
    #
    # path(('api/'), include('expense.urls')),
    #
    # re_path(r'^api/', include(v1_api.urls)),
    #
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # "SWAGGER_UI_FAVICON_HREF": settings.STATIC_URL + "static/favicon/favicon5.ico", # default is swagger favicon
