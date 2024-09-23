from django.urls import path

from . import views

urlpatterns = [
    path('<int:headline_id>', views.headline, name='headline'),
]