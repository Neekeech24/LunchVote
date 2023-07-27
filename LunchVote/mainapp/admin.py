from django.contrib import admin
from .models import User, Restaurant, Vote, Slot


class VotesInline(admin.TabularInline):
    model = Vote


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["user", "max_votes"]
    inlines = [
        VotesInline,
    ]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    inlines = [
        VotesInline
    ]
