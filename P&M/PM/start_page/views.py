from django.shortcuts import render
from .forms import Search
from .models import Medcine
from .models import Synonyms
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect


def index(request):
    search = Search()
    return render(request, "start_page/start.html", {"search_form": search})


def search_medcine(request):
    search = Search()
    medcine_name = request.GET.get("medcine_name")
    try:
        result = Synonyms.objects.get(name=medcine_name)
    except Exception:
        return render(request, "start_page/not_in_base.html")
    else:
        medcine_id_in_database = Synonyms.objects.get(name=medcine_name).medcine.id
        medcine = Medcine.objects.get(id = medcine_id_in_database)
        all_synonyms = medcine.synonyms_set.all()
        data = { "search_form":search, "medcine":medcine, "search_name":medcine_name, "synonym":result, "all_synonyms":all_synonyms}
        return render(request, "start_page/search.html", context=data)

