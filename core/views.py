from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
        'mensagem': "Estudos em Python - Django"
    }
    return render(request, template_name, context)
# Create your views here.
