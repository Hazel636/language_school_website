from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, city_choices, category_choices, country_choices
from django.http import JsonResponse

def index(request):
    listings = Listing.objects.order_by('-is_mvp','-price').filter(is_published=True)

    paginator = Paginator(listings,9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'price_choices': price_choices, 
        'city_choices': city_choices, 
        'country_choices': country_choices, 
        'category_choices': category_choices,
    }

    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    school = listing.school
    context = {
        'listing':listing,
        #'school':school
    }

    return render(request, 'listings/listing.html', context)



def search(request):
    queryset_list = Listing.objects.order_by('-is_mvp','price')
    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(school__city__iexact=city)

    #country
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            queryset_list = queryset_list.filter(school__country__iexact=country)
            
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    #category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__name__iexact=category)

    context = {
        'price_choices': price_choices, 
        'city_choices': city_choices, 
        'category_choices': category_choices, 
        'country_choices': country_choices, 
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)

def get_cities(request):
    country = request.GET.get('country')
    cities = []
    if country == '加拿大':
        cities = [
            {'value': 'Vancouver', 'text': '温哥华'},
            {'value': 'Toronto', 'text': '多伦多'},
        ]
    return JsonResponse({'cities': cities})