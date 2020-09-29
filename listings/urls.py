from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    # path requires an id
    path('<int:listings_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
