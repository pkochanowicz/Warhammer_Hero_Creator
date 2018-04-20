from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import os

RACES = (
    ("human", "human"),
    ("dwarf", "dwarf"),
    ("elf", "elf"),
    ("halfling", "halfling"),
)

GENDERS = (
    ("male", "male"),
    ("female", "female"),
)


def get_image_path(instance, filename):
    return os.path.join('../media/portraits', str(instance.id), filename)


class Hero(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    race = models.CharField(max_length=16, choices=RACES, default="human")
    current_career = models.CharField(max_length=32, null=True, blank=True)
    previous_careers = models.CharField(max_length=32, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=16, default="male")
    # unimportant
    eye_color = models.CharField(max_length=16, null=True, blank=True)
    hair_color = models.CharField(max_length=16, null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    star_sign = models.CharField(max_length=32, null=True, blank=True)
    number_of_siblings = models.SmallIntegerField(null=True, blank=True)
    birthplace = models.CharField(max_length=32, null=True, blank=True)
    distinguishing_marks = models.CharField(max_length=32, null=True, blank=True)
    # stats
    weapon_skill = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    ballistic_skill = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    strength = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    toughness = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    agility = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    intelligence = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    will_power = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    fellowship = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    attacks = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    wounds = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=5)
    strength_bonus = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    toughness_bonus = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    movement = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    magic = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    insanity_points = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    fate_points = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    # functionalities
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    portrait = models.SmallIntegerField([MinValueValidator(1), MaxValueValidator(8)], blank=True, null=True)

