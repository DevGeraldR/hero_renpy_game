# For background images

image bg intro = im.Scale("intro_bg.png", 1920, 1080)
image bg intro2 = im.Scale("intro_2_bg.jpg", 1920, 1080)
image bg fire_battle = im.Scale("fire_battle_bg.png", 1920, 1080)
image bg ice_battle = im.Scale("ice_battle_bg.png", 1920, 1080)
image bg forest_battle = im.Scale("forest_battle_bg.png", 1920, 1080)

# To show new skill

image new_skill heal = im.Scale("../images/skill/heal_skill_idle.png", 190, 200)

# Animation when character is standing

image hero stand :
    "../images/hero/hero_stand_1.png"
    pause 0.2
    "../images/hero/hero_stand_2.png"
    pause 0.2
    "../images/hero/hero_stand_3.png"
    pause 0.2
    repeat 

image enemy_1 stand :
    "../images/enemy_1/enemy_1_stand_1.png"
    pause 0.2
    "../images/enemy_1/enemy_1_stand_2.png"
    pause 0.2
    repeat
    
image enemy_2_1 stand :
    "../images/enemy_2/enemy_2_stand_1.png"
    pause 0.2
    "../images/enemy_2/enemy_2_stand_2.png"
    pause 0.2
    repeat

image enemy_2_2 stand :
    "../images/enemy_2/enemy_2_stand_1.png"
    pause 0.2
    "../images/enemy_2/enemy_2_stand_2.png"
    pause 0.2
    repeat

image enemy_3_1 stand :
    "../images/enemy_3/enemy_3_stand_1.png"
    pause 0.2
    "../images/enemy_3/enemy_3_stand_2.png"
    pause 0.2
    "../images/enemy_3/enemy_3_stand_3.png"
    pause 0.2
    repeat

image enemy_3_2 stand :
    "../images/enemy_3/enemy_3_stand_1.png"
    pause 0.2
    "../images/enemy_3/enemy_3_stand_2.png"
    pause 0.2
    "../images/enemy_3/enemy_3_stand_3.png"
    pause 0.2
    repeat

image enemy_3_3 stand :
    "../images/enemy_3/enemy_3_stand_1.png"
    pause 0.2
    "../images/enemy_3/enemy_3_stand_2.png"
    pause 0.2
    "../images/enemy_3/enemy_3_stand_3.png"
    pause 0.2
    repeat

# Animation when character is striking

image hero attack :
    "../images/hero/hero_attack_1.png"
    pause 0.2
    "../images/hero/hero_attack_2.png"

image enemy_1 attack:
    "../images/enemy_1/enemy_1_attack_1.png"
    pause 0.2
    "../images/enemy_1/enemy_1_attack_2.png"

image enemy_2_1 attack:
    "../images/enemy_2/enemy_2_attack_1.png"
    pause 0.2
    "../images/enemy_2/enemy_2_attack_2.png"

image enemy_2_2 attack:
    "../images/enemy_2/enemy_2_attack_1.png"
    pause 0.2
    "../images/enemy_2/enemy_2_attack_2.png"

image enemy_3_1 attack:
    "../images/enemy_3/enemy_3_attack_1.png"
    pause 0.2
    "../images/enemy_3/enemy_3_attack_2.png"

image enemy_3_2 attack:
    "../images/enemy_3/enemy_3_attack_1.png"
    pause 0.2
    "../images/enemy_3/enemy_3_attack_2.png"

image enemy_3_3 attack:
    "../images/enemy_3/enemy_3_attack_1.png"
    pause 0.2
    "../images/enemy_3/enemy_3_attack_2.png"

# Animation when character was hit

image hero hit :
    "../images/hero/hero_hit.png"
    pause 0.1

image enemy_1 hit :
    "../images/enemy_1/enemy_1_hit.png"
    pause 0.1

image enemy_2_1 hit :
    "../images/enemy_2/enemy_2_hit.png"
    pause 0.1

image enemy_2_2 hit :
    "../images/enemy_2/enemy_2_hit.png"
    pause 0.1

image enemy_3_1 hit :
    "../images/enemy_3/enemy_3_hit.png"
    pause 0.1

image enemy_3_2 hit :
    "../images/enemy_3/enemy_3_hit.png"
    pause 0.1

image enemy_3_3 hit :
    "../images/enemy_3/enemy_3_hit.png"
    pause 0.1

# Animation when healing

image hero heal =  "../images/hero/hero_heal.png"
image enemy_1 heal =  "../images/enemy_1/enemy_1_heal.png"
image enemy_2_1 heal = "../images/enemy_2/enemy_2_heal.png"
image enemy_2_2 heal = "../images/enemy_2/enemy_2_heal.png"
image enemy_3_1 heal =  "../images/enemy_3/enemy_3_heal.png"
image enemy_3_2 heal = "../images/enemy_3/enemy_3_heal.png"
image enemy_3_3 heal = "../images/enemy_3/enemy_3_heal.png"

# For talk animation

image talk hero :
    "../images/hero/hero_talk_1.png" 
    pause 0.1
    "../images/hero/hero_talk_2.png" 
    pause 0.1
    "../images/hero/hero_talk_3.png" 
    pause 0.1
    repeat

image talk enemy_1:
    "../images/enemy_1/enemy_1_talk.png" 
    pause 0.1
    "../images/enemy_1/enemy_1_talk_2.png" 
    pause 0.1
    "../images/enemy_1/enemy_1_talk_3.png" 
    pause 0.1
    repeat

image talk enemy_2:
    "../images/enemy_2/enemy_2_talk.png" 
    pause 0.2
    "../images/enemy_2/enemy_2_talk_2.png" 
    pause 0.2
    repeat

image talk enemy_3:
    "../images/enemy_3/enemy_3_talk.png" 
    pause 0.2
    "../images/enemy_3/enemy_3_talk_2.png" 
    pause 0.2
    repeat

