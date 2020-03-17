from django.urls import path
from . import views
# urlpatterns = [

#     path('', views.booklist.as_view(), name='book_list'),
#     path('view/<int:pk>', views.bookview.as_view(), name='book_view'),
#     path('new', views.bookcreate.as_view(), name='book_new'),
#     path('view/<int:pk>', views.bookview.as_view(), name='book_view'),
#     path('edit/<int:pk>', views.bookupdate. as_view(), name='book_edit'),
#     path('delete/<int:pk>', views.bookdelete. as_view(), name='book_delete'),
# ]


# url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),


# URLS USING THE REGULAR EXPRESSIONS FOR FUNCTION BASED VIEWS.

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', booklist, name='booklist'),
    url(r'^view/(?P<pk>\d+)$', bookview, name='bookview'),
    url(r'^new$', bookcreate, name='bookcreate'),
    url(r'^update/(?P<pk>\d+)$', bookupdate, name='bookupdate'),
    url(r'^delete/(?P<pk>\d+)$', bookdelete, name='bookdelete'),

]
