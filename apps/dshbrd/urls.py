from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from apps.dshbrd import views

urlpatterns = [
    url(r'^travels/$', login_required(views.Dashboard.as_view(),login_url='/accounts/login'),name='travel-dashboard'),
    url(r'^travels/destination/(?P<id>\d+)$',views.Trip.as_view(),name='destination-detail'),
    url(r'^add/',views.Trip.as_view(),name='destination-create'),
]
