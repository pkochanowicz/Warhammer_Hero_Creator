document.addEventListener('DOMContentLoaded', function () {
    var portrait_number = 1;
    var portrait = document.getElementById("id_portrait");
    var portrait_left_button = document.getElementById("portrait_left_button");
    var portrait_right_button = document.getElementById("portrait_right_button");
    var race_downroll = document.getElementById("id_race");
    var selected_race = "human";
    var gender_downroll = document.getElementById("id_gender");
    var selected_gender = "male";
    var personal_details_inputs = document.querySelectorAll('.character-personal-details > table > tbody > tr > td > input');
    var personal_details_roll_button = document.querySelectorAll("personal_details_roll_button");
    var character_profile_inputs = document.querySelectorAll('.character-profile-table > table > tbody > tr > td > input');
    var character_profile_roll_button = document.getElementById("character_profile_roll_button");
    var portrait_number_html = document.getElementById("portrait_number");
    var shallyas_mercy_select = document.getElementById("shallyas_mercy_select");
    var shallyas_mercy_button = document.getElementById("shallyas_mercy_button");
    var career_row = document.querySelector('.character > table > tbody');
    var carrer_options = career_row.lastElementChild.querySelectorAll('td > select > option');
    var weapon_skill, ballistic_skill, strength, tougness, agility, intelligence, will_power, fellowship,
        attacks, wounds, strength_bonus, toughness_bonus, movement, magic, insanity_points, fate_points;
    var skill_list = [weapon_skill, ballistic_skill, strength, tougness, agility, intelligence, will_power,
        fellowship, attacks, wounds, strength_bonus, toughness_bonus, movement, magic, insanity_points, fate_points];
    var skill_name_list = ["Weapon skill", "Ballistic skill", "Strength", "Tougness", "Agility", "Intelligence"
        , "Will power", "Fellowship", "Attacks", "Wounds", "Strength bonus", "Toughness bonus", "Movement",
        "Magic", "Insanity points", "Fate points"];
    var human_entry_careers = ["agitator", "apprentice_wizard", "bailiff", "barber_surgeon", "boatman", "bodyguard",
        "bone_picker", "bounty_hunter", "burgher", "camp_follower", "charcoal_burner", "coachman", "entertainer",
        "estalian_diestro", "ferryman", "fisherman", "grave_robber", "hedge_wizard", "hunter", "initiate", "jailer",
        "kislevite_kossar", "marine", "mercenary", "messenger", "militiaman", "miner", "noble", "norse_berserker",
        "outlaw", "outrider", "peasant", "pit_fighter", "protagonist", "rat_catcher", "roadwarden", "rogue", "scribe",
        "seaman", "servant", "smuggler", "soldier", "squire", "student", "thief", "thug", "toll_keeper", "tomb_robber",
        "tradesman", "vagabond", "valet", "watchman", "woodsman", "zealot"];
    var dwarf_entry_careers = ["agitator", "bodyguard", "burgher", "coachman", "entertainer", "hunter", "jailer",
        "marine", "mercenary", "miner", "noble", "outlaw", "pit_fighter", "protagonist", "rat_catcher", "runebearer",
        "scribe", "seaman", "servant", "shieldbreaker", "smuggler", "soldier", "student", "thief", "toll_keeper",
        "tomb_robber", "tradesman", "troll_slayer", "watchman"];
    var elf_entry_careers = ["apprentice_wizard", "entertainer", "envoy", "hunter", "kithband_warrior", "mercenary",
        "messenger", "outlaw", "outrider", "rogue", "scribe", "seaman", "student", "thief", "tradesman", "vagabond"];
    var halfing_entry_careers = ["agitator", "barber_surgeon","bone_picker", "bounty_hunter", "burgher",
        "camp_follower", "charcoal_burner","entertainer", "field_warden", "fisherman", "grave_robber", "hunter",
        "mercenary", "messenger", "militiaman", "outlaw","peasant", "rat_catcher", "rogue", "servant", "smuggler",
        "soldier", "student", "thief", "toll_keeper", "tomb_robber", "tradesman", "vagabond", "valet", "watchman"];


    CheckIfCareerIsAvailable();
//dices:
    function diceRoll(number_of_dices, type_of_dices) {
        var result = 0;
        for (var i = 0; i < number_of_dices; i++) {
            result += ((Math.floor(Math.random() * type_of_dices)) + 1);
        }
        return result;
    }

    function randomNumber(maximum_number) {
        return Math.floor((Math.random()) * maximum_number) + 1;
    }

    function isInArray(value, array) {
        return array.indexOf(value) > -1;
    }

    function PrimarySkill(base, roll, skill_name, input_name) {
        this.base = base;
        this.roll = roll;
        this.skill_name = skill_name;
        this.input_name = input_name;
        input_name.value = base + roll;
        if (roll < 11)
            shallyasMercyAddOption(skill_name);
    }
    function SecondarySkill(result, skill_name, input_name) {
        this.result = result;
        this.skill_name = skill_name;
        this.input_name = input_name;
        input_name.value = result;
    }
    //race and gender selector change
    race_downroll.addEventListener("change", function (e) {
        shallyasMercyRemoveOptions();
        selected_race = race_downroll.options[race_downroll.selectedIndex].text.toLowerCase();
        portrait.src = "/static/portraits/warhammer/" + selected_race + "/"
            + selected_gender + "/" + portrait_number + ".jpg";
        personal_details_inputs.forEach(function (element, index, array) {
            element.value = null;
        character_profile_inputs.forEach(function (element, index, array) {
                element.value = null;
            });
        CheckIfCareerIsAvailable();
        });
    });

    gender_downroll.addEventListener("change", function (e) {
        selected_gender = gender_downroll.options[gender_downroll.selectedIndex].text.toLowerCase();
        portrait.src = "/static/portraits/warhammer/" + selected_race + "/"
            + selected_gender + "/" + portrait_number + ".jpg";
    });

    //career fits the race:
    function CheckIfCareerIsAvailable(){
        carrer_options.forEach(function (element, index, array) {
           element.disabled = false;
            });
        if (selected_race === "human"){
            carrer_options.forEach(function (element, index, array) {
                if (isInArray(element.value, human_entry_careers) === false) {
                    element.disabled = "disabled";
                }
            });
        }
        if (selected_race === "dwarf"){
            carrer_options.forEach(function (element, index, array) {
                if (isInArray(element.value, dwarf_entry_careers) === false) {
                    element.disabled = "disabled";
                }
            });
        }
        if (selected_race === "elf"){
            carrer_options.forEach(function (element, index, array) {
                if (isInArray(element.value, elf_entry_careers) === false) {
                    element.disabled = "disabled";
                }
            });
        }
        if (selected_race === "halfling"){
            carrer_options.forEach(function (element, index, array) {
                if (isInArray(element.value, halfing_entry_careers) === false) {
                    element.disabled = "disabled";
                }
            });
        }
        carrer_options[26].selected = "selected";
    }

    character_profile_roll_button.addEventListener("click", function (e) {
        shallyasMercyRemoveOptions();
        shallyas_mercy_select.style.visibility = "visible";
        shallyas_mercy_button.style.visibility = "visible";
        character_profile_inputs.forEach(function (element, index, array) {
            //human profile rolls
            if (selected_race === "human"){
                //main skills
                if (index >= 0 && index <= 7) {
                    skill_list[index] = new PrimarySkill(20, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 25) {
                    var roll = diceRoll(1, 10);
                    if (roll > 0 && roll < 4)
                        element.value = 10;
                    else if (roll > 3 && roll < 7)
                        element.value = 11;
                    else if (roll > 6 && roll < 10)
                        element.value = 12;
                    else if (roll === 10)
                        element.value = 13;
                    skill_list[9] = new SecondarySkill(element.value, skill_name_list[9], element);
                }
                if (index === 28) {
                    skill_list[12] = new SecondarySkill(4, skill_name_list[12], element);
                }
                if (index === 31) {
                    roll = diceRoll(1, 10);
                    if (roll > 0 && roll < 5)
                        element.value = 2;
                    else
                        element.value = 3;
                    skill_list[15] = new SecondarySkill(element.value, skill_name_list[15], element);
                    }
                }
            // dwarf profile rolls
            if (selected_race === "dwarf") {
                if (index === 1 || index === 2 || index === 5 || index === 6) {
                skill_list[index] = new PrimarySkill(20, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 0 || index === 3) {
                skill_list[index] = new PrimarySkill(30, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 4 || index === 7) {
                skill_list[index] = new PrimarySkill(10, diceRoll(2, 10), skill_name_list[index], element);
                }
                //dwarf secondary skills
                if (index === 25) {
                    roll = diceRoll(1, 10);
                    if (roll > 0 && roll < 4)
                        element.value = 11;
                    else if (roll > 3 && roll < 7)
                        element.value = 12;
                    else if (roll > 6 && roll < 10)
                        element.value = 13;
                    else if (roll === 10)
                        element.value = 14;
                    skill_list[9] = new SecondarySkill(element.value, skill_name_list[9], element);
                }
                if (index === 28) {
                    skill_list[12] = new SecondarySkill(3, skill_name_list[12], element);
                }
                if (index === 31) {
                roll = diceRoll(1, 10);
                if (roll > 0 && roll < 5)
                    element.value = 1;
                else if (roll > 4 && roll < 8)
                    element.value = 2;
                else if (roll > 7)
                    element.value = 3;
                skill_list[15] = new SecondarySkill(element.value, skill_name_list[15], element);
                }
            }
            //elf profile rolls
            if (selected_race === "elf") {
                if (index === 0 || index === 2 || index === 3 || index === 5 || index === 6 || index === 7) {
                    skill_list[index] = new PrimarySkill(20, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 1 || index === 4) {
                    skill_list[index] = new PrimarySkill(30, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 25) {
                    roll = diceRoll(1, 10);
                    if (roll > 0 && roll < 4)
                        element.value = 9;
                    else if (roll > 3 && roll < 7)
                        element.value = 10;
                    else if (roll > 6 && roll < 10)
                        element.value = 11;
                    else if (roll === 10)
                        element.value = 12;
                    skill_list[9] = new SecondarySkill(element.value, skill_name_list[9], element);
                }
                if (index === 28) {
                    skill_list[12] = new SecondarySkill(5, skill_name_list[12], element);
                }
                if (index === 31) {
                    roll = diceRoll(1, 10);
                    if (roll > 0 && roll < 5)
                        element.value = 1;
                    else if (roll > 4)
                        element.value = 2;
                    skill_list[15] = new SecondarySkill(element.value, skill_name_list[15], element);
                }
            }
            // halfling profile rolls
            if (selected_race === "halfling") {
                if (index === 0 || index === 2 || index === 3) {
                skill_list[index] = new PrimarySkill(10, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 1 || index === 4 || index === 7) {
                skill_list[index] = new PrimarySkill(30, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 5 || index === 6) {
                skill_list[index] = new PrimarySkill(20, diceRoll(2, 10), skill_name_list[index], element);
                }
                if (index === 25) {
                    roll = diceRoll(1, 10);
                    if (roll > 0 && roll < 4)
                        element.value = 8;
                    else if (roll > 3 && roll < 7)
                        element.value = 9;
                    else if (roll > 6 && roll < 10)
                        element.value = 10;
                    else if (roll === 10)
                        element.value = 11;
                    skill_list[9] = new SecondarySkill(element.value, skill_name_list[9], element);
                }
                if (index === 28) {
                    skill_list[12] = new SecondarySkill(3, skill_name_list[12], element);
                }
                if (index === 31) {
                    roll = diceRoll(1, 10);
                    if (roll < 8)
                        element.value = 2;
                    else
                        element.value = 3;
                    skill_list[15] = new SecondarySkill(element.value, skill_name_list[15], element);
                }
            }
            //common rolls
            if (index === 24) {
                    skill_list[8] = new SecondarySkill(1, skill_name_list[8], element);
            }
            if (index === 26) {
                    skill_list[10] = new SecondarySkill((skill_list[2].input_name.value)[0], skill_name_list[10], element);
            }
            if (index === 27) {
                    skill_list[11] = new SecondarySkill((skill_list[3].input_name.value)[0], skill_name_list[11], element);
            }
            if (index === 29) {
                    skill_list[13] = new SecondarySkill(0, skill_name_list[13], element);
            }
            if (index === 30) {
                    skill_list[14] = new SecondarySkill(0, skill_name_list[14], element);
            }
        });
    });

    function shallyasMercyAddOption(skill_name){
        var skill = document.createElement("option");
        skill.text = skill_name;
        shallyas_mercy_select.add(skill);
    }


    function shallyasMercyRemoveOptions() {
         shallyas_mercy_select.length = 0;
    }

    shallyas_mercy_button.addEventListener("click", function (e) {
        var skill_to_change = shallyas_mercy_select.options[shallyas_mercy_select.selectedIndex].text.toLowerCase();
        skill_list.forEach(function (element,	index,	array){
           if (element.skill_name.toLowerCase() === skill_to_change){
               element.roll = 11;
               element.input_name.value = element.roll + element.base;
           }
       shallyas_mercy_select.style.visibility = "hidden";
        shallyas_mercy_button.style.visibility = "hidden";
        });
    });

        //portrait go left and right
    portrait_left_button.addEventListener("click", function (e) {
        portrait_number -= 1;
        if (portrait_number < 1) {
            portrait_number = 8;
        }
        portrait.src = "/static/portraits/warhammer/" + selected_race +
            "/" + selected_gender + "/" + portrait_number + ".jpg";
        portrait_number_html.value = portrait_number;
    });

    portrait_right_button.addEventListener("click", function (e) {
        portrait_number += 1;
        if (portrait_number > 8) {
            portrait_number = 1;
        }
        portrait.src = "/static/portraits/warhammer/" + selected_race + "/"
            + selected_gender + "/" + portrait_number + ".jpg";
        portrait_number_html.value = portrait_number;
    });
});