from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from loremipsum import Generator
from .models import Engine
# Create your views here.

def index(request):
    context = {
        'latest_engine_list': Engine.objects.order_by('-pub_date')[:5],
    }
    return render(request, 'engines/index.html', context)
    # return JsonResponse(context)

def detail(request, engine_id):
    engine = Engine.objects.filter(id=engine_id)[0]
    paragraph_count = int(request.GET.get('paragraph_count') if request.GET.get('paragraph_count') is not None else 0)
    context = {
        'engine': engine,
        'paragraph_count': request.GET.get('paragraph_count'),
        'generated_paragraphs': generate_paragraphs(engine, paragraph_count) if paragraph_count > 0 else None
    }

    return render(request, 'engines/detail.html', context)
    # return JsonResponse(context)

def generate(request, engine_id=None, paragraph_count=None):
    engine = Engine.objects.filter(id=engine_id)[0]
    paragraph_count = paragraph_count if paragraph_count is not None else 2
    paragraphs = generate_paragraphs(engine, paragraph_count)

    return JsonResponse({ 'engine_id': engine_id, 'engine_name': engine.name, 'paragraphs': paragraphs })


# util
def generate_paragraphs(engine, paragraph_count):
    # defined engine
    # engine = Engine.objects.filter(id=engine_id)[0]
    # configured generator
    g = Generator(engine.sample, engine.dictionary.split('\n'))

    def get_text_only(item): return item[2]

    paragraphs = list(map(get_text_only, list(g.generate_paragraphs(int(paragraph_count)))))
    return paragraphs