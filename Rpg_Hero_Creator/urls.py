"""Rpg_Hero_Creator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from warhammer.views import HeroCreationView, HeroView, UserLoginView, AddUserView, UserLogoutView, HeroesSearchAndView, \
    MainSiteView, HeroDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainSiteView.as_view(), name="index"),
    url(r'^warhammer/hero_creation/', HeroCreationView.as_view(), name='warhammer-hero-creation'),
    url(r'^warhammer/hero/(?P<hero_id>(\d+))$', HeroView.as_view(), name="warhammer-hero-view"),
    url(r'^warhammer/heroes/', HeroesSearchAndView.as_view(), name='warhammer-heroes'),
    url(r'^warhammer/hero/delete/(?P<hero_id>(\d+))$', HeroDeleteView.as_view(), name='warhammer-hero-delete'),

    url(r'^user_login/', UserLoginView.as_view(), name='user-login'),
    url(r'^user_logout/', UserLogoutView.as_view(), name='user-logout'),
    url(r'^add_user/', AddUserView.as_view(), name='add-user'),
]
