from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, validate_email
from .models import Hero

# warhammer hero creation forms


class HeroCreationCharacterForm(forms.Form):
    name = forms.CharField(label='Hero name', max_length=32)
    race = forms.ChoiceField(choices=(("human", "Human"),
                                      ("dwarf", "Dwarf"),
                                      ("elf", "Elf"),
                                      ("halfling", "Halfling"),))
    gender = forms.ChoiceField(choices=(("male", "Male"),
                                        ("female", "Female"),))
    current_career = forms.CharField(label='Current career', max_length=32)


class HeroCreationPersonalDetailsForm(forms.Form):
    previous_careers = forms.CharField(label='Previous careers', max_length=32, required=False)
    age = forms.IntegerField(label="Age", validators=[MinValueValidator(14, message="14 is minimal")], required=False)
    eye_color = forms.CharField(label='Eye color', max_length=16, required=False)
    hair_color = forms.CharField(label='Hair color', max_length=16, required=False)
    weight = forms.IntegerField(label='Weight', required=False)
    height = forms.IntegerField(label='Height', required=False)
    star_sign = forms.CharField(label='Star sign', max_length=32, required=False)
    number_of_siblings = forms.IntegerField(label='Number of siblings', required=False)
    birthplace = forms.CharField(label='Birthplace', max_length=32, required=False)
    distinguishing_marks = forms.CharField(label="Distinguishing marks", max_length=32, required=False)


class HeroCreationCharacterProfileForm(forms.Form):
    weapon_skill = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    ballistic_skill = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    strength = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    toughness = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    agility = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    intelligence = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    will_power = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fellowship = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    attacks = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    wounds = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    strength_bonus = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    toughness_bonus = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    movement = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    magic = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    insanity_points = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fate_points = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], widget=forms.TextInput(attrs={'readonly':'readonly'}))


class HeroSearchForm(forms.Form):
    name = forms.CharField(label='Hero name', max_length=32, required=False)
    race = forms.ChoiceField(choices=(("", "Any"),
                                      ("human", "Human"),
                                      ("dwarf", "Dwarf"),
                                      ("elf", "Elf"),
                                      ("halfling", "Halfling")), required=False)
    gender = forms.ChoiceField(choices=(("", "Any"),
                                        ("male", "Male"),
                                        ("female", "Female"),), required=False)
    current_career = forms.CharField(label='Current career', max_length=32, required=False)

# user management forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class AddUserForm(forms.Form):
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First name', required=False)
    last_name = forms.CharField(label='Last name', required=False)
    email = forms.CharField(label='E-mail', validators=[validate_email])
