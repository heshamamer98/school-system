from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm, SearchForm, EditForm
from .models import Student


@login_required
def home(request):
    # add student
    if request.method == 'POST' and 'StudentRegisterBtn' in request.POST:
        form = StudentRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    # student search by id
    elif request.method == 'POST' and 'SearchBtn' in request.POST:
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            studentId = searchform.cleaned_data.get('id')
            student = Student.objects.get(id=studentId)
            return render(request, 'blog/search.html', { 'student': student})
    else:
        form = StudentRegisterForm()
        searchform = SearchForm()
    return render(request, 'blog/home.html', { 'form': form, 'searchform': searchform })

@login_required
def delete(request, delete_id):
    student = Student.objects.get(id=delete_id).delete()
    return redirect('blog-home')

@login_required
def edit(request, edit_id):
    student = Student.objects.get(id=edit_id)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = EditForm(instance=student)
    return render(request, 'blog/edit.html', { 'form': form })


def students(request):
    students = Student.objects.all()
    
    if request.method == 'POST':
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            studentId = searchform.cleaned_data.get('id')
            student = Student.objects.get(id=studentId)
            return render(request, 'blog/search.html', { 'student': student})
    else:
        searchform = SearchForm()
    return render(request, 'blog/students.html', { 'students': students, 'searchform': searchform })



def search(request, search_id):
    student = Student.objects.get(id=search_id)
    return render(request, 'blog/search.html', { 'student': student})