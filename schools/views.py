from django.shortcuts import render,get_object_or_404
from .models import School
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.models import Listing

def index(request):
    schools = School.objects.order_by('-is_mvp').filter(is_published=True)

    paginator = Paginator(schools,9)
    page = request.GET.get('page')
    paged_schools = paginator.get_page(page)

    context = {
        'schools': paged_schools
    }
    return render(request,'schools/schools.html',context)

def school(request,school_id):
    school = get_object_or_404(School, pk = school_id)
    listings = Listing.objects.filter(school = school)

    context = {
        'school': school,
        'listings': listings,
    }
    return render(request, 'schools/school.html', context)

