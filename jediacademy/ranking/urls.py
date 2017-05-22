from django.conf.urls import url

from .views import MentorList, RankRegisterCreate


urlpatterns = [
    url(r'^mentors/101/(?P<threshold>\d+)$',
        MentorList.as_view(), name='mentor-list'),
    url(r'^mentors/rankregister/create/$',
        RankRegisterCreate.as_view(), name='rankregister-create'),
    # url(r'', )
]