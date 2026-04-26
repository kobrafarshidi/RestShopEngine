from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer
from .forms import CustomUserCreationForm
from .models import User
from orders.models import Order


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '✅ ثبت‌نام با موفقیت انجام شد! لطفاً وارد شوید.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == 'email':
                        messages.error(request, f'❌ ایمیل: {error}')
                    elif field == 'password1':
                        messages.error(request, f'❌ رمز عبور: {error}')
                    elif field == 'password2':
                        messages.error(request, f'❌ تکرار رمز عبور: {error}')
                    elif field == 'username':
                        messages.error(request, f'❌ نام کاربری: {error}')
                    else:
                        messages.error(request, f'❌ {error}')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'✅ خوش آمدید {user.username}!')
            return redirect('home')
        else:
            messages.error(request, '❌ نام کاربری یا رمز عبور اشتباه است.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, '✅ شما با موفقیت خارج شدید.')
    return redirect('home')


@login_required
def profile_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'accounts/profile.html', {'orders': orders})


# API Views
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=201)
        return Response(serializer.errors, status=400)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)