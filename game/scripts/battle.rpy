
# For 1v1 fight

label gameplay_1v1:
    while hero.hp > 0:
        
        call dice_roll from _call_dice_roll

        # Hero turn
        # To call the skill option

        $ skill = renpy.call_screen("hero_skills")

        call hero_skill from _call_hero_skill
        
        # If player win
        # Jump to the game_manager for assigning of next level     

        if enemy_1.hp <= 0:
            stop music

            # Play sound lvlup

            play sound "../audio/lvlup_sound.ogg"

            scene bg fire_battle

            # To hide the life bars

            hide screen hp_bars_1v1

            show talk hero
            voice "../audio/hero/h21.wav"
            h "You win, good job your wise decision save a lot of people"
            hide talk
            show new_skill heal at truecenter
            voice "../audio/hero/h22.wav"
            h "Now we earned new skill. HEAL: it is use for additional life"
            hide new_skill heal

            $ level += 1

            jump game_manager
        
        # Enemy Turn

        call enemy_attack from _call_enemy_attack

    # If failed display the end_menu
    stop music
    hide hero stading with dissolve

    scene bg fire_battle

    # To hide the life bars

    hide screen hp_bars_1v1
    
    show talk enemy_1
    voice "../audio/e1/e1_3.wav"
    e1 "You are too weak..."
    hide talk

    jump end_menu

# For 1v2 fight

label gameplay_1v2:

        while hero.hp > 0:
            
            call dice_roll from _call_dice_roll_1
                
            $ skill = renpy.call_screen("hero_skills")
            
            # Choosing of target is not available when healing

            if target == "self":

                # Execute attack

                call hero_skill from _call_hero_skill_1

            else:
                # Choose which one to attack

                $ target = renpy.call_screen("choose_enemy_1v2")

                # Execute attack

                call hero_skill from _call_hero_skill_2

                # If player win jump to game_manager to assign to the next level           

                if enemy_2_1.hp <= 0 and enemy_2_2.hp <= 0:
                    stop music

                    # Play sound lvlup

                    play sound "../audio/lvlup_sound.ogg"

                    scene bg ice_battle

                    # To hide the life bars
    
                    hide screen hp_bars_1v2

                    show talk hero
                    voice "../audio/hero/h23.wav"
                    h "We win, good job with your dedication to save other people we restore ice world into its normal state"
                    hide talk
                    $ level += 1

                    jump game_manager

            # Reformat target

            $ target = " "
            
            # Enemy Turn
            # For deciding which one will attack

            $ enemies_turn = 0
            while enemies_turn <= 1:
                if enemies_turn == 0 and enemy_2_1.hp > 0:
                    $ enemy = "enemy_2_1"
                    call enemy_attack from _call_enemy_attack_1

                elif enemies_turn == 1 and enemy_2_2.hp > 0:
                    $ enemy = "enemy_2_2"
                    call enemy_attack from _call_enemy_attack_2
                $ enemies_turn += 1

        # If failed display the end_menu
        stop music
        hide hero stading with dissolve

        scene bg ice_battle

        # To hide the life bars

        hide screen hp_bars_1v2
        show talk enemy_2
        voice "../audio/e2/e2_4.wav"
        e2 "HAHAHA! I told you, you can't and will never defeat us!"
        hide talk
        jump end_menu

# For 1v3 fight

label gameplay_1v3:

        while hero.hp > 0:
            
            call dice_roll from _call_dice_roll_2
                
            $ skill = renpy.call_screen("hero_skills")
            
            # Choosing of target is not available when healing

            if target == "self":

                # Execute attack

                call hero_skill from _call_hero_skill_3
            
            else:

                # Choose which one to attack

                $ target = renpy.call_screen("choose_enemy_1v3")
                
                # Execute attack

                call hero_skill from _call_hero_skill_4

                # If player win jump to game_manager to assign to the next level           

                if enemy_3_1.hp <= 0 and enemy_3_2.hp <= 0 and enemy_3_3.hp <= 0 :
                    
                    stop music

                    # Play sound final level beated

                    play sound "../audio/final_win_sound.ogg"

                    scene bg forest_battle

                    # To hide the life bars

                    hide screen hp_bars_1v3

                    show talk hero
                    voice "../audio/hero/h24.wav"
                    h "Congratulations you save the world! The whole humanity is thanking you!"
     
                    # To go to start menu
                    # For background and music

                    scene bg intro
                    play music "../audio/intro_music.ogg"

                    $ level = 1

                    jump start_menu

            # Reformat target

            $ target = " "
            
            # Enemy Turn
            # For deciding which one will attack

            $ enemies_turn = 0
            while enemies_turn <= 2:
                if enemies_turn == 0 and enemy_3_1.hp > 0:
                    $ enemy = "enemy_3_1"
                    call enemy_attack from _call_enemy_attack_3

                elif enemies_turn == 1 and enemy_3_2.hp > 0:
                    $ enemy = "enemy_3_2"
                    call enemy_attack from _call_enemy_attack_4
                elif enemies_turn == 2 and enemy_3_3.hp > 0:
                    $ enemy = "enemy_3_3"
                    call enemy_attack from _call_enemy_attack_5
                $ enemies_turn += 1

        # If failed display the end_menu
        stop music
        hide hero stading with dissolve

        scene bg forest_battle

        # To hide the life bars

        hide screen hp_bars_1v3
        
        show talk enemy_3
        voice "../audio/e3/e3_3.wav"
        e3 "HAHAHA I thought that man can save humanity?"

        show talk hero
        voice "../audio/hero/h25.wav"
        h "Just wait he will fight you again..."

        hide talk

        jump end_menu   