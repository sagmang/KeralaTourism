from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#....home page....
def HOME(request):
    return render(request, 'HOME.html') 
#....sign in page....
def SIGNIN(request):
    return render(request, 'SIGNIN.html') 
#....sign up page....
def SIGNUP(request):
    return render(request, 'SIGNUP.html') 
#....munnar page....
def MUNNAR(request):
    return render(request, 'MUNNAR.html') 
#....alappuzha page....
def ALAPPUZHA(request):
    return render(request, 'ALAPPUZHA.html') 
#....kannur page....
def KANNUR(request):
    return render(request, 'KANNUR.html') 
#....kozhikode page....
def KOZHIKODE(request):
    return render(request, 'KOZHIKODE.html') 
