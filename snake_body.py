import turtle as tr
STARTING_POSITION=[(0,0),(-15,0),(-30,0)]
class Snake:
    def __init__(self):
        self.snake=[]
        for n in STARTING_POSITION:
            self.add_body(n)
        self.head=self.snake[0]
        self.head.shape("circle")

    def add_body(self,n):
        snake_body=tr.Turtle("square")
        snake_body.color("white")
        snake_body.shapesize(0.75)
        snake_body.penup()
        snake_body.goto(n)
        self.snake.append(snake_body)

    def move(self):
        for n in range(len(self.snake)-1,0,-1):
            x_coordinate=self.snake[n-1].xcor()
            y_cooridnate=self.snake[n-1].ycor()
            self.snake[n].goto(x=x_coordinate,y=y_cooridnate)
        self.head.forward(15)

    def turn_up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def turn_right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def turn_left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def turn_down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def extend_body(self):
        self.add_body(self.snake[-1].position())
    def reset_snake(self):
        for segments in self.snake:
            segments.goto(1000,1000)
        self.snake.clear()
        for n in STARTING_POSITION:
            self.add_body(n)
            self.head=self.snake[0]
            self.head.shape("circle")
