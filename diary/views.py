from django.shortcuts import render, redirect
from .models import DiaryEntry
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')  
    context = {'entries': entries} 
    return render(request, 'html/diary/home.html', context) 

@login_required
def new_entry(request):
    return render(request, 'html/diary/new_entry.html')
        # if request.method == 'POST':
        #     form = DiaryEntry(request.POST)
        #     if form.is_valid():
        #         entry = form.save(commit=False)
        #         entry.user = request.user  
        #         entry.save()
        #         return redirect('home')  
        # else:
        #     form = DiaryEntry()
        # return render(request, 'new_entry.html', {'form': form})


@login_required
def edit_entry(request, entry_id):
    return render(request, 'html/diary/edit_entry.html', {'entry_id': entry_id})

@login_required
def delete_entry(request, entry_id):
    return render(request, 'html/diary/delete_entry.html', {'entry_id': entry_id})
