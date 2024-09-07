from django.db import models


STATE_CHOICE = ((
    ('india','india'),
    ('dehli','dehli'),
    ('chomu','chomu'),
    ('sikar','sikar')
))
class Profile(models.Model):
    name = models.CharField(max_length=121)
    email = models.EmailField(unique=True)
    dob = models.DateField(auto_now=False , auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE,max_length=121)
    gender = models.CharField(max_length=121)
    location = models.CharField(max_length=121)
    pro_image =models.ImageField(upload_to='pro_image',blank=True)
    pro_doc =models.FileField(upload_to='pro_file',blank=True)

