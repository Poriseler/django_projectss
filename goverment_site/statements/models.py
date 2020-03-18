from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Statement(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("statements:detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
