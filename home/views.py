# views.py
from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def page1(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page2')
    else:
        form = PersonForm()

    return render(request, 'page1.html', {'form': form})

def page2(request):
    people = Person.objects.all()  # Get all people from the database
    return render(request, 'page2.html', {'people': people})
