from pyglet import *
import pyglet
import math
import time
from pyglet.window import key
import random

#window stuff
window = pyglet.window.Window(1000,550,"adventure of the lost")
batch = pyglet.graphics.Batch()
batch1 = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()

#keyboard stuff, probably will forget
keys = key.KeyStateHandler()
window.push_handlers(keys)

#load images
me = pyglet.resource.image("me.png")
im = pyglet.resource.image("mynom.png")
im1 = pyglet.resource.image("sowy.png")

highscore = 100

#draw background probably not the best way
frontground = shapes.Rectangle(x=0,y=0,width=1000000,height=1000000,color=(25,90,10))
background = shapes.Rectangle(x=0,y=0,width=1000000,height=1000000,color=(225,225,225))


coin_catch = 0
l1 = pyglet.text.Label("new highscore",font_name="Times New Roman",font_size=50,x=100,y=100)
l = pyglet.text.Label("you win",font_name="Times New Roman",font_size=50,x=50,y=50)
w = pyglet.text.Label("you need to collect 100 coins, good luck ",font_name="Arial",font_size=20,x=50,y=20)

#drawing sprites
rect = shapes.Circle(x=100,y=150,radius=50,color=(12,0,5))
sprite = pyglet.sprite.Sprite(im,x=450,y=50,batch=batch)
playbutton = pyglet.sprite.Sprite(me,x=200,y=200,batch=batch)
player = pyglet.sprite.Sprite(im1,x=90,y=150,batch=batch)
sprite.scale_y = 0.45
sprite.scale_x = 0.45
player.scale_y = 0.5
player.scale_x = 0.5

#wrong usage
@window.event
def on_draw():
   window.clear()
   background.draw()
   batch.draw()
   batch1.draw()
   frontground.draw()
   playbutton.draw()
   w.draw()
   rect.draw()

   if rect.x > playbutton.x:
      rect.x = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002
      w.x = 100000000000000000
      playbutton.x= 100000
      playbutton.y= 100000
      frontground.width = 0
      frontground.height = 0

   if keys[key.UP]:
      rect.y = rect.y + 5
   elif keys[key.DOWN]:
      rect.y = rect.y - 5
   elif keys[key.LEFT]:
      rect.x = rect.x - 5
   elif keys[key.RIGHT]:
      rect.x = rect.x + 5


   if keys[key.W]:
      player.y = player.y + 5
   elif keys[key.S]:
      player.y = player.y - 5
   elif keys[key.A]:
      player.x = player.x - 5
   elif keys[key.D]:
      player.x = player.x + 5
   def update():
     global highscore
     global coin_catch
     
 
     d = math.sqrt(math.pow(player.x-sprite.x,2)  + math.pow(player.y-sprite.y,2))
     if d < 20:
         background.color = (225,225,0)
         coin_catch += 1
         sprite.x = random.randint(20,200)
         sprite.y = random.randint(20,450)
     if coin_catch > 10000:
       
       l.draw()
     if coin_catch > highscore:
        l1.draw()
        coin_catch = highscore

   update()   
pyglet.app.run()
