from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.all_notes_view, name='all_notes'),
    path('notes/<int:note_id>/', views.note_detail_view, name='note_detail'),
    path('users/<int:user_id>/', views.user_detail_view, name='user_profile'),
    path('notes/create/', views.create_note, name='create_note'),
    path('notes/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('notes/<int:note_id>/delete/', views.delete_note, name='delete_note')
]
