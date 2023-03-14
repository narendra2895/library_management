from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= 'index'),
    path("insert_record", views.insert_record, name= 'insert_record'),
    path("edit/<rid>", views.edit, name= 'edit'),
    path("delete/<rid>", views.delete, name= 'delete'),
 

]