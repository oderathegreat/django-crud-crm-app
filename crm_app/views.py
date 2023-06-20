from django.http import JsonResponse
from django.shortcuts import render, redirect

# django auth system
from django.contrib.auth import authenticate, login, logout

# message flashing
from django.contrib import messages

# sign up form
from .forms import SignUpForm, AddRecordForm

# display record from our payments table
from .models import Payment

# view set from rest-framework
from rest_framework import viewsets

from .serializers import TransSerializer
from .models import Trans


class Transdata(viewsets.ModelViewSet):
    queryset = Trans.objects.all().order_by('amount')
    serializer_class = TransSerializer


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
    messages.success(request, "You Have Been Logged Out ")
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
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to view the record")
        return redirect('home')

    form = AddRecordForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record added successfully")
            return redirect('/')

    return render(request, "add_record.html", {'form': form})


# perform migrations for test transactions
def test_transactions(request):
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, you must be logged in first")
        return redirect('home')

    if request.method == "POST":
        amount = request.POST.get('amount')
        transcode = request.POST.get('transcode')

        trans_data = Trans(amount=amount, transcode=transcode, user=request.user)
        trans_data.save()
        messages.success(request, "Transaction data saved successfully")

    return render(request, "testtrans.html")


def login_api(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request'}, status=400)
