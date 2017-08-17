from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

from .models import perfil, arxius
from .forms import RegistreForm, PerfilForm, UserForm
from gestoria.models import noticia


from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

# Create your views here.

class RegistreUsuari(CreateView):
	model = User
	template_name = 'usuaris/templates/registre.html'
	form_class = RegistreForm
	success_url = reverse_lazy('login')

@login_required
@transaction.atomic
def Perfil(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = PerfilForm(request.POST, instance=request.user.perfil)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '%(Correu)s, ha actualitzat el seu perfil!')
            return redirect('usuaris:inici')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = PerfilForm(instance=request.user.perfil)
    return render(request, 'usuaris/templates/perfil.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def inici(request):
	return render(request, 'usuaris/templates/inici.html', {})

class descarregues(ListView):
    template_name = 'usuaris/templates/descarregues.html'
    paginate_by = 5
    def get_queryset(self, *args, **kwargs):
        return arxius.objects.filter(usuari=self.request.user)

