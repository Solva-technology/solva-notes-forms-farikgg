from django.shortcuts import get_object_or_404, redirect, render 

from .models import Note, User
from .forms import NoteForm
from .service import get_note_detail, get_notes_list, get_user_detail


def all_notes_view(request):
    note_list = get_notes_list()

    return render(
        request=request,
        template_name='notes/notes_info/all_notes.html',
        context={'note_list': note_list}
    )    

def note_detail_view(request, note_id: int):
    note_detail = get_note_detail(note_id)
    
    return render(
        request=request,
        template_name='notes/notes_info/detail.html',
        context={'note_detail': note_detail}
    )

def user_detail_view(request, user_id: int):
    user_detail = get_user_detail(user_id)

    return render(
        request=request,
        template_name='notes/user_info/user_profile.html',
        context={'user_detail': user_detail}
    )

def search(request):
    if request.method == 'GET':
        note_id = request.GET.get('note_id')
        user_id = request.GET.get('user_id')

        if note_id:
            return redirect('notes:note_detail', note_id=note_id)
        elif user_id:
            return redirect('notes:user_profile', user_id=user_id)

    return render(request, 'notes/search.html')
 
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.author = request.user
            else:
                note.author = User.objects.get_or_create(name="Anonymous")[0]
            note.save()
            form.save_m2m()
            return redirect('notes:all_notes')
    else:
        form = NoteForm()

    return render(request, 'notes/notes_form/create_note.html', {'form': form})

def edit_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_detail', note_id=note_id)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/notes_form/edit_note.html', {'form': form, 'note': note})

def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:all_notes')

    return render(request, 'notes/notes_form/delete_note.html', {'note': note})
