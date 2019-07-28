import os
import json
from django.core.management.base import BaseCommand
from mineral_catalog.settings import BASE_DIR
import numpy as np
import matplotlib.pyplot as plt


class Command(BaseCommand):
    help = 'Plots graph showing the distribution of the keys in JSON file'

    def handle(self, *args, **options):
        data_folder = os.path.join(BASE_DIR, 'minerals', 'resources')
        with open(os.path.join(data_folder,'minerals.json')) as json_file:
            catalog = json.load(json_file)
            # A list of dicts
        counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for mineral in catalog:
            count = 0
            mineral_properties = [
                mineral.get('name'),
                mineral.get('image_filename'),
                mineral.get('image_caption'),
                mineral.get('category'),
                mineral.get('formula'),
                mineral.get('strunz_classification'),
                mineral.get('unit_cell'),
                mineral.get('color'),
                mineral.get('crystal_symmetry'),
                mineral.get('crystal_system'),
                mineral.get('cleavage'),
                mineral.get('mohs_scale_hardness'),
                mineral.get('luster'),
                mineral.get('streak'),
                mineral.get('diaphaneity'),
                mineral.get('optical_properties'),
                mineral.get('refractive_index'),
                mineral.get('crystal_habit'),
                mineral.get('specific_gravity'),
                mineral.get('group')
            ]
            for value in mineral_properties:
                if value == None:
                    count += 1
                else:
                    sum = counts[count]
                    sum += 1
                    counts[count] = sum
                    count += 1
        x_labels = [
            'name','image_filename','image_caption','category',
            'formula','strunz_classification','unit_cell','color',
            'crystal_symmetry','crystal_system','cleavage',
            'mohs_scale_hardness','luster','streak','diaphaneity',
            'optical_properties','refractive_index','crystal_habit',
            'specific_gravity','group'
            ]
        # Export figure of the sum of each property
        plt.subplots(figsize=(12, 9), tight_layout=True)
        plt.title('Mineral catalog summary', fontsize=10)
        plt.ylabel('Counts')
        plt.xticks(rotation=75)
        plt.plot(x_labels, counts)
        plt.savefig(os.path.join(data_folder,'data.png'))
        print('A summary figure was generated in {}'.format(data_folder))
