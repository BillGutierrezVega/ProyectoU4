from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

from login.forms import UserLoginForm
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
    
    