from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Estas en la pagina principal")


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta numero {question_id}")