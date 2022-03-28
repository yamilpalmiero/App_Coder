from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def inicio(request):
    date_init = datetime.now()
    dict_context = {'title':'AppCoder de Yamil', 'message':'Bienvenidos a la pagina de Yamil (ponele)'}
    return render(request, 'appcoder/index.html', dict_context)


def estudiantes(request):
    return render(request, 'appcoder/estudiantes.html')


def profesores(request):
    return render(request, 'appcoder/profesores.html')


def cursos(request):
    return HttpResponse('Vista de cursos')


def entregables(request):
    return HttpResponse('Vista de entregables')