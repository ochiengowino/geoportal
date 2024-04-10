from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, UserPassword, Counties
from .serializers import countiesSerializer

# Create your views here.
def counties_api(request):
    if request.method == 'GET':
        counties = Counties.objects.all()
        counties_serializer = countiesSerializer(counties, many=True)
        
        return JsonResponse(counties_serializer.data, safe=False, status=200)
    
def dashboard(request):
    return render(request, 'frontend/index.html')

def home(request):
    return render(request, 'geo_app/index.html')


def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        date_of_birth = request.POST['date_of_birth']


        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
        return redirect('set_password', user_id=user.user_id)

    return render(request, 'geo_app/signup.html')

def set_password(request, user_id):
    user = User.objects.get(user_id=user_id)
  

    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user_password = UserPassword.objects.create(user=user, password=password)

            # Redirect to the login page after setting the password
            return redirect('login')

    return render(request, 'geo_app/set_password.html', {'first_name': user.first_name, 'user_id': user_id})

def user_login(request):
    # return redirect('login')
    return render(request, 'geo_app/georasters/index.html')

def user_logout(request):
    return redirect('login')

# def dashboard(request):
#     pass