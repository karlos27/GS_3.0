from django.shortcuts import render, redirect

from .models import noticia
from .forms import ContactForm
from django.views.generic import ListView

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages



# Create your views here.

def news(request):
	noticies = noticia.objects.order_by('-data_pub')[:3]
	context = {
		'noticies' : noticies,
	}
	return render(request, 'gestoria/templates/index.html', context)

class llistat(ListView):
    model = noticia
    template_name = 'gestoria/templates/noticies.html'
    paginate_by = 5

def map(request):
    return render(request, 'gestoria/templates/nosaltres.html', {})

def resposta(request):
    return render(request, 'gestoria/templates/resposta.html', {})

def contacte(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():   
        nom = form.cleaned_data.get('nom')
        correu = form.cleaned_data.get('correu')
        telf = form.cleaned_data.get('telf')
        missatge = form.cleaned_data.get('missatge')
        assumpte = 'Contacte Pàgina Web'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from]
        miss = "%s: %s. Enviat per %s Telf.: %s" %(nom, missatge, correu, telf)
        send_mail(
            assumpte,
            miss,
            email_from,
            email_to,
            )
        messages.success(request, 'Has rebut un correu de contacte.')
        return redirect('gestoria:resposta')
    context = {
        'form':form,
    }
    return render(request, 'gestoria/templates/contacte.html', context)
