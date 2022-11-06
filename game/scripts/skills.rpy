# For hero attack

label hero_skill:

    # If heal return after excecuting the skill. The rest after this is for attacking an opponent
    
    if skill == "Heal":
        call hero_skill_animation
        if d10 + hero.hp > hero.max_hp:
            $ hero.hp = hero.max_hp
        else:
            $ hero.hp += d10
        return

    # Find the oponent

    if target == "enemy_2_1":
        $ target_hp = enemy_2_1.hp
    elif target == "enemy_2_2":
        $ target_hp = enemy_2_2.hp
    elif target == "enemy_3_1":
        $ target_hp = enemy_3_1.hp
    elif target == "enemy_3_2":
        $ target_hp = enemy_3_2.hp
    elif target == "enemy_3_3":
        $ target_hp = enemy_3_3.hp
    # Reminder enemy 1 wasn't assign as target because target only use when the enemy select
    # the opponent in level 2 or up. Enemy 1 is in level 1 and has only 1 opponent.
    else:
        $ target_hp = enemy_1.hp

    # To calculates the damage & reduce the damage to the opponent

    if skill == "Punch":
        call hero_skill_animation
        if d10 >= 8:
            $ hero_attack_value = d4 + d6
            $ target_hp -= hero_attack_value
        else:
            $ target_hp -= d4
    elif skill == "Super Duper Punch": 
        call hero_skill_animation          
        if d10 >= 9:    
            $ hero_attack_value = (d6 + d4)*2
            $ target_hp -= hero_attack_value
        elif d10 >= 5:
            $ hero_attack_value =  d6 + 2                                        
            $ target_hp -= hero_attack_value
        else:
            $ hero_attack_value =  d6
            $ target_hp -= hero_attack_value

    # Reassigned the new value

    if target == "enemy_2_1":
        $ enemy_2_1.hp = target_hp

        # Handle if target was killed

        if enemy_2_1.hp <= 0: 
            $ enemy_2_1.alive = False
            hide enemy_2_1 stading with dissolve

    elif target == "enemy_2_2":
        $ enemy_2_2.hp = target_hp

        # Handle if target was killed

        if enemy_2_2.hp <= 0: 
            $ enemy_2_2.alive = False
            hide enemy_2_2 stading with dissolve
    elif target == "enemy_3_1":
        $ enemy_3_1.hp = target_hp

        # Handle if target was killed

        if enemy_3_1.hp <= 0: 
            $ enemy_3_1.alive = False
            hide enemy_3_1 stading with dissolve
    elif target == "enemy_3_2":
        $ enemy_3_2.hp = target_hp

        # Handle if target was killed

        if enemy_3_2.hp <= 0: 
            $ enemy_3_2.alive = False
            hide enemy_3_2 stading with dissolve
    
    elif target == "enemy_3_3":
        $ enemy_3_3.hp = target_hp

        # Handle if target was killed

        if enemy_3_3.hp <= 0: 
            $ enemy_3_3.alive = False
            hide enemy_3_3 stading with dissolve

    else:
        $ enemy_1.hp = target_hp

        # Handle if target was killed

        if enemy_1.hp <= 0: 
            $ enemy_1.alive = False
            hide enemy_1 stading with dissolve

    return

# Animation when hero attack

label hero_skill_animation:

    # To go the target location

    if level == 1:

        # Go to the target position

        show hero attack with dissolve:
            xalign 0.8
            yalign 0.7

        # Show animation when target hit

        show enemy_1 hit

    elif level >= 2:

        # To go and attack the target enemy
        # Self target means heal

        if target == "self":
            show hero heal with dissolve:
                xalign 0.2
                yalign 0.7
        
        elif target == "enemy_2_1":
            show hero attack with dissolve:
                xalign 0.8
                yalign 0.6
            show enemy_2_1 hit
        elif target == "enemy_2_2":
            show hero attack with dissolve:
                xalign 0.8
                yalign 0.9
            show enemy_2_2 hit
        elif target == "enemy_3_1":
            show hero attack with dissolve:
                xalign 0.8
                yalign 0.6
            show enemy_3_1 hit
        elif target == "enemy_3_2":
            show hero attack with dissolve:
                xalign 0.8
                yalign 0.9
            show enemy_3_2 hit
        elif target == "enemy_3_3":
            show hero attack with dissolve:
                xalign 0.9
                yalign 0.75
            show enemy_3_3 hit
            

    # Go back to the standing position

    show hero stand with dissolve:
        xalign 0.2
        yalign 0.7

    return
    
# For enemy attack

label enemy_attack:

    # For random values to decided in healing, damage and critical

    call dice_roll

    # To calculates the damage & reduce the damage to the opponent
    # Calls enemy attack animation to display action in the screen

    if level == 1:    

        if d20 >= 21:
            call enemy_attack_animation                                                                                
            $ hero.hp -= d10

        # When healing

        elif d20 <=2:

            # Toisplay healing animation

            show enemy_1 heal with dissolve

            if d4 + enemy_1.hp > enemy_1.max_hp:
                $ enemy_1.hp = enemy_1.max_hp
            else:
                $ enemy_1.hp += d4

            # To hide healing animation

            show enemy_1 stand with dissolve

        else:
            call enemy_attack_animation                                                                                
            $ hero.hp -= d4

    elif level >= 2:

        if enemy == "enemy_2_1":      

            if d20 >= 19:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d10

            elif d20 <=2:

                # To display healing animation

                show enemy_2_1 heal

                if d4 + enemy_2_1.hp > enemy_2_1.max_hp:
                    $ enemy_2_1.hp = enemy_2_1.max_hp
                else:
                    $ enemy_2_1.hp += d4

                # To hide healing animation

                show enemy_2_1 stand
            else:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d4

        elif enemy == "enemy_2_2":            

            if d20 >= 19:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d10
            elif d20 <=2:

                # To display healing animation

                show enemy_2_2 heal with dissolve

                if d4 + enemy_2_2.hp > enemy_2_2.max_hp:
                    $ enemy_2_2.hp = enemy_2_2.max_hp
                else:
                    $ enemy_2_2.hp += d4

                # To hide healing animation

                show enemy_2_2 stand
            else:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d4

        elif enemy == "enemy_3_1":            

            if d20 >= 19:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d10
            elif d20 <=2:

                # To display healing animation

                show enemy_3_1 heal with dissolve

                if d4 + enemy_3_1.hp > enemy_3_1.max_hp:
                    $ enemy_3_1.hp = enemy_3_1.max_hp
                else:
                    $ enemy_3_1.hp += d4

                # To hide healing animation

                show enemy_3_1 stand
            else:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d4

        elif enemy == "enemy_3_2":            

            if d20 >= 19:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d10
            elif d20 <=2:

                # To display healing animation

                show enemy_3_2 heal with dissolve

                if d4 + enemy_3_2.hp > enemy_3_2.max_hp:
                    $ enemy_3_2.hp = enemy_3_2.max_hp
                else:
                    $ enemy_3_2.hp += d4

                # To hide healing animation

                show enemy_3_2 stand
            else:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d4

        elif enemy == "enemy_3_3":            

            if d20 >= 19:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d10
            elif d20 <=2:

                # To display healing animation

                show enemy_3_3 heal with dissolve

                if d4 + enemy_3_3.hp > enemy_3_3.max_hp:
                    $ enemy_3_3.hp = enemy_3_3.max_hp
                else:
                    $ enemy_3_3.hp += d4

                # To hide healing animation

                show enemy_3_3 stand
            else:
                call enemy_attack_animation                                                                                
                $ hero.hp -= d4
        
    return

# Animation for target 1 attack

label enemy_attack_animation:

    # Go to the hero location and execute attack
    # Go back after execution of attack

    if enemy == "enemy_1":
        show enemy_1 attack with dissolve:
            xalign 0.2
            yalign 0.7
        show hero hit
        show enemy_1 stand with dissolve:
            xalign 0.8 
            yalign 0.7
    elif enemy == "enemy_2_1":
        show enemy_2_1 attack with dissolve:
            xalign 0.2
            yalign 0.7
        show hero hit
        show enemy_2_1 stand with dissolve:
            xalign 0.8 
            yalign 0.6
    elif enemy == "enemy_2_2":
        show enemy_2_2 attack with dissolve:
            xalign 0.2
            yalign 0.7
        show hero hit
        show enemy_2_2 stand with dissolve:
            xalign 0.8 
            yalign 0.9
    elif enemy == "enemy_3_1":
        show enemy_3_1 attack with dissolve:
            xalign 0.2
            yalign 0.7
        show hero hit
        show enemy_3_1 stand with dissolve:
            xalign 0.8 
            yalign 0.6
    elif enemy == "enemy_3_2":
        show enemy_3_2 attack with dissolve:
            xalign 0.2
            yalign 0.7
        show hero hit
        show enemy_3_2 stand with dissolve:
            xalign 0.8 
            yalign 0.9
    elif enemy == "enemy_3_3":
        show enemy_3_3 attack with dissolve:
            xalign 0.2
            yalign 0.7
        show hero hit
        show enemy_3_3 stand with dissolve:
            xalign 0.9 
            yalign 0.75
    return