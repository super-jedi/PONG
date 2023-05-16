from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed('fast')

    def move_ball(self, direction=45):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        

          

    def bounce_border(self):
    #    change y to bounce from top and bottom
       self.y_move *= -1
  
    def bounce_paddle(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0,0)
        self.bounce_paddle()