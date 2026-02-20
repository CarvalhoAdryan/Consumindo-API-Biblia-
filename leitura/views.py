from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.

def Index(request,versao,livro_abrev,capitulo):

    headers = {
        "Authorization": f"Bearer {settings.BIBLIA_TOKEN}"
    }

    response = requests.get(f"https://www.abibliadigital.com.br/api/verses/{versao}/{livro_abrev}/{capitulo}", headers=headers)

    responsep = requests.get(f"https://www.abibliadigital.com.br/api/books/{livro_abrev}", headers=headers)

    data = responsep.json()

    livro = {
        'cap' : data[ 'chapters']
    }


    try:
        lista = response.json()
    except ValueError:
        print('A resposta não chegou com o formato esperado.')

    contexto = {
        'versiculo': lista['verses'],
        'nome' : lista['book']['name'],
        'reference' : lista['chapter']['number'],
        'versao' : lista['book']['version'],
        'c_atual' : int(capitulo),
        'c_anterior' : max(1, int(capitulo) - 1),
        'c_proximo' : int(capitulo) + 1,
        'ultimo_cap' : livro['cap'],
        'lista_capitulos' : range(1,livro['cap'] + 1),
        'livro_abrev' : livro_abrev
        }


    
    return render(request, 'leitura/index.html', contexto)



def Books(request):
    
    headers = {
        "Authorization": f"Bearer {settings.BIBLIA_TOKEN}"
    }

    response = requests.get(f"https://www.abibliadigital.com.br/api/books", headers=headers)

    try:
        lista = response.json()
    except ValueError:
        print('A resposta não chegou com o formato esperado.')

    contexto = {
        'Livros' : lista,
        }

    return render(request, 'leitura/lista.html', contexto)