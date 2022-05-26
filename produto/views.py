from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Produtos
from .forms import ProdutoForm

def listar(request):
    produtos = Produtos.objects.all()
    template_name = 'listar.html'
    context = {
        'produtos': produtos
    }
    return render(request, template_name, context)

def novo(request):
    print('method.POST:', request.method)
    if request.method == 'POST':
        print('method.POST:', request.POST)
        form = ProdutoForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('produto:listar')
    else:
        template_name = 'novo.html'
        context = {
            'form': ProdutoForm()
        }
        forms = ProdutoForm()
        for form in forms:
            print(dir(form))
        return render(request, template_name, context)

def alterar(request, pk):
    produto = Produtos.objects.get(id=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto:listar')
    else:
        template_name = 'alterar.html'
        context = {
            'form': ProdutoForm(instance=produto),
            'pk': pk
        }
        return render(request, template_name, context)

def deletar(request, pk):
    produto = Produtos.objects.get(id=pk)
    produto.delete()
    return redirect('produto:listar')
    
