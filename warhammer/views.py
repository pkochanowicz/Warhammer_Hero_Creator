import urllib.request

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from warhammer.forms import HeroCreationCharacterForm, HeroCreationPersonalDetailsForm, \
    HeroCreationCharacterProfileForm, UserLoginForm, AddUserForm, HeroSearchForm
from warhammer.models import Hero


class HeroCreationView(View):
    @method_decorator(login_required)
    def get(self, request):
        character_form = HeroCreationCharacterForm
        personal_details_form = HeroCreationPersonalDetailsForm
        character_profile_form = HeroCreationCharacterProfileForm
        race = 'human'
        gender = 'male'
        portrait = '1'
        return render(request, 'warhammer_hero_creation.html', {"character_form": character_form,
                                                                "personal_details_form": personal_details_form,
                                                                "character_profile_form": character_profile_form,
                                                                "race": race,
                                                                "gender": gender,
                                                                "portrait": portrait
                                                                })

    @method_decorator(login_required)
    def post(self, request):
        character_form = HeroCreationCharacterForm(request.POST)
        personal_details_form = HeroCreationPersonalDetailsForm(request.POST)
        character_profile_form = HeroCreationCharacterProfileForm(request.POST)
        if character_form.is_valid() & personal_details_form.is_valid() & character_profile_form.is_valid():
            # character form:
            name = character_form.cleaned_data['name']
            race = character_form.cleaned_data['race']
            gender = character_form.cleaned_data['gender']
            current_career = character_form.cleaned_data['current_career']
            # personal details form:
            previous_careers = personal_details_form.cleaned_data['previous_careers']
            age = personal_details_form.cleaned_data['age']
            eye_color = personal_details_form.cleaned_data['eye_color']
            hair_color = personal_details_form.cleaned_data['hair_color']
            weight = personal_details_form.cleaned_data['weight']
            height = personal_details_form.cleaned_data['height']
            star_sign = personal_details_form.cleaned_data['star_sign']
            number_of_siblings = personal_details_form.cleaned_data['number_of_siblings']
            birthplace = personal_details_form.cleaned_data['birthplace']
            distinguishing_marks = personal_details_form.cleaned_data['distinguishing_marks']
            # character profile form:
            weapon_skill = character_profile_form.cleaned_data['weapon_skill']
            ballistic_skill = character_profile_form.cleaned_data['ballistic_skill']
            strength = character_profile_form.cleaned_data['strength']
            toughness = character_profile_form.cleaned_data['toughness']
            agility = character_profile_form.cleaned_data['agility']
            intelligence = character_profile_form.cleaned_data['intelligence']
            will_power = character_profile_form.cleaned_data['will_power']
            fellowship = character_profile_form.cleaned_data['fellowship']
            attacks = character_profile_form.cleaned_data['attacks']
            wounds = character_profile_form.cleaned_data['wounds']
            strength_bonus = character_profile_form.cleaned_data['strength_bonus']
            toughness_bonus = character_profile_form.cleaned_data['toughness_bonus']
            movement = character_profile_form.cleaned_data['movement']
            magic = character_profile_form.cleaned_data['magic']
            insanity_points = character_profile_form.cleaned_data['insanity_points']
            fate_points = character_profile_form.cleaned_data['fate_points']
            user = request.user
            portrait = request.POST.get("portrait_number")
            new_hero = Hero.objects.create(
                name=name,
                race=race,
                gender=gender,
                current_career=current_career,
                previous_careers=previous_careers,
                age=age,
                eye_color=eye_color,
                hair_color=hair_color,
                weight=weight,
                height=height,
                star_sign=star_sign,
                number_of_siblings=number_of_siblings,
                birthplace=birthplace,
                distinguishing_marks=distinguishing_marks,
                weapon_skill=weapon_skill,
                ballistic_skill=ballistic_skill,
                strength=strength,
                toughness=toughness,
                agility=agility,
                intelligence=intelligence,
                will_power=will_power,
                fellowship=fellowship,
                attacks=attacks,
                wounds=wounds,
                strength_bonus=strength_bonus,
                toughness_bonus=toughness_bonus,
                movement=movement,
                magic=magic,
                insanity_points=insanity_points,
                fate_points=fate_points,
                user=user,
                portrait=portrait
            )
            new_hero.save()
            return redirect("/warhammer/hero/{}".format(new_hero.id))
        else:
            race = request.POST.get("race")
            gender = request.POST.get("gender")
            portrait = request.POST.get("portrait_number")
            return render(request, 'warhammer_hero_creation.html', {"character_form": character_form,
                                                                    "personal_details_form": personal_details_form,
                                                                    "character_profile_form": character_profile_form,
                                                                    "race": race,
                                                                    "gender": gender,
                                                                    "portrait": portrait})


class HeroView(View):
    @method_decorator(login_required)
    def get(self, request, hero_id):
        hero = Hero.objects.get(id=hero_id)
        return render(request, "warhammer_hero.html", {"hero": hero})


class HeroesSearchAndView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = HeroSearchForm
        user_heroes = Hero.objects.filter(user=request.user)
        return render(request, "warhammer_heroes.html", {"heroes":user_heroes,
                                                         "form": form})

    @method_decorator(login_required)
    def post(self, request):
        form = HeroSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            race = form.cleaned_data['race']
            gender = form.cleaned_data['gender']
            print(race, gender)
            current_career = form.cleaned_data['current_career']
            user_heroes = Hero.objects.filter(name__icontains=name, race__icontains=race,
                                              current_career__icontains=current_career, user=request.user)
            if gender != "":
                user_heroes = user_heroes.filter(gender=gender)
            return render(request, "warhammer_heroes.html", {'heroes': user_heroes,
                                                             "form": form})


class HeroDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, hero_id):
        hero = Hero.objects.get(id=hero_id)
        hero.delete()
        return redirect("/warhammer/heroes/")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'user_login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/warhammer/hero_creation/')
            else:
                return render(request, 'user_login.html', {'form': form,
                                                           'message': 'Wrong login or password'})


class UserLogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeated_password = form.cleaned_data['repeat_password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            if password != repeated_password:
                return render(request, 'add_user.html', {'form': form,
                                                         'message': 'Passwords don\'t match'})
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return render(request, 'add_user.html', {'form': form,
                                                         'message': 'User with that name or email already exists.'})
            User.objects.create_user(username=username, email=email, password=password,
                                     first_name=first_name, last_name=last_name)
            return render(request, 'add_user.html', {'form': form,
                                                     'message': 'User created'})
        else:
            return render(request, 'add_user.html', {'form': form,
                                                     'message': 'Form is invalid.'})


class MainSiteView(View):
    def get(self, request):
        return render(request, 'main_site.html', {})