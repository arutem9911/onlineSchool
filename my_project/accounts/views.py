from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import LoginForm
from accounts.models import User
from django.urls import reverse_lazy


# class RegisterView(CreateView):
#     model = User
#     template_name = 'register.html'
#     form_class = RegisterForm
#
#     def form_invalid(self, form):
#         print(form.initial)
#
#     def form_valid(self, form):
#         user = form.save()
#         Profile.objects.create(user=user)
#         login(self.request, user)
#         return redirect('main')


class LoginAccView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = None
            user = authenticate(request=request, username=username, password=password)

            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('main')

            error_message = "Wrong email/username or password."
            return render(request, 'login.html', {'error_message': error_message})

        return render(request, 'login.html')


# class LogoutConfirm(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'logout.html')
#
#     def post(self, request, *args, **kwargs):
#         return redirect('logout')
#
#
# class LogoutAccView(LogoutView):
#     pass


# class ProfileView(DetailView):
#     model = get_user_model()
#     template_name = 'profile/profile.html'
#     context_object_name = 'user'
#     pk_url_kwarg = 'id'


# class UserUpdate(UpdateView):
#     model = get_user_model()
#     form_class = UserUpdateForm
#     template_name = 'profile/update_profile.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'user'
#
#     def test_func(self):
#         return self.request.user == self.get_object()
#
#     def get_success_url(self):
#         return reverse_lazy('profile', kwargs={'id': self.object.id})
