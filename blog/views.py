from django.shortcuts import render,redirect,HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.utils import timezone
from .models import Post,comments
from .form import RegisterForm,LoginForm,PostForm
from django.contrib.auth import login,authenticate,logout

def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request,'blogg/homepage.html',{'posts':posts})

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

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home_page')

    return render(request, "blogg/login.html", {"form": form, 'title': 'Giriş Yap'})
def home(request):
    
    form=PostForm
    context={'form':form,}
    if request.method=="POST":
            form=PostForm(request.POST)
            
            if form.is_valid():
                form.save()
    else:
            
        form=PostForm
  

    return render(request,'blogg/home.html',context)
   


def post_delete(request, id):

    if not request.user.is_authenticated():
        return Http404()

    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("post:homepage")
    
    