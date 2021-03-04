import tkinter
from tkinter import ttk


class BallAnimation():
    def __init__(self, canvas_width=800, canvas_height=600,
                 ball_start_xpos=315, ball_start_ypos=495,
                 ball_radius=30, refresh_msec=10):
        # width of the animation window
        self._canvas_width = canvas_width
        # height of the animation window
        self._canvas_height = canvas_height
        # initial x position of the ball
        self._ball_start_xpos = ball_start_xpos
        # initial y position of the ball
        self._ball_start_ypos = ball_start_ypos
        # radius of the ball
        self._ball_radius = ball_radius
        # delay between successive frames in milliseconds
        self._refresh_msec = refresh_msec
        # create the visual objects
        self.create_window()
        self.create_canvas()
        self.create_ball()
        self.create_background()

    def run(self, xinc, yinc):
        self._xinc = xinc
        self._yinc = yinc
        self._root.after(0, self.animate_ball)
        self.xspeed = 0
        self.yspeed = 0
        self._root.after(0, self.animateplayer)
        self._root.mainloop()

    # The main window of the animation
    def create_window(self):
        self._root = tkinter.Tk()
        self._root.title("Tkinter Animation Demo")

        self._frame = ttk.Frame(self._root, padding="5 5 5 5")
        self._frame.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

        # Add a "Quit" button at the top
        self._quit_button = ttk.Button(self._frame, text="Quit", command=self._root.quit).grid(column=0, row=0,
                                                                                               sticky=tkinter.N)
        # Create the drawing canvas
        #self.create_canvas()
        self.score = 0
        self.scorestring = tkinter.StringVar(self._frame,"Score= 0")
        self.scoreboard = ttk.Label(self._frame, textvariable=self.scorestring).grid(column=0, row=2)

    def create_background(self):
        self.base = self._canvas.create_rectangle(765,325,800,600,fill="yellow", outline="black")
                                                #(x1,y1 Left top Corner & x2,y2 Right Bottom corner))
        self.hoop = self._canvas.create_rectangle(700,320,780,325, fill='red', outline="black")

        self.head = self._canvas.create_rectangle(180,405,250,475, fil='blue', outline='black', tags='Body')
        self.body = self._canvas.create_oval(180,470 , 240, 550, fill = 'red', outline ='black', tags='Body')
        self.arms = self._canvas.create_rectangle(235,490,310,500, fill = 'orange', outline = 'black', tags='Body')
        self.shootingline = self._canvas.create_arc(310, 600, 600, 350, style=tkinter.ARC, fill='black', dash=(3,5), extent=-100, start=180)

        #if self.mouseclicked == True:
            #self._canvas.show(self.shootingline)
        #else:
            #self._canvas.delete(self.shootingline)


    # Create a canvas for animation and add it to main window
    def create_canvas(self):
        self._canvas = tkinter.Canvas(self._frame, height=self._canvas_height, width=self._canvas_width)
        self._canvas.grid(column=0, row=1)
        self._canvas.configure(bg="white")
        self._canvas.bind_all( '<Button-1>', self._print_location)
        self._canvas.bind_all( '<ButtonRelease-1>', self._print_location2)
        self._canvas.bind_all('<Key-Left>', self.moveleft)
        self._canvas.bind_all('<KeyRelease-Left>', self.stop)
        self._canvas.bind_all('<Key-Right>', self.moveright)
        self._canvas.bind_all('<KeyRelease-Right>', self.stop)
        self._canvas.bind_all('<Key-Up>', self.jump)
        self._canvas.bind_all('<KeyRelease-Up>',self.stop)
        self._canvas.bind_all('<Key-Down>',self.down)
        self._canvas.bind_all('<KeyRelease-Down>', self.stop)

    def _print_location(self, event):
        print( 'Button 1 was pressed at pixel x=%d, y=%d' % (event.x, event.y))
        self.start =  (event.x, event.y)
        self.mouseclicked = True

    def _print_location2(self, event):
        print( 'Button 1 was released at pixel x=%d, y=%d' % (event.x, event.y))
        self.stop =  (event.x, event.y)
        self._xinc = (self.start[0] - self.stop[0])/2.5
        self._yinc = (self.start[1] - self.stop[1])/2.5
        if self.start[0] == self.stop[0]:
            self.gravity=0
        else:
            self.gravity = 4.5

        if self.start[1] == self.stop[1]:
            self.gravity = 0
        else:
            self.gravity = 4.5
        self.start = (event.x, event.y)
        self._canvas.coords(self._ball,
                            self.start[0] - self._ball_radius,
                            self.start[1] - self._ball_radius,
                            self.start[0] + self._ball_radius,
                            self.start[1] + self._ball_radius)
        self.mouseclicked = False

    def moveleft(self, event):
        self.xspeed = - 5

    def moveright(self, event):
        self.xspeed = + 5

    def stop(self, event):
        self.xspeed = 0
        self.yspeed = 0

    def jump(self, event):
        self.yspeed = - 3


    def down(self, event):
        self.yspeed = + 3





    def animateplayer(self):
        self._canvas.move('Body',self.xspeed, self.yspeed)
        self._root.after(self._refresh_msec, self.animateplayer)



    # Create the ball at the initial position on the canvas
    def create_ball(self):
        self._ball = self._canvas.create_oval(self._ball_start_xpos - self._ball_radius,
                                              self._ball_start_ypos - self._ball_radius,
                                              self._ball_start_xpos + self._ball_radius,
                                              self._ball_start_ypos + self._ball_radius,
                                              fill="brown", outline="white", width=4)
        self.gravity=0


    # Update the ball animation, end with callback after self._refresh_msec
    def animate_ball(self):
        self._canvas.move(self._ball, self._xinc, self._yinc)
        # Get the current coordinates of the bounding box of the ball
        xl, yl, xr, yr = self._canvas.coords(self._ball)

        # adding gravity
        self._yinc = self._yinc + self.gravity  # the top of the screen is y = 0, bottom is y = window height
        if (xr - self._xinc) <=700 and xr > 700 and (yl - self._yinc) <=325 and yl > 325:
            if self.start[0]<400:
                self.score= self.score + 3

            else:
                self.score = self.score +2
            self.scorestring.set("Score=%d" % self.score)
        # if xr > self._canvas_width - abs(self._xinc):
        #     #if self.start[0]>400:
        #     if self._canvas_width-self.start[0]:
        #         self.score = self.score + 3
        #     else:
        #         self.score = self.score + 2
        #     self.scorestring.set("Score=%d" %self.score)
        if xl < abs(self._xinc) or xr > self._canvas_width - abs(self._xinc):
            self._xinc = -self._xinc * 0.8

        if yl < abs(self._yinc) or yr > self._canvas_height - abs(self._yinc):
            self._yinc = -self._yinc * 0.8
        self._root.after(self._refresh_msec, self.animate_ball)



def main():
    # The actual execution starts here
    ba = BallAnimation()
    ba.run(0, 0)


if __name__ == '__main__':
    main()