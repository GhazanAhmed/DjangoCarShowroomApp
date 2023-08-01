from django.shortcuts import render
from .models import Brand, Staff


def index(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'car_showroom/index.html', context)

def brand_detail(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    context = {'brand': brand}
    return render(request, 'car_showroom/brand_detail.html', context)

def team(request):
    staff_members = Staff.objects.all()
    context = {'staff_members': staff_members}
    return render(request, 'car_showroom/team.html', context)
