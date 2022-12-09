label start:

    # For background image and music
    scene bg intro
    play music "../audio/intro_music.ogg"

    # Create hero

    $ hero = character("Hero", 20, 20)
    $ hero.hp = hero.max_hp
    $ hero_attack_value = 0
    $ level = 1

    # For start menu. "is_from" is use for controling the game_manager
    menu start_menu: 
        "Start Battle":
            stop music
            jump game_manager
        "Reset level":
            $ level = 1
            "Level Reseted"
            jump start_menu

    # For end menu. call in every end of each level

    menu end_menu:
        "Play this level again?":
            jump game_manager
        "Back to Main Menu":
            # For background and music
            scene bg intro
            play music "../audio/intro_music.ogg"

            jump start_menu

    return

