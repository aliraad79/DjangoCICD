from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def greet(request, name: str, age: int):
    return HttpResponse(f"Hello, {name}. You're {age} years old.")
