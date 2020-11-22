from django.test import TestCase
from .models import Image,Profile
from datetime import datetime
from django.contrib.auth.models import User

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.test_user= User(username = "Felista", password = "ilovemyself")
        self.test_user.save()

        self.test_image = Image(image='images/test.jpg', posted_by=self.test_user, date_posted=datetime.now())

    def test_instance(self):
        self.assertTrue(isinstance(self.test_image,Image))

    def test_save(self):
        self.test_image.save()
        self.assertEqual(len(Image.objects.all()), 1)

    def tearDown(self):
        self.test_user.delete() 
        Image.objects.all().delete()   