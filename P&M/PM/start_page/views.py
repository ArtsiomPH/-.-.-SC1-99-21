from django.shortcuts import render, redirect
from .forms import Search
from .models import Medcine, Synonyms, General_sources
from django.http import HttpResponseRedirect


def index(request):
    search = Search()
    recent_synonyms = Synonyms.objects.order_by("-pub_date")[:5]
    data = {"search_form": search, "recent_synonyms": recent_synonyms}
    return render(request, "start_page/start.html", context=data)


def search_medcine(request):
    medcine_name = request.GET.get("medcine_name")
    try:
        result = Synonyms.objects.get(comm_name=medcine_name)
    except Synonyms.DoesNotExist:
        return HttpResponseRedirect("/error")
    else:
        return redirect("start_page:search_param", result.url_name)

def search_param(request, url_name):
    search = Search()
    try:
        result = Synonyms.objects.get(url_name=url_name)
    except Synonyms.DoesNotExist:
        return HttpResponseRedirect("/error")
    else:
        medcine = Medcine.objects.get(synonyms__url_name=url_name)
        all_synonyms = medcine.synonyms_set.all().exclude(url_name=url_name)
        general_sources = medcine.general_sources_set.all()
        data = {"search_form":search, "medcine":medcine, "synonym":result, "all_synonyms":all_synonyms, "sources":general_sources}
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



