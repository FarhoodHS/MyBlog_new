from django.shortcuts import render, redirect, Http404
from .forms import SignupForm, DashboardForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already a registered user :|')
        return redirect('posts:post_list')
    form = SignupForm()
    if request.method == 'POST':
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            messages.success(request, 'You are now a registered user :D')
            return redirect('home')
        else:
            ex_form = form.cleaned_data
            context = {
                'form': form,
                'ex_form': ex_form
            }
    else:
        context = {
            'form': form
        }

    return render(request, 'signup_form.html', context)


def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to login first!')
        return redirect('posts:post_list')
    if request.method == 'POST':
        form = DashboardForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            if form.has_changed():
                messages.success(request, 'Changes saved successfully :)')
            else:
                messages.info(request, 'No changes made :|')
    else:
        form = DashboardForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('posts:post_list')

        # form = DashboardForm(initial={
        #     'first_name': request.user.first_name,
        #     'last_name': request.user.last_name,
        #     'email': request.user.email,
        #     'username': request.user.username,
        #     'profile_pic': request.user.profile_pic,
        # })


def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        if '@' in id:
            credential = 'Email'
            try:
                user = Profile.objects.get(email=id)
                id = user.username
                user = auth.authenticate(username=id, password=password)
            except Profile.DoesNotExist:
                messages.error(
                    request, f'{credential} or Password is incorrect :(')
                return render(request, 'login_form.html')
        else:
            credential = 'Username'
            user = auth.authenticate(username=id, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in :)')
            return redirect('posts:post_list')
        else:
            messages.error(
                request, f'{credential} or Password is incorrect :(')
    return render(request, 'login_form.html')
