from django.db import models


TYPE_CHOICES = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Miss.', 'Miss.'),
    ('Ms.', 'Ms.'),
)


class Profiles(models.Model):
    Prefix = models.CharField(max_length=60, choices=TYPE_CHOICES)
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True)
    Email = models.CharField(max_length=60, default="", blank=True)
    Username = models.CharField(max_length=60, default="")

    objects = models.Manager()

    def __str__(self):
        return self.First_Name