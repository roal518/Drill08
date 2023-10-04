from pico2d import *
import random
# Game object class here
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
def update_world():
    for o in world:
        o.update()
    pass
def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()
def reset_world():
    global running
    global grass
    global team
    global balls
    global world
#월드 하나로 모든 요소 통제 가독성이 good
    running =True
    world=[]
    grass=Grass()
    world.append(grass)
    balls =[Ball()for i in range(20)]
    team =[Boy() for i in range(11)]
    world +=team
    world +=balls
class Boy:
    def __init__(self):
        self.x,self.y=random.randint(0,300),90
        self.frame =0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame+1)%8
        self.x +=random.randint(0,4)
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
class Ball:
    def __init__(self):
        self.x,self.y = random.randint(0,800),random.randint(499,500)
        self.frame = 0
        if random.randint(0,1) == 1:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
    def update(self):
        if self.y>75:
            self.y -=random.randint(1,4)
        else:
            pass
    def draw(self):
        self.image.draw(self.x,self.y)
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self):
        pass
open_canvas()
reset_world()
# initialization code
# game main loop code
while running:
    handle_events()
    update_world()#game logic
    render_world()#draw game world
    delay(0.05)
# finalization code
close_canvas()
