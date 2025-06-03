from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import choice, randint

app = Ursina()


# player = Entity(model='cube', color=color.orange, scale=(1,2,1), position=(0,1,500))
player = FirstPersonController(model="cube", position=(0, 1, -80), speed=50, collider='box')
camera.z = -5

# z = 0
# for i in range(20):
#     platform = Entity(model='cube', color=color.gray, scale=(10, 0.5, 50), position=(0,1,z), texture="white_cube", collider='box' )
#     z += 3
platform = Entity(model='cube', scale=(10, 0.5, 300), position=(0,1,0), texture="white_cube", collider='box', texture_scale=(50,50) )
goal = Entity(model='sphere', scale=(5,10,7), position=(0,-1, 80), texture='brick', collider='mesh')

blocks = []

def create_blocks():
    global blocks
    locations = set()
    for i in range(500):
            x = random.randrange(-5, 5, 1)
            y = 0
            z = random.randrange(-75, 250, 5)
            locations.add((x,y,z))
        
    final_goal = random.choice(list(locations))  
    locations.remove(final_goal)

    for loc in locations:
            cube_width = 2
            cube_height = random.randrange(3, 8, 1)
            cube_depth = 1
            block = Entity(model="cube", scale=(cube_width, cube_height, cube_depth),dz=0.01, texture='brick', color=color.blue, collider='box', position=loc)
            blocks.append(block)
       
create_blocks()
message = Text(text="COOKED!", scale=1.5, origin=(0,0), background=True, color=color.blue)
message2 = Text(text='CONGRATS!', scale=1.5, origin=(0,0), background=True, color=color.red)
message.enabled = False
message2.enabled = False


def move():
      global blocks
    #   print("HERE:",len(blocks))
      for b in blocks:
        b.z -= b.dz
        if b.z > 50:
            b.dz *=-1

def die():
    #application.pause()
    message.enabled = True
    respawn_point = (0, 1, -80)
    player.position = respawn_point

def reset_blocks():
    global blocks
    for block in blocks:
        destroy(block)
        
    blocks.clear()
    create_blocks()

def update():
    global message,blocks
    if held_keys["escape"]:
        application.quit()
    move()
    hit_info = player.intersects()

    if hit_info.hit:
        if hit_info.entity in blocks:
            print("die")
            die()
        if hit_info.entity == goal:
            message2.enabled = True
            

    if held_keys["r"]:
        respawn_point = (0,1, -80)
        player.position = respawn_point
        reset_blocks()
        message.enabled = False
    if held_keys["f"]:
        player.jump_height += 3
    
        
        



app.run()
    



    




