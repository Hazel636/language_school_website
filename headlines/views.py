from django.shortcuts import render,get_object_or_404
from .models import Headline
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.models import Listing


def headline(request,headline_id):
    headline = get_object_or_404(Headline, pk = headline_id)
    listings = Listing.objects.filter(headline = headline)

    context = {
        'headline': headline,
        'listings': listings,
    }
    return render(request, 'headlines/headline.html', context)

