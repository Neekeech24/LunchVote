import datetime

from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    """
    Model connecting votes with user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_votes = models.IntegerField(
        verbose_name="Max votes", help_text="Number of daily votes"
    )

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    name = models.CharField(max_length=128, help_text="Name of a restaurant")

    def __str__(self):
        return self.name


class Slot(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="slots"
    )
    date = models.DateField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)


class Vote(models.Model):
    """
    Model to connect User with voted Restaurant with certain weight
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="votes"
    )
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="slots", blank=True)
    weight = models.FloatField(blank=True)

    def __str__(self):
        return f"{self.user} - {self.restaurant} - {self.weight}"

    def save(self, *args, **kwargs):
        user_votes = Vote.objects.filter(user=self.user)
        if user_votes.count() >= self.user.max_votes:
            raise Exception(f"Vote limit of {self.user.max_votes} has been reached")

        self.weight = 1
        rest_votes = user_votes.filter(restaurant=self.restaurant)
        if rest_votes:
            for i in rest_votes:
                self.weight = self.weight / 2
                if self.weight <= 0.25:
                    self.weight = 0.25
                    break

        self.slot, created = Slot.objects.get_or_create(
            restaurant=self.restaurant,
            date=datetime.datetime.today(),
        )
        super().save(*args, **kwargs)
        return self
