from random import randint

class Controller():

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.move_right = True
        self.move_left = True
        self.move_up = True
        self.move_down = True
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_moving_up = False
        self.is_moving_down = False
        self.loose = False
        self.actual_fire_ball_speed = 3.0
        self.fire_ball_cd = 1500
        self.score = 0

        self.view.window.bind("<KeyPress-q>", lambda event: self.left(event))
        self.view.window.bind("<KeyPress-d>", lambda event: self.right(event))
        self.view.window.bind("<KeyPress-z>", lambda event: self.up(event))
        self.view.window.bind("<KeyPress-s>", lambda event: self.down(event))
        self.view.window.bind("<KeyRelease-q>", lambda event: self.release_left(event))
        self.view.window.bind("<KeyRelease-d>", lambda event: self.release_right(event))
        self.view.window.bind("<KeyRelease-z>", lambda event: self.release_up(event))
        self.view.window.bind("<KeyRelease-s>", lambda event: self.release_down(event))
        self.view.restart_button.config(command=self.restart)

        self.start()
        self.check()

    def start(self):
        def repeat():
            if(self.loose):
                return
            self.new_fire_ball()
            if(self.fire_ball_cd>=400):
                self.fire_ball_cd -= 50
            elif(self.fire_ball_cd >= 50):
                self.fire_ball_cd -= 5
            if(self.actual_fire_ball_speed <= 12):
                self.actual_fire_ball_speed += 0.5
            self.view.window.after(self.fire_ball_cd, repeat)
        repeat()

    def check(self):
        def repeat():
            if(self.loose):
                return
            i = 0
            size = len(self.view.fire_balls)
            while(i < size):
                x = self.view.fire_balls[i]["x"]
                y = self.view.fire_balls[i]["y"]
                x_p = self.view.x_player
                y_p = self.view.y_player
                if((x_p - 7 < x + 15 and x_p - 7 > x - 15 and y_p < y+15 and y_p > y - 15) or (x_p + 7 < x + 15 and x_p + 7 > x - 15 and y_p < y+15 and y_p > y - 15)):
                   self.player_lost()
                elif((y_p - 7 < y + 15 and y_p - 7 > y - 15 and x_p < x+15 and x_p > x - 15) or (y_p + 7 < y + 15 and y_p + 7 > y - 15 and x_p < x+15 and x_p > x - 15)):
                    self.player_lost()
                i += 1
            self.view.window.after(10, repeat)
        repeat()
    
    def restart(self):
        if(not self.loose):
            return
        self.view.canvas.config(bg="yellow")
        self.loose = False
        self.view.change_stop()
        self.view.score_label.config(text="Score: 0")
        self.score = 0
        self.check()
        self.start()

    def left(self, event):
        if(self.is_moving_left):
            return
        else:
            self.is_moving_left = True
        def repeat():
            self.view.left()
            if(self.move_left):
                self.view.window.after(20, repeat)
            else:
                self.move_left = True
                self.is_moving_left = False
        repeat()


    def right(self, event):
        if(self.is_moving_right):
            return
        else:
            self.is_moving_right = True
        def repeat():
            self.view.right()
            if(self.move_right):
                self.view.window.after(20, repeat)
            else:
                self.move_right = True
                self.is_moving_right = False
        repeat()
        
    def up(self, event):
        if(self.is_moving_up):
            return
        else:
            self.is_moving_up = True
        def repeat():
            self.view.up()
            if(self.move_up):
                self.view.window.after(20, repeat)
            else:
                self.move_up = True
                self.is_moving_up = False
        repeat()
        
    def down(self, event):
        if(self.is_moving_down):
            return
        else:
            self.is_moving_down = True
        def repeat():
            self.view.down()
            if(self.move_down):
                self.view.window.after(20, repeat)
            else:
                self.move_down = True
                self.is_moving_down = False
        repeat()

    def release_left(self, event):
        self.move_left = False

    def release_right(self, event):
        self.move_right = False

    def release_up(self, event):
        self.move_up = False

    def release_down(self, event):
        self.move_down = False

    def new_fire_ball(self):
        self.score += 1
        self.view.score_label.config(text="Score: " + str(self.score))
        spot = randint(0, 3)
        if(spot == 0):
            self.view.create_fire_ball(0, randint(80, self.view.get_height() - 80), int(self.actual_fire_ball_speed), 0)        
        elif(spot == 1):
            self.view.create_fire_ball(self.view.get_width(), randint(80, self.view.get_height() - 80), - int(self.actual_fire_ball_speed), 0)        
        elif(spot == 2):
            self.view.create_fire_ball(randint(80, self.view.get_width() - 80), 0, 0, int(self.actual_fire_ball_speed))        
        else:
            self.view.create_fire_ball(randint(80, self.view.get_width() - 80), self.view.get_height(), 0, -int(self.actual_fire_ball_speed)) 

    def player_lost(self):
        self.loose = True
        self.view.change_stop()
        self.actual_fire_ball_speed = 3.0
        self.fire_ball_cd = 1500
        self.view.canvas.config(bg = "red") 