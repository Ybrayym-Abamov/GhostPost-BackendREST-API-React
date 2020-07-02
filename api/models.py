from django.db import models
from django.utils import timezone

from api.utils import private_key


class BoastsRoasts(models.Model):
    boast_or_roast = models.CharField(max_length=5, choices=[
        ('Boast', 'Boast'), ('Roast', 'Roast')], default=None)
    body = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now)
    secret_id = models.CharField(
        max_length=10, default=private_key)

    def __str__(self):
        if self.boolean:
            return "Boast"
        return "Roast"

    # difference of upvotes and downvotes
    @property
    def score(self):
        return (self.upvotes - self.downvotes)
