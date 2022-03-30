from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso, Estudiante
from appcoder.forms import CursoFormulario



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
    return HttpResponse('appcoder/cursos.html')


def entregables(request):
    return HttpResponse('appcoder/entregables.html')


def formulario_curso(request):
    if request.method=='post':
        curso=CursoFormulario(request.post)
        if curso.is_valid:
            data=curso.cleaned_data
            curso_nuevo=Curso(data['nombre'], data['comision'])
            curso_nuevo.save()
        return render(request, 'appcoder/index.html')
    else:
        curso=CursoFormulario()
        return render(request, 'appcoder/cursos_form.html', {'formulario':curso})


def buscarCurso(request):
    data=request.POST['comision']
    if data:
        curso=Curso.objects.filter(comision__icontains=data)
        return render(request, 'appcoder/busquedaCurso.html', {'curso':curso[0]})
    return render(request, 'appcoder/busquedaCurso.html')