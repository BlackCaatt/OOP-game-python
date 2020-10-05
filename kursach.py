import turtle
import random
import math
import time
import os
import winsound

#Настройка окна
wn = turtle.Screen()#Возможность получения экрана
wn.bgcolor("black")
wn.title("Arcade 2d game")
wn.bgpic("background.gif")
wn.register_shape("123.gif")

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()   
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)    #место отображения
        self.score = 0
        self.update_score() #первый вызов, чтобы счетчик показывался изначально
        
    def update_score(self):
        self.clear()    #очищается каждый раз, так как иначе будуд накладываться друг на друга
        self.write("Score: {}".format(self.score), False, align = "left", font = ("Arial", 14, "normal"))   #вывод очков

    def change_score(self, points): #функция обновления счетчика
        self.score += points
        self.update_score()

    def play_sound(self):
        winsound.Beep(2000,2)

class Border(turtle.Turtle):    #наследнует класс turtle

    def __init__(self):
        turtle.Turtle.__init__(self)    #инициализия turtl
        self.penup()    #настройки класса turtle
        self.hideturtle()   #спрячем этот turtle, так как иначе будет отображаться небольшой деффект
        self.speed(0)   #без анимации(моментальное появление)
        self.color("white") #цвет границы
        self.pensize(5) #ширина границы

    def draw_border(self):  #рисование границы
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

class Player (turtle.Turtle):   #class Player - наследник класса Turtle
    
    def __init__ (self):    #Конструктор
        turtle.Turtle.__init__(self)    #инизиализия библиотеки turtle
        self.penup()    #настройки из класса turtle
        self.speed(0)
        self.shape("triangle")  #self = player
        self.color("white")
        self.speed = 0.3

    def move(self): #player move
        self.forward(self.speed)    #turtle двигается вперед со скоростью определенной ранее

        if self.xcor() > 290 or self.xcor() < -290: #если треуг. подходит близко к границе, то он поворачивается влево на 60 град
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def turnleft(self): #персонаж поворачиается влево на 30 градусов
        self.left(30)
        
    def turnright(self):
        self.right(30)
        
    def increaseSpeed(self):   #увеличение скорости на 1
        self.speed += 0.15
        
    def decreaseSpeed(self):
        if self.speed >= 0.45:
            self.speed -= 0.15

class Goal (turtle.Turtle): #создание 

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("purple")
        #self.shape("circle")
        self.shape("123.gif")
        self.speed = 0.46
        self.goto(random.randint(-250, 250), random.randint(-250, 250)) #рандомный спавн
        self.setheading(random.randint(0,360))  #рандомное движение

    def jump(self):
         self.goto(random.randint(-250, 250), random.randint(-250, 250))
         self.setheading(random.randint(0,360))

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)
            
def isCollision (t1, t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False

player = Player()   #Вызов класса
border = Border()   #Вызов класса border
game = Game()


border.draw_border() #нарисовать границу из класса border

goals = []  #Создание списка
for count in range(6):  #повторяем вызов 6 раз
    goals.append(Goal())

#Настройка клавиш для игры
turtle.listen()     #turtle читает какие кнопки нажимает пользователь 
turtle.onkey(player.turnleft, "Left") #когда нажимается стрелка влево персонаж двигается влево
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increaseSpeed, "Up")
turtle.onkey(player.decreaseSpeed, "Down")

wn.tracer(0)    #Останавливает обновление окна


#Main Loop
while True:
   
    wn.update() #вырисовывает модели в памяти, а после обновляет на экране
    player.move()

    for goal in goals:
        goal.move()
        
        if isCollision(player, goal):
            goal.jump()
            game.change_score(10)
            game.play_sound()
