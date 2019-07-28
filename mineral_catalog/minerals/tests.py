from django.urls import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name= "Abelsonite",
            image_filename= "Abelsonite.jpg",
            image_caption= "Abelsonite from the Green River Formation",
            category= "Organic",
            formula= "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification= "10.CA.20",
            crystal_system= "Triclinic",
            streak= "Pink",
            diaphaneity= "Semitransparent",
            optical_properties= "Biaxial",
            group= "Organic Minerals"
            )
        rock_test = Mineral.objects.get(name = 'Abelsonite')
        self.assertEqual(rock_test.name, 'Abelsonite')


class MineralViewTest(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name= "Zoisite",
            image_filename= "Zoisite.jpg",
            image_caption= "Yellow zoisite crystal (1.7 x 1 x 0.8 cm)",
            category= "Sorosilicate - epidote group",
            group= "Silicates"
            )
        self.mineral2 = Mineral.objects.create(
            name= "Zorite",
            image_filename= "Zorite.jpg",
            image_caption= "Zorite",
            category= "Inosilicate",
            group= "Silicates"
            )
        self.mineral3 = Mineral.objects.create(
            name= "Zunyite",
            image_filename= "Zunyite.jpg",
            image_caption= "Sharp, pyramids of brown-red zunyite",
            category= "Sorosilicates",
            group= "Silicates"
            )

    def test_model_views(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mineral3, response.context['minerals'])
        self.assertIn(self.mineral2, response.context['minerals'])
        self.assertIn(self.mineral2, response.context['minerals'])

    def test_mineral_detail_view(self):
        response = self.client.get(reverse('mineral_details',
                                       kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_details.html')
        self.assertEqual(self.mineral2, response.context['mineral'])
