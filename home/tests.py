from django.test import TestCase

# Create your tests here.
class FlowerModelTest(TestCase):
    def setUp(self):
        from .models import Flower
        self.flower = Flower.objects.create(
            name="Rose",
            price=2.50,
            description="A beautiful red rose",
            remainig=100
        )

    def test_flower_creation(self):
        self.assertEqual(self.flower.name, len(self.flower.name) > 0)
        self.assertEqual(self.flower.price, int or float)
        self.assertEqual(self.flower.description, str)
        self.assertEqual(self.flower.remainig, self.flower.remainig >= 0)

    def test_flower_str_method(self):
        self.assertEqual(str(self.flower), "Rose")