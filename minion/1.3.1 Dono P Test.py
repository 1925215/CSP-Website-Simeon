import turtle as trtl
import random as rand
import math
import winsound
import threading
import cv2

wn = trtl.Screen()
wn.screensize(200,200)
wn.bgpic("space background.gif")

cap = cv2.VideoCapture('videoplayback-ezgif.com-video-cutter.mp4')

if (cap.isOpened()== False):
    print("Error opening video file")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
ship_image = "gruship.gif"
explosion = "explosion.gif"
minion1 = "minion1.gif"
minion2 = "minion2.gif"
minion3 = "minion3.gif"
minion4 = "minion4.gif"
minion5 = "minion5.gif"
minion6 = "minion6.gif"
minion7 = "minion7.gif"
minion8 = "minion1.gif"
minion9 = "minion2.gif"
minion10 = "minion3.gif"
minion11= "minion4.gif"
minion12= "minion5.gif"
minion13= "minion6.gif"
minion14= "minion7.gif"
card_minion = "click here minion.gif"
card = "Happy Birthday Card.gif"
i=0
j=0
minions = []
shapes = []
go = False
f= False
gruship = trtl.Turtle()
wn = trtl.Screen()
minion  = trtl.Turtle()
minion.pu()
#ship_image = PhotoImage(file=r"minion/Gru Ship.gif").subsample(2,2)
#wn.addshape("ship_image", Shape("image", ship_image))
wn.addshape(ship_image)
wn.addshape(explosion)
wn.addshape(minion1)
wn.addshape(minion2)
wn.addshape(minion3)
wn.addshape(minion4)
wn.addshape(minion5)
wn.addshape(minion6)
wn.addshape(minion7)
wn.addshape(minion8)
wn.addshape(minion9)
wn.addshape(minion10)
wn.addshape(minion11)
wn.addshape(minion12)
wn.addshape(minion13)
wn.addshape(minion14)
wn.addshape(card_minion)
wn.addshape(card)
shapes.append(minion1)
shapes.append(minion2)
shapes.append(minion3)
shapes.append(minion4)
shapes.append(minion5)
shapes.append(minion6)
shapes.append(minion7)
shapes.append(minion8)
shapes.append(minion9)
shapes.append(minion10)
shapes.append(minion11)
shapes.append(minion12)
shapes.append(minion13)
shapes.append(minion14)

def exploding(thing):
  stop()
  global go,f
  f=True
  #unicorn_move(unicorn, -100, -45)
  if go == False:
    go = True
    thing.pu()
    thing.shape(explosion)
    explode.start()
    wn.update
    i=0
    for step in minions:
        minions[i].shape(shapes[i])
        x = rand.randint(-300,300)
        y = rand.randint(-100,200)
        temp = minions[i]
        temp.goto(x,y)
        temp.st()
        i=i+1
    stop()
    thing.ht()
    fall()

def click_the_card(x,y):
    minion.shape(card)
    birthday.start()


def draw_ship(thing):
  thing.pu()
  thing.ht()
  thing.shape(ship_image)
  wn.update()

def fall():
  wn.tracer(0)
  minion.shape(card_minion)
  minion.goto(0,0)
  for step in range(100):
      i=0
      for each in minions:
        minions[i].speed(0)
        minions[i].backward(2)
        if i % 2 == 0:
          minions[i].setx(minions[i].xcor() + 1) 
        else:
          minions[i].setx(minions[i].xcor() - 1)
        i=i+1
      wn.update()
      trtl.time.sleep(0.05)
  wn.tracer(1)
  minion.onclick(click_the_card)
  wn.listen()

def talk():
    winsound.PlaySound("minion talk.wav", winsound.SND_ASYNC)

def explosion_sound():
    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

def happy():
    winsound.PlaySound("minionsound.wav", winsound.SND_ASYNC)

def stop():
    winsound.PlaySound(None, winsound.SND_PURGE)

while i<14:
  minioni = trtl.Turtle()
  minioni.pu()
  minioni.ht()
  minioni.setheading(90)
  minions.append(minioni)
  i = i+1

draw_ship(gruship)

gruship.goto(-1000,0)
talking = threading.Thread(target=talk)
explode = threading.Thread(target=explosion_sound)
birthday = threading.Thread(target=happy)
talking.start()
gruship.st()
x=-1000
while x<0:
  x += 1
  y =math.sin(0.5*x)*2.5
  gruship.goto(x,y)


wn.onclick(lambda x,y: exploding(gruship))
wn.listen()


wn.mainloop()