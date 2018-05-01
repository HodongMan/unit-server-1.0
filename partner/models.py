from django.db import models

class Partner(models.Model):

    division = models.CharField(max_length=200)
    grade = models.PositiveIntegerField()
    activity = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    establish_date = models.DateField()
    logo_url = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    homepage = models.CharField(max_length=200)

    class Meta:
        ordering = (
            '-id',
        )