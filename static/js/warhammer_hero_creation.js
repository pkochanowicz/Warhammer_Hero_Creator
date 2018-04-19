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
    var character_profile_inputs = document.querySelectorAll('.character-profile-table > table > tbody > tr > td > input');
    var character_profile_roll_button = document.getElementById("character_profile_roll_button");
    var portrait_number_html = document.getElementById("portrait_number");
    //character profile skills
    var weapon_skill, ballistic_skill, strength, toughness, agility, intelligence, will_power, fellowship,
        attacks, wounds, strength_bonus, toughness_bonus, movement, magic, insanity_points, fate_points;

    //random numbers generators
    function diceRoll(number_of_dieces, type_of_dieces, bonus) {
        bonus = bonus || 0;
        var result = 0;
        for (var i = 0; i < number_of_dieces; i++) {
            result += ((Math.floor(Math.random() * type_of_dieces)) + 1);
        }
        return result + bonus;
    }

    function randomNumber(maximum_number) {
        return Math.floor((Math.random()) * maximum_number) + 1;
    }

    //portrait go left and rifght
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
    //race and gender selector change
    race_downroll.addEventListener("click", function (e) {
        selected_race = race_downroll.options[race_downroll.selectedIndex].text.toLowerCase();
        portrait.src = "/static/portraits/warhammer/" + selected_race + "/"
            + selected_gender + "/" + portrait_number + ".jpg";
        personal_details_inputs.forEach(function (element, index, array) {
            element.value = null;
            character_profile_inputs.forEach(function (element, index, array) {
                element.value = null;
            });
        });
    });
    gender_downroll.addEventListener("click", function (e) {
        selected_gender = gender_downroll.options[gender_downroll.selectedIndex].text.toLowerCase();
        portrait.src = "/static/portraits/warhammer/" + selected_race + "/"
            + selected_gender + "/" + portrait_number + ".jpg";
    });
    character_profile_roll_button.addEventListener("click", function (e) {
        character_profile_inputs.forEach(function (element, index, array) {
//human/basic specific calculations
            if (index >= 0 && index <= 7) {
                element.value = diceRoll(2, 10, 20);
            }
            if (index === 24) {
                element.value = 1;
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
            }
            if (index === 26) {
                element.value = ('' + array[2].value)[0];
            }
            if (index === 27) {
                element.value = ('' + array[3].value)[0];
            }
            if (index === 28) {
                element.value = 4;
            }
            if (index === 29 || index === 30) {
                element.value = 0;
                }
            if (index === 31) {
                roll = diceRoll(1, 10);
                console.log(roll);
                if (roll > 0 && roll < 5)
                    element.value = 2;
                else
                    element.value = 3;
                }
//dwarf specific calculations
            if (selected_race === 'dwarf') {
                if (index === 0) {
                    element.value = diceRoll(2, 10, 30);
                }
                if (index === 3) {
                    element.value = diceRoll(2, 10, 30);
                }
                if (index === 4) {
                    element.value = diceRoll(2, 10, 10);
                }
                if (index === 7) {
                    element.value = diceRoll(2, 10, 10);
                }
                if (index === 25) {
                    roll = diceRoll(1, 10);
                    console.log(roll);
                    if (roll > 0 && roll < 4)
                        element.value = 11;
                    else if (roll > 3 && roll < 7)
                        element.value = 12;
                    else if (roll > 6 && roll < 10)
                        element.value = 13;
                    else if (roll === 10)
                        element.value = 14;
                }
                if (index === 28) {
                    element.value = 3;
                }
                if (index === 31) {
                roll = diceRoll(1, 10);
                console.log(roll);
                if (roll > 0 && roll < 5)
                    element.value = 1;
                else if (roll > 4 && roll < 8)
                    element.value = 2;
                else if (roll > 7)
                    element.value = 3;
                }
            }
//elf specific calculations
            if (selected_race === 'elf') {
                if (index === 1) {
                    element.value = diceRoll(2, 10, 30);
                }
                if (index === 4) {
                    element.value = diceRoll(2, 10, 30);
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
                }
                if (index === 28) {
                    element.value = 5;
                }
                if (index === 31) {
                    roll = diceRoll(1, 10);
                    console.log(roll);
                    if (roll > 0 && roll < 5)
                        element.value = 1;
                    else if (roll > 4)
                        element.value = 2;
                }
            }
//halfling specific calculations
            if (selected_race === 'halfling') {
                if (index === 0) {
                    element.value = diceRoll(2, 10, 10);
                }
                if (index === 1) {
                    element.value = diceRoll(2, 10, 30);
                }
                if (index === 2) {
                    element.value = diceRoll(2, 10, 10);
                }
                if (index === 3) {
                    element.value = diceRoll(2, 10, 10);
                }
                if (index === 4) {
                    element.value = diceRoll(2, 10, 30);
                }
                if (index === 7) {
                    element.value = diceRoll(2, 10, 30);
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
                }
                if (index === 28) {
                    element.value = 4;
            }
               if (index === 31) {
                    roll = diceRoll(1, 10);
                    console.log(roll);
                    if (roll < 8)
                        element.value = 2;
                    else
                        element.value = 3;
                }
            }
         })
    });
});