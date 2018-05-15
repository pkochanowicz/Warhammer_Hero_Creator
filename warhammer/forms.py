from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, validate_email
from .models import Hero

# warhammer hero creation forms


def	validate_age(value):
    if value < 16 or value > 125:
        raise ValidationError("Wrong age")


def	validate_weight(value):
    if value < 30 or value > 120:
        raise ValidationError("Wrong weight")


def	validate_height(value):
    if value < 80 or value > 190:
        raise ValidationError("Wrong height")


def	validate_positive(value):
    if value < 0:
        raise ValidationError("Must be a positive number")


class HeroCreationCharacterForm(forms.Form):
    name = forms.CharField(label='Hero name', max_length=32)
    race = forms.ChoiceField(choices=(("human", "Human"),
                                      ("dwarf", "Dwarf"),
                                      ("elf", "Elf"),
                                      ("halfling", "Halfling"),))
    gender = forms.ChoiceField(choices=(("male", "Male"),
                                        ("female", "Female"),))
    current_career = forms.ChoiceField(choices=(
        ("agitator", "Agitator"), ("apprentice_wizard", "Apprentice Wizard"), ("bailiff", "Bailiff"),
        ("barber-surgeon", "Barber-Surgeon"), ("boatman", "Boatman"), ("bodyguard", "Bodyguard"),
        ("bone_picker", "Bone Picker"), ("bounty_hunter", "Bounty Hunter"), ("burgher", "Burgher"),
        ("camp_follower", "Camp Follower"), ("charcoal-burner", "Charcoal-Burner"),  ("coachman", "Coachman"),
        ("entertainer", "Entertainer"),  ("envoy", "Envoy"),  ("estalian_diestro", "Estalian Diestro"),
        ("ferryman", "Ferryman"), ("fieldwarden", "Fieldwarden"),  ("fisherman", "Fisherman"),
        ("grave_robber", "Grave Robber"),  ("hedge_wizard", "Hedge Wizard"),  ("hunter", "Hunter"),
        ("initiate", "Initiate"), ("jailer", "Jailer"),  ("kislevite_kossar", "Kislevite Kossar"),
        ("kithband_warrior", "Kithband Warrior"),  ("marine", "Marine"),  ("mercenary", "Mercenary"),
        ("messenger", "Messenger"),  ("militiaman", "Militiaman"),  ("miner", "Miner"),  ("noble", "Noble"),
        ("norse_berserker", "Norse Berserker"),  ("outlaw", "Outlaw"),  ("outrider", "Outrider"),
        ("peasant", "Peasant"),  ("pit_fighter", "Pit Fighter"),  ("protagonist", "Protagonist"),
        ("rat_catcher", "Rat Catcher"),  ("roadwarden", "Roadwarden"),  ("rogue", "Rogue"),
        ("runebearer", "Runebearer"),  ("scribe", "Scribe"),  ("seaman", "Seaman"),  ("servant", "Servant"),
        ("shieldbreaker", "Shieldbreaker"),  ("smuggler", "Smuggler"),  ("soldier", "Soldier"),
        ("squire", "Squire"),  ("student", "Student"),  ("thief", "Thief"),  ("thug", "Thug"),
        ("toll_keeper", "Toll Keeper"),  ("tomb_robber", "Tomb Robber"),  ("tradesman", "Tradesman"),
        ("troll_slayer", "Troll Slayer"),  ("vagabond", "Vagabond"),  ("valet", "Valet"),
        ("watchman", "Watchman"),  ("woodsman", "Woodsman"),  ("zealot", "Zealot"),
    ))


class HeroCreationPersonalDetailsForm(forms.Form):
    previous_careers = forms.CharField(label='Previous careers', max_length=32, required=False)
    age = forms.IntegerField(label="Age", validators=[validate_age], required=False)
    eye_color = forms.CharField(label='Eye color', max_length=16, required=False)
    hair_color = forms.CharField(label='Hair color', max_length=16, required=False)
    weight = forms.IntegerField(label='Weight', validators=[validate_weight], required=False)
    height = forms.IntegerField(label='Height', validators=[validate_height], required=False)
    star_sign = forms.CharField(label='Star sign', max_length=32, required=False)
    number_of_siblings = forms.IntegerField(label='Number of siblings', validators=[validate_positive], required=False)
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
