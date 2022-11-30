from django.http import HttpResponse
from django.shortcuts import render


def primeiraurl(request):
    return HttpResponse('Minha primeira URL')

def meunome(request):
    nome = request.GET.get('nome', 'desconhecido')
    sobrenome = request.GET.get('sobrenome', '')
    return HttpResponse(f'Seu nome é {nome} {sobrenome}')

def minhaidade(request, idade):
    return HttpResponse(f'Sua idade é {idade} anos')

def primeiratela(request):
    return render(request, 'primeiratela.html')

def templatesexemplo(request):
    nome = request.GET.get('nome', 'desconhecido')
    context = {
        'nome': nome,
        'amigos': [
            'João',
            'Pedro',
            'Caio',
        ],
        'animals': {
            'dog': 'Cachorro',
            'cat': 'Gato',
            'bird': 'Pássaro'
        }
    }
    return render(request, 'templatesexemplo.html', context)

def cadastrarestudante(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birthdate = int(request.POST.get('birthdate'))
        enteryear = int(request.POST.get('enteryear'))
        return HttpResponse(f'{name} {birthdate} {enteryear}')
    return render(request, 'cadastrarestudante.html')