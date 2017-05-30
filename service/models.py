from django.db import models

# Create your models here.
class Timeline(models.Model):
    _id = models.AutoField(primary_key=True)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return str(self._id)
