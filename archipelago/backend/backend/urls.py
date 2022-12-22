"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path

from Archipelago_backend import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/login/", views.login),
    path("api/register/", views.register),
    path("api/logoff/", views.logoff),
    path("api/delete_account/", views.delete_account),
    path("api/get_user_info/", views.get_user_info),
    path("api/set_user_info/", views.set_user_info),
    path("api/get_album/", views.get_album),
    path("api/get_album_info/", views.get_album_info),
    path("api/set_album/", views.set_album),
    path("api/del_album/", views.del_album),
    path("api/get_musician/", views.get_musician),
    path("api/get_all_musician/", views.get_all_musician),
    path("api/set_musician/", views.set_musician),
    path("api/add_musician_member/", views.add_musician_member),
    path("api/set_musician_member/", views.set_musician_member),
    path("api/get_musician_member/", views.get_musician_member),
    path("api/del_musician_member/", views.del_musician_member),
    path("api/get_musician_tag/", views.get_musician_tag),
    path("api/set_musician_tag/", views.add_del_musician_tag),
    path("api/add_song/", views.add_song),
    path("api/set_song/", views.set_song),
    path("api/del_song/", views.del_song),
    path("api/get_album_tag/", views.get_album_tag),
    path("api/add_del_album_tag/", views.add_del_album_tag),

    path("api/get_homepage_info/", views.get_homepage_info),
    path("api/search_musician_album/", views.search_musician_album),
    path("api/search_tag/", views.search_tag),
    path("api/get_order/", views.get_order),
    path("api/gen_order/", views.gen_order),
    path("api/upload_img/", views.upload_img)
]
