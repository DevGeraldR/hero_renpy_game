define h = Character("Hero", who_color="#ffce0abb")

label start:

    # For background image and music

    scene bg intro

    play music "../audio/intro_music.ogg"

    show talk hero

    voice "../audio/hero/h1.wav"
    h "The Ice, Fire, and Forest world was been attacked"
    
    voice "../audio/hero/h2.wav"
    h "They need a hero that has strong dedication to help people"

    voice "../audio/hero/h3.wav"
    h "A hero who has the passion to fight even it will cause his own life"

    voice "../audio/hero/h4.wav"
    h "Let's go and save them"

    hide talk
 
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
        "Credits":
            jump credits
            

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

