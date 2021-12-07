import random as rand
import turtle as trtl
import math
import time


##################
### Game setup ###
##################

wn = trtl.Screen()

wn.setup(580,449)
wn.addshape("taco.gif")
wn.addshape("menu.gif")
wn.addshape("burrito.gif")
wn.addshape("buttonunpressed.gif")
wn.addshape("buttonpressed.gif")
wn.addshape("fork.gif")
wn.addshape("background.gif")
wn.addshape("tabasco.gif")
rectCors = ((-10,20),(10,20),(10,-20),(-10,-20))
wn.register_shape('rectangle',rectCors)
score = 0

# math problems and answers for burrito lootbox
math_problems = ["1 + 1 = ?","84 / 4 = ?","5 * 25 = ?","3^4 = ?","9 ^ 1/2 = ?","6 * 2 = ?", "50 / 10 = ?","Solve for x. 9((3x+6)/3) = 0"]
math_anwers = ["2", "21", "125","81","3", "12", "5", "-2"]

# Score Writer
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-450, -250)
score_writer.pendown()
# Font
font_setup = ("Arial", "15", "normal")


# Taco per click upgrade Button
button = trtl.Turtle()
button.speed(0)
button.penup()
button.setposition(-510, 118)

# Burrito math loot box
burrito = trtl.Turtle()
burrito.speed(0)
burrito.shape("burrito.gif")
burrito.penup()
burrito.hideturtle()

# Score rate
score_rate = 1
upgrade_cost = (score_rate*3)**2

rate = trtl.Turtle()
rate.speed(0)
rate.penup()
rate.hideturtle()
rate.setposition(-450, -230)
rate.pendown()

# Score rate upgrade text
next = trtl.Turtle()
next.color("moccasin")
next.speed(0)
next.penup()
next.hideturtle()
next.setposition(-550, 180)
next.pendown()

# Taco
taco = trtl.Turtle()
score = 0
taco.shape("taco.gif")

taco.speed(0)
taco.penup() 
taco.setposition(-190, -150)

font_setup = ("Arial", "15", "normal")


#-----game start-----
wn.bgpic("menu.gif")
game_start = False
settings = trtl.Turtle()
start_button = trtl.Turtle()
start_button.color("lemonchiffon")
start_button.shape("fork.gif")

start_button.shapesize(4)


######################
### Game functions ###
######################
def start_game(x, y):
  global game_start
  wn.setup(1200,700)
  wn.bgpic("background.gif")
  game_start = True
  start_button.hideturtle()
  taco.showturtle()
  score_writer.write(str(score) + " tacos", font = font_setup)
  
  taco.shape("taco.gif")
  button.shape("buttonunpressed.gif")
  next.write("Next upgrade: " + str(upgrade_cost) + " tacos",font = ("Arial", "7", "italic"))
  rate.write("tacos per click: " + str(score_rate))

start_button.onclick(start_game)


while game_start != True:
  taco.hideturtle()
  button.hideturtle()

####################
### Autoclickers ###
####################
tabasco = trtl.Turtle()
tabasco_writer = trtl.Turtle()

sauce_list = [tabasco, tabasco_writer]
for sauces in sauce_list:
  sauces.penup()
  sauces.speed(0)

# Menu writer
sauce_font = ("Times New Roman", "17", "italic")
menu_writer = trtl.Turtle()
menu_writer.penup()
menu_writer.speed(0)
menu_writer.hideturtle()
menu_item_list = ["-  TABASCO  -", "-  BBQ SAUCE  -", "-  KETCHUP  -", "-  MAYONNAISE  -", "-  SOY SAUCE  -"]
menu_item_coords = [(310, 145), (310, 55), (310, -35), (310, -125), (310, -215)]
for i in range(5):
  menu_writer.setposition(menu_item_coords[i])
  menu_writer.write(menu_item_list[i], font = sauce_font)


#-----tabasco-----
tabasco_delay = 5
tabasco.setposition(285, 130)
tabasco.shape("tabasco.gif")
tabasco_amount = 0
tabasco_cost = (tabasco_amount+1)**2

def tabasco_click():
  update_score(tabasco_amount)
  tabasco_autoclick()

def tabasco_autoclick():
  wn.ontimer(tabasco_click, tabasco_delay*1000)

def buy_tabasco(x, y):
  global tabasco_amount, score, tabasco_cost
  if score >= tabasco_cost:
    tabasco_amount += 1
    score -= tabasco_cost
    update_score(0)
    tabasco_cost = (tabasco_amount+1)**2
    update_tabasco()

# tabasco writer
tabasco_writer.hideturtle()
tabasco_writer.setposition(310, 120)
tabasco_writer.write("0 oz. of Tabasco", font = font_setup)
tabasco_writer.setposition(310, 100)
tabasco_writer.write("Current cost: " + str(tabasco_cost) + " tacos")

def update_tabasco():
  global tabasco_amount
  tabasco_writer.clear()
  tabasco_writer.setposition(310, 120)
  tabasco_writer.write(str(tabasco_amount) + " oz. of Tabasco", font = font_setup)
  tabasco_writer.setposition(310, 100)
  tabasco_writer.write("Current cost: " + str(tabasco_cost) + " tacos")

tabasco_autoclick()

#-----bbq sauce-----

########################
### Burrito Loot Box ###
########################
def countdown():
  burrito.setposition(rand.randint(-300, 90), rand.randint(50, 120))
  burrito.showturtle()
  wn.ontimer(countdown, rand.randint(30000,120000))
wn.ontimer(countdown,rand.randint(30000,120000))

#When the taco is clicked increase the score
def taco_click(x, y):
  update_score(score_rate)

#When the burrito is clicked ask a random math question
def burrito_click(x, y):
  lootbox()

#Asking the random math question
def lootbox():
  number = rand.randint(0,len(math_problems)-1)  
  answer = wn.textinput("Problem","What is " + str(math_problems[number]))
  while answer != math_anwers[number]:
    answer = wn.textinput("Problem","Try again what is " + (math_problems[number]))
  else:
    update_score(rand.randint(50,150))
    burrito.hideturtle()


#update the amount of tacos
def update_score(amount):
  global score
  score_writer.clear()
  score += amount
  print(score)
  score_writer.write(str(score) + " tacos", font = font_setup)
  
######################
### Upgrade Button ###
######################
#When the button is clicked upgrade
def button_click(x, y):
  upgrade() 

#Updgrade the rate of tacos per click
def upgrade():
  global score_rate
  global score
  global upgrade_cost
  if score >= upgrade_cost:
    button.shape("buttonpressed.gif")
    score_rate += 1
    rate.clear()
    rate.write("Tacos per click: " + str(score_rate))
    score -= upgrade_cost
    score_writer.clear()
    score_writer.write(str(score) + " tacos", font = font_setup)
    upgrade_cost = (score_rate*3)**2

    next.clear()
    next.write("Next upgrade: " + str(upgrade_cost) + " tacos",font = ("Arial", "7", "italic"))
    button.shape("buttonunpressed.gif")


#-----click detection-----
tabasco.onclick(buy_tabasco)
burrito.onclick(burrito_click)
button.onclick(button_click)
taco.onclick(taco_click)
button.showturtle()

wn.listen()
wn.mainloop()