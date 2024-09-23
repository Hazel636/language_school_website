from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='schools'),
    path('<int:school_id>', views.school, name='school'),
]