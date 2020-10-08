import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.home),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow)
    path('shows/<int: id>', views.readShow),
    path('shows/<int: id>/edit', views.editShow),
    path('shows/<int: id>/edit', views.updateShow),
    path('shows/<int: id>/edit', views.deleteShow)
]