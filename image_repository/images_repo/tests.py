from django.test import TestCase
from .models import Image
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import ImageForm
from django.core.files.uploadedfile import SimpleUploadedFile




class ImageModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.pub_user = User.objects.create(username='test_pub', password='test123')
        cls.pub_img = Image.objects.create(title="public",
                             description="A public cat",
                             public=True)
        cls.priv_user = User.objects.create(username='test_priv', password='test123')
        cls.priv_img = Image.objects.create(title="public",
                             description="A public cat",
                             public=True)

class TestImageForm(TestCase):
    def test_empty_form(self):
        form = ImageForm()
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('public', form.fields)
        self.assertIn('image', form.fields)

class TestAddImage(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test', password='test123')
        cls.form_empty = ImageForm()
        cls.image = SimpleUploadedFile('file.jpeg', b'file_content', content_type='image/jpeg')
        cls.form_no_title_data = {'public': True, 'description': 'desc', 'title': 'title', 'image': cls.image}
        cls.form_no_desc_data = {'public': True, 'title': 'title', 'image': cls.image}
        cls.form_no_image_data = {'public': True, 'description': 'desc', 'title': 'title'}
        cls.form_no_public_data = {'public': '', 'description': 'desc', 'title': 'title', 'image': cls.image}
    
    def test_anonymous_user_load(self):
        response = self.client.get(reverse('add-image'), follow=True)
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8')
        self.assertInHTML('<h1>Please register or login to upload an image.</h1>', html)

    def test_user_logged_in_load(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add-image'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'images_repo/add_image.html')

    def test_user_logged_in_empty_title_submit(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('add-image'), data=self.form_no_title_data)
        self.assertTemplateUsed(response, 'images_repo/add_image.html')
        self.assertFalse(response.context['form'].is_valid())

    def test_user_logged_in_empty_public_submit(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('add-image'), data=self.form_no_public_data)
        self.assertTemplateUsed(response, 'images_repo/add_image.html')
        self.assertFalse(response.context['form'].is_valid())

    def test_user_logged_in_empty_image_submit(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('add-image'), data=self.form_no_image_data)
        self.assertTemplateUsed(response, 'images_repo/add_image.html')
        self.assertFalse(response.context['form'].is_valid())

    