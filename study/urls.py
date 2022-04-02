"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path,include
from . import views


urlpatterns = [
    path("music/",include('music.urls')),
    path("news/",include("news.urls")),
    path("sport/",include("sport.urls")),
    path('admin/', admin.site.urls),
    path("html/page/1",views.page1_view),
    path("html/page/2",views.page2_view),
    path("html/page/3",views.page3_view),
    path("html",views.html_view),
    path("html/page/<int:n>",views.pagen_view),
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$',views.pagep_view),
    path("html/page/<int:m>/<str:t>/<int:n>",views.pagem_view),
    path("test_request",views.test_request),
    path("test_get_post",views.test_get_post),
    path("test_html", views.test_html),
    path("test_request_html",views.test_request_html),
    path("test_param_html",views.test_param_html),
    path("test_if_for",views.test_if_for),
    path("test_calculator_html",views.test_calculator_html),

    path("base_index",views.base_view),
    path("music_index",views.music_view),
    path("sport_index",views.sport_view),

    path("test/url",views.test_url),
    path("test_url_result/<int:age>",views.test_url_result,name="tr"),

    path("test_static",views.test_static),

    path("bookstore/",include("bookstore.urls"))
]
