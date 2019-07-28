from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.FilePathField(path='/img')
    image_caption = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    formula = models.TextField(null=True, blank=True)
    strunz_classification = models.TextField(null=True, blank=True)
    crystal_system = models.TextField(null=True, blank=True)
    unit_cell = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    crystal_symmetry = models.TextField(null=True, blank=True)
    cleavage = models.TextField(null=True, blank=True)
    mohs_scale_hardness = models.TextField(null=True, blank=True)
    luster = models.TextField(null=True, blank=True)
    streak = models.TextField(null=True, blank=True)
    diaphaneity = models.TextField(null=True, blank=True)
    optical_properties = models.TextField(null=True, blank=True)
    refractive_index = models.TextField(null=True, blank=True)
    crystal_habit = models.TextField(null=True, blank=True)
    specific_gravity = models.TextField(null=True, blank=True)
    group = models.TextField(null=True, blank=True)
