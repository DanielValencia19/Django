from django.shortcuts import render,redirect,get_object_or_404
from . models import Personas
from django.http import JsonResponse, HttpResponse 
import json

# Create your views here.

def inicio(request):
    return render(request,'persona/registro.html')

def registrar_persona(request):
    if request.method== 'POST':
        documento=request.POST.get('documento')
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        direccion=request.POST.get('direccion')
        correo=request.POST.get('correo')
        
        persona=Personas(
            documento=documento,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            correo=correo,
        )
        
        persona.save()
    return redirect('inicio')

def listar_personas(request):
    personas=Personas.objects.all()
    data={
        'personas':personas,
    }
    return render(request,"persona/listar.html",data)
def eliminar_persona(request,id):
    persona=Personas.objects.get(id=id)
    persona.delete()
    return redirect("listar_personas")

def pre_editar_persona(request,id):
    personas= Personas.objects.get(id=id)
    data={
        "personas":personas,
        
    }
    return render(request,"persona/editar.html",data)

def actualizar_persona(request,id):
    if request.method == "POST":
        personas=Personas.objects.get(id=id)
        
        personas.documento =request.POST.get('documento')
        personas.nombre=request.POST.get('nombre')
        personas.apellido=request.POST.get('apellido')
        personas.direccion=request.POST.get('direccion')
        personas.correo=request.POST.get('correo')

        personas.save()
    
    return redirect('listar_personas')