from django.test import TestCase
from .models import Image

class SigninTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='12test12')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
# TODO: Setup tests for image model class
class ImageModelTests(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     Image.objects.create(title="public",
    #                          description="A public cat",
    #                          public=True
    #     )
    #     Image.objects.create(title="public",
    #                          description="A public cat",
    #                          public=True
    #     )
    # def 


# # Create your tests here.
# class Image(models.Model):
#     title=models.CharField('Image Title', max_length=100)
#     description=models.CharField('Image Description', blank=True, max_length=500)
#     time_uploaded=models.DateTimeField('Upload Time', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     image=models.ImageField(upload_to='images/')
#     public=models.BooleanField('Public', default=False)
#     owner=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    

    