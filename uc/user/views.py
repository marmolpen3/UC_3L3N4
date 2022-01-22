from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import RegisterForm


class Login(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True


class Register(FormView):
    template_name = 'user/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form, **kwargs):
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        return super().form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(form=form)
        context['error'] = True
        return self.render_to_response(context)


class Index(TemplateView):
    template_name = 'user/index.html'
