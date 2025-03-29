from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('new/', views.new_entry, name='new_entry'),  # Add a new entry  
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Edit an entry
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),  # Delete an entry
]
