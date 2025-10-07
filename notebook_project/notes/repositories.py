from django.db.models import Prefetch
from django.shortcuts import get_object_or_404

from .models import Note, User


def get_all_notes():
    return (
        Note.objects
        .select_related('author')
        .prefetch_related('category')
        .all()
    )

def get_note_by_id(note_id: int):
    return get_object_or_404(
        Note.objects
        .select_related('author', 'author__profile', 'status')
        .prefetch_related('category'),
        pk=note_id
    )

def get_user_by_id(user_id: int):
    return get_object_or_404(
        User.objects
        .select_related('profile')
        .prefetch_related(
            Prefetch(
                'notes',
                queryset=Note.objects.select_related('status')
            )
        ),
        pk=user_id
    )
