from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm

@login_required
def home(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary/home.html', {'entries': entries})

@login_required
def new_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('home')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/new_entry.html', {'form': form})

@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})

@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/edit_entry.html', {'form': form, 'entry': entry})

@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    return render(request, 'diary/delete_entry.html', {'entry': entry})
