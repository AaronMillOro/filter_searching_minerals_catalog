from django.shortcuts import render, get_object_or_404

from .models import Mineral

def index(request):
    """Get all minerals to display on main page"""
    minerals = Mineral.objects.order_by('name').all()
    rand_min = Mineral.objects.order_by('?').first()
    # 'minerals' and 'rand_min' are dictionaries sent to template
    return render(request,'index.html',{
                                        'minerals':minerals,
                                        'rand_min':rand_min
                                        })

def mineral_details(request, pk):
    """Get details of each mineral"""
    mineral = get_object_or_404(Mineral, pk=pk)
    rand_min = Mineral.objects.order_by('?').first()
    return render(request,'mineral_details.html',{
                                                 'mineral':mineral,
                                                 'rand_min':rand_min
                                                 })
