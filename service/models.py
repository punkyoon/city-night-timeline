from django.db import models

# Create your models here.
class Timeline(models.Model):
    _id = models.AutoField(primary_key=True)
    message = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self._id)
