from django.shortcuts import render

#  Create your views here.

from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated :
        return redirect('adminapp:adminPage')
    else:
# TODO aquí anira pagina usuaris de consulta
        return render(request, 'home.html')
