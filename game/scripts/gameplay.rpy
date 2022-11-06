# To Reset level, hide previous image and assign user to apropriate level

label game_manager:

    # To not hide images that is already hidden

    if is_from != "Start_menu":
        hide screen hp_bars
        hide hero stand 
        hide enemy_1 stand
        if level == 2:
            hide enemy_2_1 stand
            hide enemy_2_2 stand
        elif level == 3:
            hide enemy_3_1 stand
            hide enemy_3_2 stand
            hide enemy_3_3 stand

        # To go back to the main_menu

        if is_from == "Back to Main Menu":
            
            # For background
            scene intro_bg

            jump start_menu

    # Reset the player and target hp before going to the
    # next level or same level again as try again
    
    $ hero.hp = hero.max_hp
    $ target_hp = 0
    $ target = " "
    if level == 1:
        jump level_1 
    elif level == 2:
        jump level_2
    elif level == 3:
        jump level_3