from django.urls import path
from . import views
urlpatterns = [
    path('', views.booklist.as_view(), name='book_list'),
    path('view/<int:pk>', views.bookview.as_view(), name='book_view'),
    path('new', views.bookcreate.as_view(), name='book_new'),
    path('view/<int:pk>', views.bookview.as_view(), name='book_view'),
    path('edit/<int:pk>', views.bookupdate. as_view(), name='book_edit'),
    path('delete/<int:pk>', views.bookdelete. as_view(), name='book_delete'),
]


# url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),
