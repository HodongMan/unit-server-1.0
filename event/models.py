from django.db import models

class Event(models.Model):

    host = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    register_start = models.DateTimeField()
    register_end = models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    cost  = models.PositiveIntegerField()
    keyword = models.CharField(max_length=200)
    homepage = models.CharField(max_length=200)

    class Meta:
        ordering = (
            '-id',
        )
