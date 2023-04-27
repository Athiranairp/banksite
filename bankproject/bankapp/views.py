from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.forms import forms
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import District, Branch
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



# Create your views here.
def base(request):
    return render(request, 'base.html')


def submission(request):
    return render(request, 'submitpage.html')

#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('person_add')
#         else:
#             error_message = "Invalid username or password"
#             return render(request, 'register.html', {'error_message': error_message})
#     else:
#         return render(request, 'login.html')
#
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('person_add')
        else:
            messages.success(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')


def home_view(request):
    return render(request, 'homenew.html')


from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Branch


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted.')
            # Redirect to the home page
            return redirect(reverse('submission'))
    return render(request, 'registration_form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)


            # Redirect to the home page
            return redirect(reverse('submission'))

    return render(request, 'registration_form.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(branch.values('id', 'name')), safe=False)


def logout(request):
    logout(request)
    return redirect('login')
