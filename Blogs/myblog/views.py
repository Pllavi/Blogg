# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render
# from myblog.models import Post, Category
#
#
# # Create your views here.
# def home(request):
#
#     posts = Post.objects.all()[:11]
#     # # print(posts)
#     #
#     cats = Category.objects.all()
#
#     data = {
#         'posts': posts,
#         'cats': cats
#     }
#     return render(request, 'home.html', data)
#
#
# def post(request, url):
#     post = Post.objects.get(url=url)
#     cats = Category.objects.all()
#
#     # print(post)
#     return render(request, 'posts.html', {'post': post, 'cats': cats})
#
#
# def category(request, url):
#     cat = Category.objects.get(url=url)
#     posts = Post.objects.filter(cat=cat)
#     return render(request, "category.html", {'cat': cat, 'posts': posts})
from django.http import HttpResponse
from django.shortcuts import render
from myblog.models import Post, Category


from django.contrib.auth.views import LogoutView, LoginView
# Create your views here.
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login page upon logout

def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'dashboard.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render

def subscription_page(request):
    return render(request, 'subscription.html')

@login_required(login_url='login')
def dashboard(request):
    user = request.user  # Access authenticated user
    return render(request, 'dashboard.html', {'user': user})

def blog(request):
    # Optionally, you can fetch blog posts from a database here
    # posts = BlogPost.objects.all()  # Assuming you have a model named BlogPost
    # Then pass the posts to the template context

    return render(request, 'blog.html')


def edit(request):
    # Add any necessary logic here

    return render(request, 'edit.html')

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostEditForm
from .models import Post

# views.py

from django.shortcuts import render, redirect
from .models import Category, Post
from .forms import CategoryEditForm, PostEditForm


def edit(request, category_id, post_id):
    category = Category.objects.get(pk=category_id)
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        category_form = CategoryEditForm(request.POST, instance=category)
        post_form = PostEditForm(request.POST, instance=post)
        if category_form.is_valid() and post_form.is_valid():
            category_form.save()
            post_form.save()
            return redirect('home')  # Redirect to home page after saving changes
    else:
        category_form = CategoryEditForm(instance=category)
        post_form = PostEditForm(instance=post)

    return render(request, 'edit.html', {'category_form': category_form, 'post_form': post_form})


from django.shortcuts import render, redirect
from .models import Post


def create_blog_post(request):
    if request.method == 'POST':
        form = PostEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of your home page URL pattern
    else:
        form = PostEditForm()
    return render(request, 'create_blog_post.html', {'form': form})
