from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Engine
from lipsunation.engines.lib.ipsum import get_paragraphs

def index(request):
    context = {
        'latest_engine_list': Engine.objects.order_by('name'),
    }
    return render(request, 'engines/index.html', context)
    # return JsonResponse(context)

def detail(request, slug):
    engine = get_object_or_404(Engine, slug=slug)
    if request.POST.get('paragraph_count'):
        return redirect('engines:lorem_ipsum', slug=slug, paragraph_count=request.POST['paragraph_count'])
    else:
        paragraph_count = int(request.POST.get('paragraph_count') if request.POST.get('paragraph_count') is not None else 0)
        context = {
            'engine': engine,
            'paragraph_count': request.POST.get('paragraph_count'),
            'generated_paragraphs': get_paragraphs(engine, paragraph_count) if paragraph_count > 0 else None
        }

        return render(request, 'engines/detail.html', context)

def lorem_ipsum(request, slug=None, paragraph_count=None):
    engine = get_object_or_404(Engine, slug=slug)
    paragraph_count = int(paragraph_count if paragraph_count is not None else 2)
    paragraphs = get_paragraphs(engine, paragraph_count)

    return render(request, 'engines/lorem_ipsum.html', { 'engine': engine, 'generated_paragraphs': paragraphs })

