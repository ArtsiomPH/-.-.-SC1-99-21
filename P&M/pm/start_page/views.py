from django.shortcuts import render, redirect
from .forms import Search, Add_medcine, Add_synonyms, Add_literature
from .models import Medcine, Synonyms, General_sources
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.db.models import Sum
from django.contrib import messages
from django.forms import inlineformset_factory
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    search = Search()
    recent_synonyms = Synonyms.objects.order_by("-pub_date")[:5]
    request_range = timezone.now() - timezone.timedelta(days=14)
    popular_medcines = Synonyms.objects.filter(request_counter__date__gt=request_range).annotate(
        sm=Sum("request_counter__count")).order_by("-sm")[:5]
    data = {"search_form": search, "recent_synonyms": recent_synonyms, "popular_medcines": popular_medcines}
    return render(request, "start_page/start.html", context=data)


def search_medcine(request):
    medcine_name = request.GET.get("medcine_name")
    try:
        synonym = Synonyms.objects.get(comm_name=medcine_name.capitalize())
    except Synonyms.DoesNotExist:
        return redirect("start_page:error")
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
        return redirect("start_page:error")
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

@login_required()
def base(request):
    return render(request, "start_page/base_operations.html")

@login_required()
def add_tags(request):
    synonyms = Synonyms.objects.all()
    data = []
    for synonym in synonyms:
        data.append(synonym.comm_name)
    return JsonResponse(data, safe=False)

@login_required()
def create_medcine(request):
    # create synonym's form
    SynonymsFormSet = inlineformset_factory(Medcine, Synonyms, form=Add_synonyms, can_delete=False, extra=2)
    # create literatures form
    SourcesFormSet = inlineformset_factory(Medcine, General_sources, form=Add_literature, can_delete=False, extra=5)
    if request.method == 'POST':
        # new medcine add
        new_medcine = Add_medcine(request.POST)
        if new_medcine.is_valid():
            if not Medcine.objects.filter(international_name=request.POST.get('international_name')).exists():
                new_medcine.save()
                medcine_name = new_medcine.cleaned_data['international_name']
                medcine_object = Medcine.objects.get(international_name=medcine_name)
                medcine_object.general_url_name = medcine_name.lower()
                medcine_object.save()
                synonyms = SynonymsFormSet(request.POST, instance=medcine_object)
                sources = SourcesFormSet(request.POST, instance=medcine_object)
                if sources.is_valid() and synonyms.is_valid():
                    for source in sources:
                        if source.cleaned_data:
                            source.save()
                    for synonym in synonyms:
                        if synonym.cleaned_data:
                            synonym.save()
                    messages.add_message(request, messages.SUCCESS, "Запись добавлена")
                    return redirect('start_page:base')
                else:
                    medcine_object.delete()
                    add_medcine = Add_medcine(request.POST)
                    add_synonyms = SynonymsFormSet(request.POST)
                    add_sources = SourcesFormSet(request.POST)
                    data = {'add_medcine': add_medcine, 'add_synonyms': add_synonyms, 'add_sources': add_sources}
                    return render(request, "start_page/create_base.html", context=data)
            else:
                messages.add_message(request, messages.ERROR,
                                     f'Препарат {request.POST.get("international_name")} есть в базе данных')
                return redirect('start_page:create')
        else:
            add_synonyms = SynonymsFormSet(request.POST)
            add_medcine = Add_medcine(request.POST)
            add_sources = SourcesFormSet(request.POST)
            data = {'add_medcine': add_medcine, 'add_synonyms': add_synonyms, 'add_sources': add_sources}
            return render(request, "start_page/create_base.html", context=data)
    else:
        add_medcine = Add_medcine()
        add_synonyms = SynonymsFormSet()
        add_sources = SourcesFormSet()
        data = {'add_medcine': add_medcine, 'add_synonyms': add_synonyms, 'add_sources': add_sources}
        return render(request, "start_page/create_base.html", context=data)


class Update_base(LoginRequiredMixin, ListView):
    template_name = "start_page/update_base.html"
    context_object_name = 'medcines'
    queryset = Medcine.objects.all()
    paginate_by = 15
    page_kwarg = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['international_name'] = Medcine.objects.all()
        context['general_url_name'] = Medcine.objects.all()
        return context

@login_required()
def update_medcine(request, general_url_name):
    SynonymsFormSet = inlineformset_factory(Medcine, Synonyms, form=Add_synonyms, can_delete=True, extra=2)
    SourcesFormSet = inlineformset_factory(Medcine, General_sources, form=Add_literature, can_delete=True, extra=5)
    medcine_object = Medcine.objects.get(general_url_name=general_url_name)
    if request.method == 'POST':
        # new medcine add
        new_medcine = Add_medcine(request.POST, instance=medcine_object)
        if new_medcine.is_valid():
            new_medcine.save()
            medcine_name = new_medcine.cleaned_data['international_name']
            medcine_object.general_url_name = medcine_name.lower()
            synonyms_formset = SynonymsFormSet(request.POST, instance=medcine_object)
            sources_formset = SourcesFormSet(request.POST, instance=medcine_object)
            if sources_formset.is_valid() and synonyms_formset.is_valid():
                for source in sources_formset:
                    if source.cleaned_data:
                       source.save()
                for synonym in synonyms_formset:
                    if synonym.cleaned_data:
                       synonym.save()
                medcine_object.save()
                messages.add_message(request, messages.SUCCESS, "Запись обновлена")
                return redirect('start_page:update')
            else:
                add_synonyms = SynonymsFormSet(request.POST, instance=medcine_object)
                add_medcine = Add_medcine(request.POST, instance=medcine_object)
                add_sources = SourcesFormSet(request.POST, instance=medcine_object)
                data = {'add_medcine': add_medcine, 'add_synonyms': add_synonyms, 'add_sources': add_sources}
                return render(request, "start_page/create_base.html", context=data)
        else:
            add_synonyms = SynonymsFormSet(request.POST, instance=medcine_object)
            add_medcine = Add_medcine(request.POST, instance=medcine_object)
            add_sources = SourcesFormSet(request.POST, instance=medcine_object)
            data = {'add_medcine': add_medcine, 'add_synonyms': add_synonyms, 'add_sources': add_sources}
            return render(request, "start_page/create_base.html", context=data)
    else:
        add_synonyms = SynonymsFormSet(instance=medcine_object)
        add_sources = SourcesFormSet(instance=medcine_object)
        add_medcine = Add_medcine(instance=medcine_object)
        data = {'add_medcine': add_medcine, 'add_synonyms': add_synonyms, 'add_sources': add_sources}
        return render(request, "start_page/create_base.html", context=data)

@login_required()
def delete_medcine(request, pk):
    medcine = Medcine.objects.get(pk=pk)
    medcine.delete()
    messages.add_message(request, messages.INFO, "Запись удалена")
    return redirect('start_page:update')



