from django.urls import path
from . import views
urlpatterns = [
    path('all/',views.get_subjects,name='getting_subjects'),
    path('create/',views.create_subject,name='subject_create'),
    path('<int:pk>',views.get_subject,name='subject_get'),
]