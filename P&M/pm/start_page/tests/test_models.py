from django.test import TestCase
from start_page.models import Medcine, Synonyms
from django.core.exceptions import ValidationError


class SynAndMedModelsTest(TestCase):
    def test_cannot_save_empty_med(self):
        med = Medcine(international_name="")
        with self.assertRaises(ValidationError):
            med.save()
            med.full_clean()

    def test_get_absolute_url(self):
        med = Medcine.objects.create()
        syn = Synonyms.objects.create(url_name='name', medcine=med)
        self.assertEqual(syn.get_absolute_url(), f'/search/{syn.url_name}')

    def test_duplicate_medcines_are_invalid(self):
        Medcine.objects.create(international_name="bla")
        with self.assertRaises(ValidationError):
            med = Medcine(international_name="bla")
            med.full_clean()
            med.save()



