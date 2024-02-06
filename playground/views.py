from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Query

def filter_queries(request, query_id):
    query = {
        "query_id": query_id,
        "title": "The Beginning of the End",
        "description": "The end is nigh!",
        "status": "SUBMITTED",
        "submitted_by": "Valar Morgulis",  
    }
    return JsonResponse(query)

def say_hello(request):
    all_queries = Query.objects.all()  # Correct model name
    context = {'queries': filter_queries}
    return render(request, "hello.html", context)

class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama refuses Valentine shots"},
            {"id": 2, "title": "The Beginning of the End: Valentine's Day Massacre"},
            {"id": 3, "title": "The End of the Beginning: Your eyes go see shege!"},
        ]

    def get(self, request):
        return JsonResponse({"result": self.queries})