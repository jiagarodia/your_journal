from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page to show all diary entries
    path('new/', views.new_entry, name='new_entry'),  # Page to create a new diary entry
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),  # Detail view for a diary entry
    path('entry/<int:pk>/edit/', views.edit_entry, name='edit_entry'),  # Edit an entry
    path('entry/<int:pk>/delete/', views.delete_entry, name='delete_entry'),  # Delete an entry
]
