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
            name= "Acanthite",
            image_filename= "Acanthite.jpg",
            image_caption= """Acanthite on calcite - Locality: Freiberg District,
            Erzgebirge- Scale is one inch with a rule at one cm""",
            category= "Sulfide",
            color="Iron-black",
            group= "Silicates",
            )
        self.mineral2 = Mineral.objects.create(
            name= "Alluaudite",
            image_filename= "Alluaudite.jpg",
            image_caption= "Alluaudite",
            category= "Phosphate",
            color= """Dirty yellow to brownish yellow, grayish green;
            superficially dull greenish black, brownish black,
            black, when altered""",
            group= "Phosphates"
            )
        self.mineral3 = Mineral.objects.create(
            name= "Zunyite",
            image_filename= "Zunyite.jpg",
            image_caption= "Sharp, pyramids of brown-red zunyite",
            category= "Sorosilicates",
            color="Grayish white, flesh-red; colorless in thin section",
            group= "Silicates"
            )
        self.mineral4 = Mineral.objects.create(
            name= "Allanpringite",
            image_filename= "Allanpringite.jpg",
            image_caption= "Picture width 4 mm",
            category= "Phosphate",
            color="Pale brownish yellow",
            group= "Phosphates"
            )

    def test_model_views(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.mineral3, response.context['minerals'])
        self.assertIn(self.mineral2, response.context['minerals'])
        self.assertIn(self.mineral1, response.context['minerals'])

    def test_mineral_detail_view(self):
        response = self.client.get(reverse('mineral_details',
                                       kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_details.html')
        self.assertEqual(self.mineral2, response.context['mineral'])

    def test_group_search_view(self):
        response = self.client.get(reverse('group_search',
                                           kwargs={'group': 'Phosphates'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_search.html')
        self.assertContains(response, self.mineral4.group)

    def test_letter_search_view(self):
        response = self.client.get(reverse('letter_search',
                                           kwargs={'letter': 'A'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_search.html')
        self.assertContains(response, self.mineral2.name)

    def test_color_search_view(self):
        response = self.client.get(reverse('color_search',
                                           kwargs={'color': 'White'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mineral_search.html')
        self.assertTrue('white' in self.mineral3.color)
