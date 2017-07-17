"""Community Guide URL Configuration
The `urlpatterns` list routes URLs to views. 
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

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


# update urls to have paginators
urlpatterns = [
	url(r'^$', views.index),
	url(r'^explore/$', views.explore),
	
	url(r'^departments/$', views.departments),
	url(r'^utilities/$', views.utilandservice),
	url(r'^important/$', views.important),
	url(r'^education/$', views.education),
	url(r'^restaurant/$', views.restaurant),
	url(r'^LCRV/$', views.lodgecamprv),
	url(r'^localattractions/$', views.attractions),
	# Page Numbers
	url(r'^departments/(?P<page>[\w]+)/', views.departments),
	url(r'^utilities/(?P<page>[\w]+)/', views.utilandservice),
	url(r'^important/(?P<page>[\w]+)/', views.important),
	url(r'^education/(?P<page>[\w]+)/', views.education),
	url(r'^restaurant/(?P<page>[\w]+)/', views.restaurant),
	url(r'^LCRV/(?P<page>[\w]+)/', views.lodgecamprv),
	url(r'^localattractions/(?P<page>[\w]+)/', views.attractions),
	# Membership currently not supported
	#url(r'^membership/(?P<page>[\w]+)/', views.membership),
]
