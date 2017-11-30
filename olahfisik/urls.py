from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^categories', views.categories_view, name='categories'),
    url(r'^run', views.lari_view, name='lari'),
    url(r'^badminton', views.bad_view, name='bad'),
    url(r'^futsal', views.fut_view, name='fut'),
    url(r'^swim', views.ren_view, name='ren'),
    url(r'^gymnastic', views.sen_view, name='sen'),
    url(r'^pingpong', views.ping_view, name='ping'),
    url(r'^details/(?P<venue_id>\d+)/', views.details_view, name='details')
]
