from django.shortcuts import render, redirect
from .forms import Search
from .models import Medcine, Synonyms
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Sum



def index(request):
    search = Search()
    recent_synonyms = Synonyms.objects.order_by("-pub_date")[:5]
    request_range = timezone.now() - timezone.timedelta(days=7)
    popular_medcines = Synonyms.objects.filter(request_counter__date__gt=request_range).annotate(
        sm=Sum("request_counter__count")).order_by("-sm")[:5]
    data = {"search_form": search, "recent_synonyms": recent_synonyms, "popular_medcines": popular_medcines}
    return render(request, "start_page/start.html", context=data)


def search_medcine(request):
    medcine_name = request.GET.get("medcine_name")
    try:
        synonym = Synonyms.objects.get(comm_name=medcine_name)
    except Synonyms.DoesNotExist:
        return HttpResponseRedirect("/error")
    else:
        view, created = synonym.request_counter_set.get_or_create(synonym=synonym.id, date=timezone.now())
        view.count = view.count + 1
        view.save(update_fields=["count"])
        return redirect("start_page:search_param", synonym.url_name)


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
        data = {"search_form": search, "medcine": medcine, "synonym": result, "all_synonyms": all_synonyms,
                "sources": general_sources}
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
