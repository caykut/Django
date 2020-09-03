from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post,comments
from .form import RegisterForm,LoginForm
from django.contrib.auth import login,authenticate,logout

def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request,'blogg/homepage.html',{'posts':posts})
def home(request):
    commentss = comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request,'blogg/home.html',{'commentss':commentss})
   
def homee(request): 
    return render(request,'blogg/homee.html')
def register(request):
      if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homee')
      else:
        form = RegisterForm()
      return render(request, 'blogg/register.html', {'form': form}) 

def my_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home_page')

    return render(request, "blogg/login.html", {"form": form, 'title': 'Giriş Yap'})


        
    
    