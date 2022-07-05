from django.test import TestCase
from start_page.forms import Add_medcine
from start_page.models import Medcine


class MecineFormTest(TestCase):
    def test_form_render_text_input(self):
        form = Add_medcine()
        self.assertIn('<span class="helptext">Ввод латиницей с большой буквы</span>', form.as_p())
        self.assertIn('name="international_name"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = Add_medcine(data={'international_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['international_name'], ['Поле обязательно для заполнения'])

    def test_form_validations_for_dublicate_medcines(self):
        Medcine.objects.create(international_name='Opp')
        form = Add_medcine(data={'international_name': "Opp"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['international_name'], ['Препарат с таким МНН уже существует.'])