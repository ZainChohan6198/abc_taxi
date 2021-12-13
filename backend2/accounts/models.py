from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone_num = models.CharField(max_length=120)
    email = models.EmailField(max_length=70, blank=True, null= True)
    message = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Display(models.Model):
    message = models.TextField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.message
