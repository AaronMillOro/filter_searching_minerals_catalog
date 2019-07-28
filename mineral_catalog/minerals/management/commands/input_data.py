"""
Logic to add multiple rows into Model generated in Django.
Kind acknowledgements to Happiness Nwosu and Vitor Freitas
for they posts that helped me to make part of the code
sources:
https://tinyurl.com/y52r7lya
https://tinyurl.com/y67my58o
"""
import os
import json
from django.core.management.base import BaseCommand
from mineral_catalog.settings import BASE_DIR
from minerals.models import Mineral


class Command(BaseCommand):
    help = 'Loads JSON file named mineral.json'

    def handle(self, *args, **options):
        data_folder = os.path.join(BASE_DIR, 'minerals', 'resources')
        with open(os.path.join(data_folder,'minerals.json')) as json_file:
            catalog = json.load(json_file)
            # A list of dicts
        i = 0
        for mineral in catalog:
            i += 1
            row = Mineral.objects.create(
                name= mineral.get('name'),
                image_filename= mineral.get('image_filename'),
                image_caption= mineral.get('image_caption'),
                category= mineral.get('category'),
                formula= mineral.get('formula'),
                strunz_classification= mineral.get('strunz_classification'),
                unit_cell= mineral.get('unit_cell'),
                color= mineral.get('color'),
                crystal_symmetry= mineral.get('crystal_symmetry'),
                crystal_system= mineral.get('crystal_system'),
                cleavage= mineral.get('cleavage'),
                mohs_scale_hardness= mineral.get('mohs_scale_hardness'),
                luster= mineral.get('luster'),
                streak= mineral.get('streak'),
                diaphaneity= mineral.get('diaphaneity'),
                optical_properties= mineral.get('optical_properties'),
                refractive_index= mineral.get('refractive_index'),
                crystal_habit= mineral.get('crystal_habit'),
                specific_gravity= mineral.get('specific_gravity'),
                group= mineral.get('group')
            )
            row.save()
            if i % 100 == 0:
                print('Loading minerals ...')
        print('A total of {} entries were added to the database !!!'.format(i))
