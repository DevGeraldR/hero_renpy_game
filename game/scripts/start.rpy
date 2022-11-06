label start:

    # For background
    scene intro_bg

    # Create hero

    $ hero = character("Hero", 20, 20)
    $ hero.hp = hero.max_hp
    $ hero_attack_value = 0
    $ level = 1

    # For start menu. "is_from" is use for controling the game_manager
    menu start_menu: 
        "Start":
            $ is_from = "Start_menu"
            jump game_manager
        "Reset level":
            $ level = 1
            "Level Reseted"
            jump start_menu

    # For end menu. call in every end of each level

    menu end_menu:
        "Play this level again?":
            $ is_from = "Play Again"
            jump game_manager
        "Back to Main Menu":
            $ is_from = "Back to Main Menu"
            jump game_manager

    return