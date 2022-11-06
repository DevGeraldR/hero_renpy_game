# For level 1 battle

label level_1:

    # For background
    scene fire_battle_bg

    # Create the enemy

    $ enemy_1 = character("enemy_1", 12, 12)
    $ enemy_1.hp = enemy_1.max_hp
    $ enemy = "enemy_1"

    # Show level intro and life bars

    call show_level
    show screen hp_bars
    
    # Show characters

    show hero stand:
        xalign 0.2
        yalign 0.7
    show enemy_1 stand:
        xalign 0.8
        yalign 0.7

    # For gameplay

    while hero.hp > 0:
        call dice_roll
        menu:
            "Punch":
                $ skill = "Punch"
                call hero_skill
            "Super Duper Punch":
                $ skill = "Super Duper Punch"
                call hero_skill

        # If player win
        # Jump to the game_manager for assigning of next level     

        if enemy_1.hp <= 0:
            "You win the combat encounter!"
            $ level += 1
            $ is_from = "Level"
            jump game_manager
        
        # Enemy Turn

        call enemy_attack

    # If failed display the end_menu
    hide hero stading with dissolve
    "You died..."
    jump end_menu

# For level 2 battle

label level_2:

    # For background
    scene ice_battle_bg

    # Create enemy's

    $ enemy_2_1 = character("Enemy_2_1", 12, 12)
    $ enemy_2_2 = character("Enemy_2_2", 12, 12)
    $ enemy_2_1.hp = enemy_2_1.max_hp
    $ enemy_2_2.hp = enemy_2_2.max_hp

    # Show level intro and life bars

    call show_level
    show screen hp_bars

    # Show characters

    show hero stand:
        xalign 0.2
        yalign 0.7
    show enemy_2_1 stand:
        xalign 0.8
        yalign 0.6
    show enemy_2_2 stand:
        xalign 0.8
        yalign 0.9

    # For gameplay

    while hero.hp > 0:
        
        call dice_roll
            
        menu:
            "Punch":
                $ skill = "Punch"
            "Super Duper Punch":
                $ skill = "Super Duper Punch"
            "Heal":
                $ skill = "Heal"
                $ target = "self"
                call hero_skill
        
        # Choosing of target is not available when healing

        if target != "self":

            # Choose which one to attack

            menu:
                "Attack Enemy 1" if enemy_2_1.alive:
                    $ target = "enemy_2_1"
                    call hero_skill
                "Attack Enemy 2" if enemy_2_2.alive: 
                    $ target = "enemy_2_2"
                    call hero_skill

            # If player win jump to game_manager to assign to the next level           

            if enemy_2_1.hp <= 0 and enemy_2_2.hp <= 0:
                "You win the combat encounter!"
                $ level += 1
                $ is_from = "Level"
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
    hide hero stading with dissolve
    "You died..."
    jump end_menu
    
# For level 3 battle

label level_3:

    # For background
    scene forest_battle_bg

    # Create enemy's

    $ enemy_3_1 = character("Enemy_3_1", 12, 12)
    $ enemy_3_2 = character("Enemy_3_2", 12, 12)
    $ enemy_3_3 = character("Enemy_3_3", 12, 12)
    $ enemy_3_1.hp = enemy_3_1.max_hp
    $ enemy_3_2.hp = enemy_3_2.max_hp
    $ enemy_3_3.hp = enemy_3_3.max_hp


    # Show level intro and life bars

    call show_level
    show screen hp_bars

    # Show characters

    show hero stand:
        xalign 0.2
        yalign 0.7
    show enemy_3_1 stand:
        xalign 0.8
        yalign 0.6
    show enemy_3_2 stand:
        xalign 0.8
        yalign 0.9
    show enemy_3_3 stand:
        xalign 0.9
        yalign 0.75

    # For gameplay

    while hero.hp > 0:
        
        call dice_roll
            
        menu:
            "Punch":
                $ skill = "Punch"
            "Super Duper Punch":
                $ skill = "Super Duper Punch"
            "Heal":
                $ skill = "Heal"
                $ target = "self"
                call hero_skill
        
        # Choosing of target is not available when healing

        if target != "self":

            # Choose which one to attack

            menu:
                "Attack Enemy 1" if enemy_3_1.alive:
                    $ target = "enemy_3_1"
                    call hero_skill
                "Attack Enemy 2" if enemy_3_2.alive: 
                    $ target = "enemy_3_2"
                    call hero_skill
                "Attack Enemy 3" if enemy_3_3.alive: 
                    $ target = "enemy_3_3"
                    call hero_skill

            # If player win jump to game_manager to assign to the next level           

            if enemy_3_1.hp <= 0 and enemy_3_2.hp <= 0 and enemy_3_3.hp <= 0 :
                "You beat the game!"
                "Congratulations"
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
                call enemy_attack

            elif enemies_turn == 1 and enemy_3_2.hp > 0:
                $ enemy = "enemy_3_2"
                call enemy_attack
            elif enemies_turn == 2 and enemy_3_3.hp > 0:
                $ enemy = "enemy_3_3"
                call enemy_attack
            $ enemies_turn += 1

    # If failed display the end_menu
    hide hero stading with dissolve
    "You died..."
    jump end_menu   

# Show the level

label show_level:
    show text "Level [level]" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    return

# Random Number Generator
# For critical hit and other action that happens unintentional

label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

#For life bars

screen hp_bars:
    frame:
        xpadding 10
        ypadding 10
        xalign 0.1
        yalign 0.05
        xmaximum 600
        vbox:
            spacing 20
            text "You"
            bar value hero.hp range hero.max_hp
    
    frame:
        xpadding 10
        ypadding 10
        xalign 0.9
        yalign 0.05
        xmaximum 600
        vbox:
            spacing 20
            if level == 1 and enemy_1.alive:
                text "Enemy 1"
                bar value enemy_1.hp range enemy_1.max_hp
            if level == 2:
                if enemy_2_1.alive: 
                    text "Enemy 1"
                    bar value enemy_2_1.hp range enemy_2_1.max_hp
                if enemy_2_2.alive: 
                    text "Enemy 2"
                    bar value enemy_2_2.hp range enemy_2_2.max_hp
            if level == 3:
                if enemy_3_1.alive: 
                    text "Enemy 1"
                    bar value enemy_3_1.hp range enemy_3_1.max_hp
                if enemy_3_2.alive: 
                    text "Enemy 2"
                    bar value enemy_3_2.hp range enemy_3_2.max_hp
                if enemy_3_3.alive: 
                    text "Enemy 3"
                    bar value enemy_3_3.hp range enemy_3_3.max_hp