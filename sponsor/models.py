from django.db import models

class Sponsor(models.Model):

    division = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    support_date = models.DateField()
    support_amount = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    establish_date = models.DateField()
    logo_url = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    keyword = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    homepage = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = (
            '-id',
        )