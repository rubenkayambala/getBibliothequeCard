from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import CarteForm
from .models import Carte
from .pdf import makepdf
# from django_xhtml2pdf.utils import generate_pdf

def HomeView(request):
    template_name = 'home/index.html'
    return render(request, template_name)


def RegisterView(request):
    template_name = 'home/register.html'
    if request.method == "POST":
        form = CarteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
        else:
            messages.error(request, "Données incorrectes! Réessayez")
            form = CarteForm()
            context = {
                'form': form,
            }
            return render(request, template_name, context)
    form = CarteForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def ListView(request):
    users = Carte.objects.all()
    template_name = 'home/list.html'
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def DetailView(request, id):
    user = Carte.objects.get(id=id)
    template_name = 'home/detail.html'
    context = {
        'user': user,
    }
    return render(request, template_name, context)


def CarteView(request, id):
    user = Carte.objects.get(id=id)
    template_name = 'home/carte.html'
    context = {
        'user': user,
    }
    return render(request, template_name, context)


# def pdf(request):
#     pdf = makepdf("home/carte.html")
#     return HttpResponse(pdf, content_type="application/pdf")



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def pdf(request):
    # carte = Carte.objects.get(id=id)
    template_name = 'home/carte.html'
    # context = {'carte': carte}
    context = {}
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="report.pdf"' 
    template = get_template(template_name)
    html = template.render(context)
    pdf = pisa.CreatePDF(html, dest=response)
    if pdf.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response