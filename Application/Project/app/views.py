from django.contrib import messages 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Barangay, Service, UserProfile, Request
from .forms import PostForm, BarangayForm, ServiceForm, UserProfileForm, RequestForm

# Home view
def home(request):
    return render(request, 'app/home.html')

# About view
def about(request):
    return render(request, 'app/about.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')  
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials') 
    return render(request, 'app/login.html')

@login_required
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)  # Fetch user profile first
    posts = Post.objects.filter(author=request.user)
    barangays = Barangay.objects.filter(userprofile=user_profile)  # Use userprofile
    services = Service.objects.filter(userprofile=user_profile)  # Use userprofile
    requests = Request.objects.filter(userprofile=user_profile)  # Use userprofile
    
    return render(request, 'app/user_profile.html', {
        'posts': posts,
        'barangays': barangays,
        'services': services,
        'requests': requests
    })

# CRUD for Post
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})

# (Other CRUD functions remain unchanged)
# ... (rest of the existing view functions)
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')
    else:
        form = PostForm()
    return render(request, 'app/post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post-list')
    return render(request, 'app/post_confirm_delete.html', {'post': post})

# CRUD for Barangay
def barangay_list(request):
    barangays = Barangay.objects.all()
    return render(request, 'app/barangay_list.html', {'barangays': barangays})

def barangay_detail(request, pk):
    barangay = get_object_or_404(Barangay, pk=pk)
    return render(request, 'app/barangay_detail.html', {'barangay': barangay})

def barangay_create(request):
    if request.method == "POST":
        form = BarangayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barangay-list')
    else:
        form = BarangayForm()
    return render(request, 'app/barangay_form.html', {'form': form})

def barangay_update(request, pk):
    barangay = get_object_or_404(Barangay, pk=pk)
    if request.method == "POST":
        form = BarangayForm(request.POST, instance=barangay)
        if form.is_valid():
            form.save()
            return redirect('barangay-detail', pk=barangay.pk)
    else:
        form = BarangayForm(instance=barangay)
    return render(request, 'app/barangay_form.html', {'form': form})

def barangay_delete(request, pk):
    barangay = get_object_or_404(Barangay, pk=pk)
    if request.method == "POST":
        barangay.delete()
        return redirect('barangay-list')
    return render(request, 'app/barangay_confirm_delete.html', {'barangay': barangay})

# CRUD for Service
def service_list(request):
    services = Service.objects.all()
    return render(request, 'app/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'app/service_detail.html', {'service': service})

def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service-list')
    else:
        form = ServiceForm()
    return render(request, 'app/service_form.html', {'form': form})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service-detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'app/service_form.html', {'form': form})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.delete()
        return redirect('service-list')
    return render(request, 'app/service_confirm_delete.html', {'service': service})

# CRUD for UserProfile
def userprofile_list(request):
    userprofiles = UserProfile.objects.all()
    return render(request, 'app/userprofile_list.html', {'userprofiles': userprofiles})

def userprofile_detail(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'app/userprofile_detail.html', {'userprofile': userprofile})

def userprofile_create(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userprofile-list')
    else:
        form = UserProfileForm()
    return render(request, 'app/userprofile_form.html', {'form': form})

def userprofile_update(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('userprofile-detail', pk=userprofile.pk)
    else:
        form = UserProfileForm(instance=userprofile)
    return render(request, 'app/userprofile_form.html', {'form': form})

def userprofile_delete(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    if request.method == "POST":
        userprofile.delete()
        return redirect('userprofile-list')
    return render(request, 'app/userprofile_confirm_delete.html', {'userprofile': userprofile})

# CRUD for Request
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'app/request_list.html', {'requests': requests})

def request_detail(request, pk):
    request_instance = get_object_or_404(Request, pk=pk)
    return render(request, 'app/request_detail.html', {'request': request_instance})

def request_create(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request-list')
    else:
        form = RequestForm()
    return render(request, 'app/request_form.html', {'form': form})

def request_update(request, pk):
    request_instance = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=request_instance)
        if form.is_valid():
            form.save()
            return redirect('request-detail', pk=request_instance.pk)
    else:
        form = RequestForm(instance=request_instance)
    return render(request, 'app/request_form.html', {'form': form})

def request_delete(request, pk):
    request_instance = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        request_instance.delete()
        return redirect('request-list')
    return render(request, 'app/request_confirm_delete.html', {'request': request_instance})



# User Profile View
def user_profile(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
        barangays = Barangay.objects.filter(user=request.user)
        services = Service.objects.filter(user=request.user)
        requests = Request.objects.filter(user=request.user)
        return render(request, 'app/user_profile.html', {
            'posts': posts,
            'barangays': barangays,
            'services': services,
            'requests': requests
        })
    return redirect('login')  # Redirect to login if not authenticated
