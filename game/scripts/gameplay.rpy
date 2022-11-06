# To Reset level, hide previous image and assign user to apropriate level

label game_manager:

    # Reset the player and target hp before going to the
    # next level or same level again as try again
    
    $ hero.hp = hero.max_hp
    $ target_hp = 0
    $ target = " "

    # Play the battle music before entering the battle

    play music "../audio/battle_music.ogg"

    # Enter the level

    if level == 1:
        jump level_1 
    elif level == 2:
        jump level_2
    elif level == 3:
        jump level_3