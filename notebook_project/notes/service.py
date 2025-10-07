from django.utils.dateformat import DateFormat

from .repositories import get_all_notes, get_note_by_id, get_user_by_id


MAX_SYMBOLS = 100
DATE_FORMAT = 'Y-m-d H:i'
BIRTH_DATE_FORMAT = 'd-m-Y'
INFO_BIO = 'Не указано'
END_OF_LONG_TEXT = '...'

def converting_datetime(dt, fmt):
    return DateFormat(dt).format(fmt)

def get_notes_list():
    notes = get_all_notes()
    data = []
    for note in notes:
        data.append({
            'text_preview': note.text[:MAX_SYMBOLS] + END_OF_LONG_TEXT,
            'author': note.author.name,
            'status': note.status,
            'category': list(note.category.values_list('title', flat=True)),
            'created_at': converting_datetime(note.created_at, DATE_FORMAT),
        })
    return data

def get_note_detail(note_id: int):
    noteData = get_note_by_id(note_id)
    profileData = getattr(noteData.author, 'profile', None)

    return {
        'id': noteData.pk,
        'text': noteData.text,
        'author': {
            'name': noteData.author.name,
            'email': noteData.author.email,
            'bio': profileData.bio if profileData else None,
            'birth_date': converting_datetime(profileData.birth_date, BIRTH_DATE_FORMAT)
                if (profileData and profileData.birth_date) else None,
        },
        'status': {
            'name': noteData.status.name if noteData.status else None,
            'is_final': noteData.status.is_final if noteData.status else False,
        },
        'category': list(noteData.category.values_list('title', flat=True)),
        'created_at': converting_datetime(noteData.created_at, DATE_FORMAT),
    }

def get_user_detail(user_id: int):
    userData = get_user_by_id(user_id)
    userProfile = getattr(userData, 'profile')
    userNote = getattr(userData, 'notes')

    return {
        'name': userData.name,
        'email': userData.email,
        'bio': userProfile.bio if hasattr(userData, 'profile') else INFO_BIO,
        'birth_date': userProfile.birth_date,
        'notes': [
            {
                'text': note.text[:MAX_SYMBOLS],
                'status': note.status.name if note.status else None            
            } 
                for note in userNote.all()
        ]
    }
