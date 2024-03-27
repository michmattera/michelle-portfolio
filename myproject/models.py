from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email