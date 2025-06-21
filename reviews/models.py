from django.db import models # type: ignore

# Create your models here.
from django.db import models # type: ignore

class Review(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    review = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
