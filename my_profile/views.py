from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def home(request):
    profile = Profile.objects.all()

    return render(request, 'home.html', {'profile': profile})

def upload(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.save()

        return redirect('home')

    else:
        form = ProfileForm()
        
    return render(request, 'upload.html', {'form': form})

def more(request):

    return render(request, 'more.html')