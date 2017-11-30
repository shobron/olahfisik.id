from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^categories', views.categories_view, name='categories'),
    url(r'^results', views.results_view, name='results'),
    url(r'^details/(?P<venue_id>\d+)/', views.details_view, name='details')
]
