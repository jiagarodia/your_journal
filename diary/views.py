# 


from django.shortcuts import render
from .models import DiaryEntry

def home(request):
    context = {
        'diaryentry': DiaryEntry.objects.all()
    }
    return render(request, 'html/diary/home.html', context)

def new_entry(request):
    return render(request, 'html/diary/new_entry.html')

def edit_entry(request, entry_id):
    return render(request, 'html/diary/edit_entry.html', {'entry_id': entry_id})

def delete_entry(request, entry_id):
    return render(request, 'html/diary/delete_entry.html', {'entry_id': entry_id})
