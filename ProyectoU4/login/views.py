from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from login.forms import UserLoginForm

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