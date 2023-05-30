from django.shortcuts import render, redirect

# django auth system
from django.contrib.auth import authenticate, login, logout

# message flashing
from django.contrib import messages

# sign up form
from .forms import SignUpForm, AddRecordForm

# display record from our payments table
from .models import Payment


def home(request):
    payments = Payment.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "Error! Username or Password dont match")

            return redirect('home')
    else:
        return render(request, 'home.html', {'payments': payments})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You Have Successfully Created Your Account")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def clientRecord(request, pk):
    if request.user.is_authenticated:
        # look up the record
        client_rec = Payment.objects.get(id=pk)
        return render(request, "record.html", {'client_rec': client_rec})
    else:
        messages.success(request, "You must be logged in to view the record")
        return redirect('home')

    # delete record


def deleteRecord(request, pk):
    if request.user.is_authenticated:
        client_rec = Payment.objects.get(id=pk).delete()
        messages.success(request, "Successfully Deleted Record")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully")
                return redirect('home')

    else:
        messages.success(request, "You Must be Logged in to add Record")

    return render(request, "add_record.html", {'form': form})
