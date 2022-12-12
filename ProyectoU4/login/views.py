from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login

from login.models import FormProyecto
from login.forms import UserLoginForm, FormularioUsusariCustom
from login.forms import FormProyectoForm

# Create your views here.
# class LoginView(View):
#     def get(request,self):
#         form = UserLoginForm()
#         context = {'form': form}
#         return render(request, 'login.html', context)
    
#     def post(self, request):
#         formulario = UserLoginForm(request.POST)
#         if formulario.is_valid():
#             request.session['user_name_insert'] = formulario.cleaned_data['user_name']
#             request.session['password_insert'] = formulario.cleaned_data['password']
    
#             return HttpResponse('Valores guardados en sesion')
#         return HttpResponse('Valores del formulario invalidos')

class Vistaindex(View):
    def get(self, request):
        return render(request, 'index.html')
    
    

def form_proyecto(request):
    form = FormProyectoForm(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Proyecto insertado correctamente.')
        form = FormProyectoForm()
    else:
        messages.error(request, 'Error al insertar un Proyecto. Revise los datos.')
    context = {'form': form }      
    return render(request, 'proyecto.html', context)

class Form_proyecto(View):
    def post(self, request):
        form = FormProyectoForm(request.POST or None)
        if form.is_valid():
            form.save()		
            messages.success(request, 'Proyecto insertado correctamente.')
            form = FormProyectoForm()
        else:
            messages.error(request, 'Error al insertar un Proyecto. Revise los datos.')
        context = {'form': form }      
        return render(request, 'proyecto.html', context)
    


def registro(request):
    data = {
        'form': FormularioUsusariCustom()
    }
    
    if request.method == 'POST':
        formulario = FormularioUsusariCustom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.changed_data['password1'])
            login(request, user)
            messages.success(request, 'Ususario registrado correctamente')
            return redirect('login:registroUsuario')
        data['form']= formulario
    return render(request, 'registration/registro.html', data)


#listado de productos
class ListaProyectos(ListView):
    model = FormProyecto
    template_name = 'index.html'
    # Added query to limit amount of results
    queryset = FormProyecto.objects.filter()[:30]