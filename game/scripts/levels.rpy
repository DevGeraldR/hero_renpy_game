define e1 = Character("Fire Enemy")
define e2 = Character("Ice Enemy")
define e3 = Character("Forest Enemy")

# For level 1 battle

label level_1:

    # For background
    scene bg fire_battle

    show talk hero
    voice "../audio/hero/h5.wav"
    h "Now we are at the fire world"

    voice "../audio/hero/h6.wav"
    h "Right now we have two skills both of them has their own damage"

    voice "../audio/hero/h7.wav"
    h "Be wise in choosing attack as this will cause other peoples life"

    voice "../audio/hero/h8.wav"
    h "Be alert at anytime enemy may appear"

    show talk enemy_1
    voice "../audio/e1/e1.wav"
    e1 "A human, are you too excited to die that you came here?"

    show talk hero
    voice "../audio/hero/h9.wav"
    h "We are here to defeat you!"

    show talk enemy_1
    voice "../audio/e1/e1_2.wav"
    e1 "Do you think you can do that?"
    
    show talk hero
    voice "../audio/hero/h10.wav"
    h "Enough with the  talk let's fight!"

    hide talk

    window hide

    # Create the enemy

    $ enemy_1 = character("enemy_1", 12, 12)
    $ enemy_1.hp = enemy_1.max_hp
    $ enemy = "enemy_1"

    
    # Show characters

    show hero stand:
        xalign 0.2
        yalign 0.7
    show enemy_1 stand:
        xalign 0.8
        yalign 0.7

    # Show life bars
    show screen hp_bars_1v1

    # For gameplay

    jump gameplay_1v1


# For level 2 battle

label level_2:

    # For background
    scene bg ice_battle

    show talk hero
    voice "../audio/hero/h11.wav"
    h "Now we are at the ice world"

    voice "../audio/hero/h12.wav"
    h "Be prepared the enemy is much stronger in here"

    voice "../audio/hero/h13.wav"
    h "There they are we must defeat them to restore the ice world"

    show talk enemy_2
    voice "../audio/e2/e2_1.wav"
    e2 "Is that a joke?"

    voice "../audio/e2/e2_2.wav"
    e2 "Do you really think that, that human can defeat us?"

    show talk hero
    voice "../audio/hero/h14.wav"
    h "Ofcourse, with the right judgement, He can defeat you with no time..."

    show talk enemy_2
    voice "../audio/e2/e2_3.wav"
    e2 "Lets begin then!!!"

    hide talk
    window hide

    # Create enemy's

    $ enemy_2_1 = character("Enemy_2_1", 12, 12)
    $ enemy_2_2 = character("Enemy_2_2", 12, 12)
    $ enemy_2_1.hp = enemy_2_1.max_hp
    $ enemy_2_2.hp = enemy_2_2.max_hp

    # Show life bars

    show screen hp_bars_1v2

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

    jump gameplay_1v2
    
# For level 3 battle

label level_3:

    # For background
    scene bg forest_battle

    show talk hero
    voice "../audio/hero/h15.wav"
    h "We are now in the forest world"

    voice "../audio/hero/h16.wav"
    h "The last world that needs our help"

    voice "../audio/hero/h17.wav"
    h "But here the enemy is far more stronger that thoose we fought"

    voice "../audio/hero/h18.wav"
    h "But we beleive in you! The whole humanity is on your hand!"

    voice "../audio/hero/h19.wav"
    h "You can defeat them!!!"

    show talk enemy_3
    voice "../audio/e3/e3_1.wav"
    e3 "HA HA HA HA, don't understatement us those you fought are just a peice of trash"
    
    show talk hero
    voice "../audio/hero/h20.wav"
    h "Just like you all?"

    show talk enemy_3
    voice "../audio/e3/e3_2.wav"
    e3 "WHAAAAAA!!!!! Come on lets begin I am to excited to kill you!!!"

    hide talk
    window hide

    # Create enemy's

    $ enemy_3_1 = character("Enemy_3_1", 12, 12)
    $ enemy_3_2 = character("Enemy_3_2", 12, 12)
    $ enemy_3_3 = character("Enemy_3_3", 12, 12)
    $ enemy_3_1.hp = enemy_3_1.max_hp
    $ enemy_3_2.hp = enemy_3_2.max_hp
    $ enemy_3_3.hp = enemy_3_3.max_hp


    # Show life bars
    show screen hp_bars_1v3

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
        xalign 1.1
        yalign 0.75

    # For gameplay

    jump gameplay_1v3

# Random Number Generator
# For critical hit and other action that happens unintentional

label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

#For life bars

screen hp_bars_1v1:
    vbox:
        xalign 0.1
        yalign 0.05
        xmaximum 600
        spacing 20
        text "You"
        bar value hero.hp range hero.max_hp
    
    vbox:
        xalign 0.9
        yalign 0.05
        xmaximum 600
        spacing 20
        text "Fire Enemy"
        bar value enemy_1.hp range enemy_1.max_hp

screen hp_bars_1v2:
    vbox:
        xalign 0.1
        yalign 0.05
        xmaximum 600
        spacing 20
        text "You"
        bar value hero.hp range hero.max_hp

    
    vbox:
        xalign 0.9
        yalign 0.05
        xmaximum 600
        spacing 20
        if enemy_2_1.alive: 
            text "Ice Enemy 1"
            bar value enemy_2_1.hp range enemy_2_1.max_hp
        if enemy_2_2.alive: 
            text "Ice Enemy 2"
            bar value enemy_2_2.hp range enemy_2_2.max_hp

screen hp_bars_1v3:

        vbox:
            xalign 0.1
            yalign 0.05
            xmaximum 600
            spacing 20
            text "You"
            bar value hero.hp range hero.max_hp
    
        vbox:
            xalign 0.9
            yalign 0.05
            xmaximum 600
            spacing 20
            if enemy_3_1.alive: 
                text "Forest Enemy 1"
                bar value enemy_3_1.hp range enemy_3_1.max_hp
            if enemy_3_2.alive: 
                text "Forest Enemy 2"
                bar value enemy_3_2.hp range enemy_3_2.max_hp
            if enemy_3_3.alive: 
                text "Forest Enemy 3"
                bar value enemy_3_3.hp range enemy_3_3.max_hp
            
# Skills button

screen hero_skills:

    frame:
        xalign 0.1
        yalign 0.9
        xpadding 30
        ypadding 30

        vbox:
            text "Select Skill" at truecenter size 30
            null height 30
            hbox: 
                spacing 20
                imagebutton:
                    idle "../images/skill/punch_skill_idle.png"
                    hover "../images/skill/punch_skill_hover.png"
                    action Return("Punch") 
                imagebutton:
                    idle "../images/skill/super_duper_punch_skill_idle.png"
                    hover "../images/skill/super_duper_punch_skill_hover.png"
                    action Return("Super Duper Punch")
                if level >= 2:
                    imagebutton:
                        idle "../images/skill/heal_skill_idle.png"
                        hover "../images/skill/heal_skill_hover.png"
                        action [SetVariable("target", "self"), Return("Heal")]

# Choose enemy button

screen choose_enemy_1v2:

    textbutton "Cancel":
        background "#000000"
        xalign 0.1
        yalign 0.8
        action Jump("gameplay_1v2")

    if enemy_2_1.alive:
        imagebutton:
            xalign 0.8
            yalign 0.6
            idle "../images/enemy_2/enemy_2_select_idle.png"
            hover "../images/enemy_2/enemy_2_select_hover.png"
            action Return("enemy_2_1") 
    if enemy_2_2.alive: 
        imagebutton:
            xalign 0.8
            yalign 0.9
            idle "../images/enemy_2/enemy_2_select_idle.png"
            hover "../images/enemy_2/enemy_2_select_hover.png"
            action Return("enemy_2_2")

screen choose_enemy_1v3:

    textbutton "Cancel":
        background "#000000"
        xalign 0.1
        yalign 0.8
        action Jump("gameplay_1v3")

    if enemy_3_1.alive:
        imagebutton:
            xalign 0.8
            yalign 0.6
            idle "../images/enemy_3/enemy_3_select_idle.png"
            hover "../images/enemy_3/enemy_3_select_hover.png"
            action Return("enemy_3_1") 
    if enemy_3_2.alive: 
        imagebutton:
            xalign 0.8
            yalign 0.9
            idle "../images/enemy_3/enemy_3_select_idle.png"
            hover "../images/enemy_3/enemy_3_select_hover.png"
            action Return("enemy_3_2") 

    if enemy_3_3.alive: 
        imagebutton:
            xalign 1.1
            yalign 0.75
            idle "../images/enemy_3/enemy_3_select_idle.png"
            hover "../images/enemy_3/enemy_3_select_hover.png"
            action Return("enemy_3_3") 
