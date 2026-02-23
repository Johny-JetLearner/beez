import pgzrun
import random
WIDTH=500
HEIGHT=500
bee=Actor("bee")
bee.x=300
bee.y=200
score=0
flower=Actor("flower")
flower.x=random.randint(0,500)
flower.y=random.randint(0,500)
def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(str(score),center=(50,50))
def update():
    global score 
    if keyboard.up:
        bee.y=bee.y-5
    if keyboard.down:
        bee.y=bee.y+5
    if keyboard.right:
        bee.x=bee.x+5
    if keyboard.left:
        bee.x=bee.x-5
    if bee.colliderect(flower):
        flower.x=random.randint(0,500)
        flower.y=random.randint(0,500)
        score=score+10
pgzrun.go()