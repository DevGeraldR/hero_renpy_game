
# For 1v1 fight

label gameplay_1v1:
    while hero.hp > 0:
        
        call dice_roll

        # Hero turn
        # To call the skill option

        $ skill = renpy.call_screen("hero_skills")

        call hero_skill
        
        # If player win
        # Jump to the game_manager for assigning of next level     

        if enemy_1.hp <= 0:
            stop music

            # Play sound lvlup

            play sound "../audio/lvlup_sound.ogg"

            "You win the combat encounter"
            show new_skill heal at truecenter
            "New skill unlock: HEAL, Click to go to next level"
            hide new_skill heal

            $ level += 1

            # To hide the life bars

            hide screen hp_bars_1v1

            jump game_manager
        
        # Enemy Turn

        call enemy_attack

    # If failed display the end_menu
    stop music
    hide hero stading with dissolve
    "You died..."


    # To hide the life bars

    hide screen hp_bars_1v1

    jump end_menu

# For 1v2 fight

label gameplay_1v2:

        while hero.hp > 0:
            
            call dice_roll
                
            $ skill = renpy.call_screen("hero_skills")
            
            # Choosing of target is not available when healing

            if target == "self":

                # Execute attack

                call hero_skill

            else:
                # Choose which one to attack

                $ target = renpy.call_screen("choose_enemy_1v2")

                # Execute attack

                call hero_skill

                # If player win jump to game_manager to assign to the next level           

                if enemy_2_1.hp <= 0 and enemy_2_2.hp <= 0:
                    stop music

                    # Play sound lvlup

                    play sound "../audio/lvlup_sound.ogg"

                    "You win the combat encounter! Click to go to next level"
                    $ level += 1

                    # To hide the life bars

                    hide  screen hp_bars_1v2

                    jump game_manager

            # Reformat target

            $ target = " "
            
            # Enemy Turn
            # For deciding which one will attack

            $ enemies_turn = 0
            while enemies_turn <= 1:
                if enemies_turn == 0 and enemy_2_1.hp > 0:
                    $ enemy = "enemy_2_1"
                    call enemy_attack

                elif enemies_turn == 1 and enemy_2_2.hp > 0:
                    $ enemy = "enemy_2_2"
                    call enemy_attack
                $ enemies_turn += 1

        # If failed display the end_menu
        stop music
        hide hero stading with dissolve

        "You died..."

        # To hide the life bars

        hide screen hp_bars_1v2

        jump end_menu

# For 1v3 fight

label gameplay_1v3:

        while hero.hp > 0:
            
            call dice_roll
                
            $ skill = renpy.call_screen("hero_skills")
            
            # Choosing of target is not available when healing

            if target == "self":

                # Execute attack

                call hero_skill
            
            else:

                # Choose which one to attack

                $ target = renpy.call_screen("choose_enemy_1v3")
                
                # Execute attack

                call hero_skill

                # If player win jump to game_manager to assign to the next level           

                if enemy_3_1.hp <= 0 and enemy_3_2.hp <= 0 and enemy_3_3.hp <= 0 :
                    
                    stop music

                    # Play sound final level beated

                    play sound "../audio/final_win_sound.ogg"

                    "Congratulations you beat the game!"

                    # To go to start menu
                    # For background and music

                    scene bg intro
                    play music "../audio/intro_music.ogg"

                    $ level = 1

                    # To hide the life bars

                    hide screen hp_bars_1v3

                    jump start_menu

            # Reformat target

            $ target = " "
            
            # Enemy Turn
            # For deciding which one will attack

            $ enemies_turn = 0
            while enemies_turn <= 2:
                if enemies_turn == 0 and enemy_3_1.hp > 0:
                    $ enemy = "enemy_3_1"
                    call enemy_attack

                elif enemies_turn == 1 and enemy_3_2.hp > 0:
                    $ enemy = "enemy_3_2"
                    call enemy_attack
                elif enemies_turn == 2 and enemy_3_3.hp > 0:
                    $ enemy = "enemy_3_3"
                    call enemy_attack
                $ enemies_turn += 1

        # If failed display the end_menu
        stop music
        hide hero stading with dissolve
        "You died..."

        # To hide the life bars

        hide screen hp_bars_1v3

        jump end_menu   