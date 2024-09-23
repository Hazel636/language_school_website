from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from headlines.models import Headline
from listings.choices import price_choices, city_choices, country_choices, category_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    headlines = Headline.objects.order_by('-created_at')

    paginator = Paginator(headlines,4)
    page = request.GET.get('page')
    paged_headlines = paginator.get_page(page)

    context = {
        'headlines': paged_headlines
    }

    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')
