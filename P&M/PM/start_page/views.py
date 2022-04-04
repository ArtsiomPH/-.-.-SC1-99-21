from django.shortcuts import render
from .forms import Search
from .models import Medcine, Synonyms
from django.http import HttpResponseRedirect


def index(request):
    search = Search()
    recent_synonyms = Synonyms.objects.order_by("-pub_date")[:5]
    data = {"search_form": search, "recent_synonyms": recent_synonyms}
    return render(request, "start_page/start.html", context=data)


def search_medcine(request):
    search = Search()
    medcine_name = request.GET.get("medcine_name")
    try:
        result = Synonyms.objects.get(comm_name=medcine_name)
    except Synonyms.DoesNotExist:
        return HttpResponseRedirect("/error")
    else:
        medcine_id_in_database = Synonyms.objects.get(comm_name=medcine_name).medcine.id
        medcine = Medcine.objects.get(id=medcine_id_in_database)
        all_synonyms = medcine.synonyms_set.all()
        data = {"search_form":search, "medcine":medcine, "search_name":medcine_name, "synonym":result, "all_synonyms":all_synonyms}
        return render(request, "start_page/search.html", context=data)

def search_param(request, url_name):
    search = Search()
    try:
        result = Synonyms.objects.get(url_name=url_name)
    except Synonyms.DoesNotExist:
        return HttpResponseRedirect("/error")
    else:
        medcine_name = url_name
        medcine_id_in_database = Synonyms.objects.get(url_name=url_name).medcine.id
        medcine = Medcine.objects.get(id=medcine_id_in_database)
        all_synonyms = medcine.synonyms_set.all()
        data = {"search_form":search, "medcine":medcine, "search_name":medcine_name, "synonym":result, "all_synonyms":all_synonyms}
        return render(request, "start_page/search.html", context=data)

def about(request):
    search = Search()
    return render(request, "start_page/about.html", {"search_form": search})

def policy(request):
    search = Search()
    return render(request, "start_page/policy.html", {"search_form": search})

def error(request):
    search = Search()
    return render(request, "start_page/not_in_base.html", {"search_form": search})



