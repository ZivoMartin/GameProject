import tkinter as tk

class View():

    def __init__(self, window, speed):
        self.window = window
        self.speed = speed
        self.stop = False
        self.x_player = 500
        self.y_player = 350
        self.width = 800
        self.height = 500
        self.fire_balls = []
        self.count_id = 0

        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, background='yellow')
        self.player = self.canvas.create_rectangle(self.x_player - 7, self.y_player - 7, self.x_player + 7, self.y_player + 7, fill="green")
        self.restart_button = tk.Button(self.window, text="restart")
        self.score_label = tk.Label(self.window, text="Score: 0")
        self.canvas.pack()
        self.restart_button.pack(side="bottom")
        self.score_label.pack(side="top")


    


    def move_player(self, x, y):
        self.canvas.delete(self.player)
        self.player = self.canvas.create_rectangle(x-7, y-7, x + 7, y + 7, fill="green")

    def left(self):
        if(self.x_player >= self.speed):
            self.move_player(self.x_player - self.speed, self.y_player)
            self.x_player = self.x_player - self.speed
    
    def right(self):
        if(self.x_player <= self.width - self.speed):
            self.move_player(self.x_player + self.speed, self.y_player)
            self.x_player = self.x_player + self.speed
    
    def up(self):
        if(self.y_player >= self.speed):
            self.move_player(self.x_player, self.y_player - self.speed)
            self.y_player = self.y_player - self.speed

    def down(self):
        if(self.y_player <= self.height - self.speed):
            self.move_player(self.x_player, self.y_player + self.speed)
            self.y_player = self.y_player + self.speed

    
    def create_fire_ball(self, x, y, speed_x, speed_y):
        fire_ball = self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="red")
        self.count_id += 1
        self.fire_balls.append({"fire_ball": fire_ball, "id": self.count_id - 1, "x": x, "y": y})
        
        def repeat(indice, id):
            size = len(self.fire_balls)
            if(indice >= size):
                indice = size - 1
            while(self.fire_balls[indice]["id"] != id):
                indice -= 1
            self.canvas.delete(self.fire_balls[indice]["fire_ball"])
            if(self.stop or not (self.fire_balls[indice]["x"] >= 0 and self.fire_balls[indice]["x"] <= self.width and self.fire_balls[indice]["y"] >= 0 and self.fire_balls[indice]["y"] <= self.height)):
                self.fire_balls.pop(indice)
            else:
                self.fire_balls[indice]["x"] += speed_x
                self.fire_balls[indice]["y"] += speed_y
                self.fire_balls[indice]["fire_ball"] = self.canvas.create_oval(self.fire_balls[indice]["x"]-15, self.fire_balls[indice]["y"]-15, self.fire_balls[indice]["x"]+15, self.fire_balls[indice]["y"]+15, fill="red")
                self.canvas.after(20, lambda : repeat(indice, id))
            

        repeat(len(self.fire_balls) - 1, self.count_id - 1)
    

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    

    
    def change_stop(self):
        if(self.stop):
            self.stop = False
        else:
            self.stop = True