from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request, 'login_session_app/index.html')



def register(request):
    #validations

    
    if len(request.POST['first_name']) < 2:
        messages.error(request, 'Your first name is too short')

    if len(request.POST['last_name']) < 2:
        messages.error(request, 'Your last name is too short')


    if len(request.POST['email']) < 2:
        messages.error(request, 'Your email is too short')

    if len(request.POST['email']) < 8:
        messages.error(request, 'Your email is too short')

    if request.POST['password'] != request.POST['passwordConfrim']:
        messages.error(request, 'Your password do not match.')

    



    # user = User.objects.create(first_name = request.POST['first_name'],
    #                             last_name = request.POST['last_name'],
    #                             email=request.POST['email'],)
    # if user:
    #     print("created user")
    #     request.session['email'] = request.POST['email']
    #     return redirect ('/home')

    return redirect('/')


def login(request):
    print(request.POST)

    matched_user = User.objects.get(email=request.POST['email'])
    
    if matched_user:
        print("matched user!")
        print(matched_user.email)
        request.session['email'] = request.POST['email']

  

    print(request.session['email'])
    print(request.session["email"])
    
    return redirect('/home')

def home(request):

    # if not request.session.get('email'):
    # if not 'email' in request.session:

    #     return redirect('/')
    matched_user = User.objects.get(email=request.session['email'])

    context ={'my_shirts': Shirt.objects.filter(created_by=matched_user),
    'not_my': Shirt.objects.exlude(created_by=matched_user),
    'all_shirts': Shirt.objects.all(),
    }


    al


    return render(request, "login_session_app/home.html", context)


def logout(request):
    request.session.clear()
    return redirect('/')



def create(request):
    print(request.POST)

    #get user object
    current_user = User.objects.get(email=request.session['email'])
    print(current_user)

    Shirt.objects.create(size=request.POST['size'],
                        color=request.POST['color'],
                        material=request.POST['material'],
                        created_by=current_user)

    return redirect('/home')


def event(request):

    return redirect('/')


def event_show(request):

    return redirect('/')