from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserEditForm


# Главная страница со списком пользователей
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


# Страница редактирования конкретного пользователя
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'users/user_edit.html', {'form': form, 'user_edited': user})


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form
