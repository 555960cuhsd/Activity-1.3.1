import random as rand
import turtle as trtl
import time

##################
### Game setup ###
##################

wn = trtl.Screen()
wn.addshape("taco.gif")
wn.addshape("burrito.gif")

score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-200, -180)
score_writer.pendown()

# Upgrade Button
button = trtl.Turtle()
button.speed(0)
button.shape("burrito.gif")
button.penup()
button.setposition(-170, 180)

# Score rate
score_rate = 1
upgrade_cost = (score_rate*2)**2

rate = trtl.Turtle()
rate.speed(0)
rate.penup()
rate.hideturtle()
rate.setposition(-200, -220)
rate.pendown()
rate.write("tacos per click: " + str(score_rate))

next = trtl.Turtle()
next.speed(0)
next.penup()
next.hideturtle()
next.setposition(-220, 200)
next.pendown()
next.write("Next upgrade: " + str(upgrade_cost) + " tacos")

# Chicken
taco = trtl.Turtle()
score = 0
taco.shape("taco.gif")

taco.speed(0)
taco.penup() 

font_setup = ("Arial", "15", "normal")

score_writer.write(str(score) + " tacos", font = font_setup)

# Point Text
p = trtl.Turtle()
p.hideturtle()
p.speed(3)



######################
### Game functions ###
######################
def taco_click(x, y):
  update_score()
  

def update_score():
  score_writer.clear()
  global score
  score += score_rate
  print(score)
  score_writer.write(str(score) + " tacos", font = font_setup)
  



def button_click(x, y):
  upgrade() 

def upgrade():
  global score_rate
  global score
  global upgrade_cost
  if score >= upgrade_cost:
    score_rate += 1
    rate.clear()
    rate.write("Tacos per click: " + str(score_rate))
    score -= upgrade_cost
    score_writer.clear()
    score_writer.write(str(score) + " tacos", font = font_setup)
    upgrade_cost = (score_rate*2)**2

    next.clear()
    next.write("Next upgrade: " + str(upgrade_cost) + " tacos")

button.onclick(button_click)
taco.onclick(taco_click)

wn.mainloop()
