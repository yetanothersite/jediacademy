from django.conf.urls import url

from .views import MainPageView, PersonCreateView, PersonDetailView


urlpatterns = [
    url(r'^$',
        MainPageView.as_view(), name='mainpage'),
    url(r'^person/create/$',
        PersonCreateView.as_view(), name='person-create'),
    url(r'^person/(?P<pk>\d+)/detail/$',
        PersonDetailView.as_view(), name='person-detail'),
]
