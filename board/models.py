from django.db import models

class Board(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    views = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-id',)