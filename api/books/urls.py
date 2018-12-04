from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^books/(?P<book_id>\d+)/$', views.book_detail),
    url(r'^books/(?P<book_id>\d+)/chapters/$', views.book_chapters_list),
    url(r'^books/(?P<book_id>\d+)/chapters/(?P<chapter_id>\w+)/$', views.book_chapter_content),
]
