from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Mineral


groups = ['Silicates','Oxides','Sulfates','Sulfides','Carbonates',
          'Halides','Sulfosalts','Phosphates','Borates','Organic Minerals',
          'Arsenates','Native Elements','Other']

colors = ['Red','Orange','Yellow','Green','Blue','Pink','Purple', 'White',
          'Black',]


def index(request, letter=None):
    """Get all minerals to display on main page"""
    if letter == None:
        letter = 'A'
    minerals = Mineral.objects.order_by('name').all()
    rand_min = Mineral.objects.order_by('?').first()
    groups
    colors
    return render(request,'index.html',{
                                        'minerals':minerals,
                                        'rand_min':rand_min,
                                        'letter':letter,
                                        'groups':groups,
                                        'colors':colors,
                                        })


def mineral_details(request, pk):
    """Get details of each mineral"""
    mineral = get_object_or_404(Mineral, pk=pk)
    rand_min = Mineral.objects.order_by('?').first()
    groups
    colors
    return render(request,'mineral_details.html',{
                                                 'mineral':mineral,
                                                 'rand_min':rand_min,
                                                 'groups':groups,
                                                 'colors':colors,
                                                 })


def mineral_search(request):
    """Get all minerals from a query search (term)"""
    term = request.GET.get('query')
    min_query = Mineral.objects.order_by('name').filter(
    Q(name__icontains=term)|Q(image_caption__icontains=term)|
    Q(category__icontains=term)|Q(formula__icontains=term)|
    Q(strunz_classification__icontains=term)|Q(color__icontains=term)|
    Q(crystal_system__icontains=term)|Q(crystal_symmetry__icontains=term)|
    Q(cleavage__icontains=term)|Q(category__icontains=term)|
    Q(mohs_scale_hardness__icontains=term)|Q(luster__icontains=term)|
    Q(streak__icontains=term)|Q(diaphaneity__icontains=term)|
    Q(optical_properties__icontains=term)|Q(unit_cell__icontains=term)|
    Q(refractive_index__icontains=term)|Q(group__icontains=term)|
    Q(crystal_habit__icontains=term)|Q(specific_gravity__icontains=term)
    )
    rand_min = Mineral.objects.order_by('?').first()
    groups
    colors
    return render(request,'mineral_search.html',{
                                                'min_query':min_query,
                                                'rand_min':rand_min,
                                                'groups':groups,
                                                'colors':colors,
                                                })


def letter_search(request, letter):
    """Get all minerals with selected initial"""
    min_query = Mineral.objects.order_by('name').filter(name__startswith=letter)
    rand_min = Mineral.objects.order_by('?').first()
    groups
    colors
    return render(request,'mineral_search.html',{
                                                'min_query':min_query,
                                                'rand_min':rand_min,
                                                'letter' :letter,
                                                'groups':groups,
                                                'colors':colors,
                                                })


def group_search(request, group):
    """Get all minerals from a group"""
    min_query = Mineral.objects.order_by('name').filter(
        group__icontains=group
    )
    rand_min = Mineral.objects.order_by('?').first()
    groups
    colors
    return render(request,'mineral_search.html',{
                                                'min_query':min_query,
                                                'rand_min':rand_min,
                                                'groups':groups,
                                                'group': group,
                                                'colors':colors,
                                                })


def color_search(request, color):
    """ Search option based on color """
    min_query = Mineral.objects.order_by('name').filter(
        color__icontains=color
    )
    rand_min = Mineral.objects.order_by('?').first()
    groups
    colors
    return render(request,'mineral_search.html', {
                                                 'min_query':min_query,
                                                 'rand_min':rand_min,
                                                 'groups':groups,
                                                 'colors':colors,
                                                 'color':color,
                                                 })
