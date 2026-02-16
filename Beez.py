import pgzrun
import random
WIDTH=500
HEIGHT=500
bee=Actor("bee")
bee.x=300
bee.y=200
flower=Actor("flower")
flower.x=random.randint(0,500)
flower.y=random.randint(0,500)
def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
pgzrun.go()
