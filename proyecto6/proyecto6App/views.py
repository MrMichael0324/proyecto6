from django.shortcuts import render
from proyecto6App.models import Proyecto
from proyecto6App.form import ProyectoForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listaproyecto(request):
    proyecto = Proyecto.objects.all()
    data= {'proyectos':proyecto}
    return render(request, 'proyecto.html',data)

def agregarproyecto(request):
    form = ProyectoForm()
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data= {'form':form}
    return render(request, 'agregarproyecto.html',data)

def editarproyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = ProyectoForm(instance=proyecto)
    data = {'form': form}
    return render(request, 'editarproyecto.html', data)

def eliminarproyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return index(request)



