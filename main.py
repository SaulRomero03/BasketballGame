import tkinter
from tkinter import ttk


class BallAnimation():
    def __init__(self, canvas_width=1200, canvas_height=800,
                 ball_start_xpos=630, ball_start_ypos=210,
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
        self.mouse_is_clicked = False

    def resetball(self):
        xl, yl, xr, yr = self._canvas.coords(self.arms)
        y = (yl + yr) / 2
        self._canvas.coords(self._ball,
                            xr - self._ball_radius,
                            y - self._ball_radius,
                            xr + self._ball_radius,
                            y + self._ball_radius)

    def start(self):
        self.resetball()
        self.animatetimer()


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

    def animatetimer(self):

        self.timer= self.timer - self._refresh_msec/1000 * 10  #(refresh_msec = .01)
        if self.timer<=0:
            self.timer=0
            self._canvas.delete(self._ball)
            self._ball=None
        self.timerstr.set("Time: %.1f" % self.timer)
        if self.timer>0:
            self._root.after(self._refresh_msec * 10 , self.animatetimer)



    def create_background(self):
        self.base = self._canvas.create_rectangle(765,325,800,600,fill="#7E7E7E", outline='black', dash = (3,8),  width = 3,  tags = 'hoop')
                                                #(x1,y1 Left top Corner & x2,y2 Right Bottom corner))
        self.hoop = self._canvas.create_rectangle(700,320,780,325, fill='white', outline="#D0312D", tags = 'hoop', width = 2.5 )

        self.head = self._canvas.create_rectangle(185,420,250,480, fil='green', outline='black', tags='Body')
        self.body = self._canvas.create_oval(190,470 , 245, 550, fill = 'blue', outline ='black', tags='Body')
        self.arms = self._canvas.create_rectangle(235,490,280,500, fill = 'magenta', outline = 'black', tags='Body')
        self.backboard = self._canvas.create_rectangle(780, 210, 798, 325, fill = 'white', outline = '#7E7E7E', dash = (3,5), width = 3, tags = 'hoop')
        self.scoreboard = self._canvas.create_rectangle(350,25,850,125, fill='black', outline = '#D4AF37', width =5 )
        self.pointssqr = self._canvas.create_rectangle(375, 50,520,100, fill="red", outline = 'white', width=4 )
        self.timesqr = self._canvas.create_rectangle(555,54, 665, 94, fill='black', outline = 'white', width = 4)
        self.sqr2 = self._canvas.create_rectangle(690, 50, 830, 100, fill='blue', outline = 'white', width=4)
        self.line = self._canvas.create_rectangle(1,585, 1999,800, fill='grey', outline = 'black' , width = 4)

        self.instructions= tkinter.StringVar(self._canvas, "Instructions:")
        self.instructionsstr = ttk.Label(self._canvas, textvariable=self.instructions).place(anchor=tkinter.CENTER, x=635, y=630)

        self.str1 = tkinter.StringVar(self._canvas, "Rules are Simple")
        self.string1 = ttk.Label(self._canvas, textvariable=self.str1).place(anchor=tkinter.CENTER, x=635, y=660)

        self.str2 = tkinter.StringVar(self._canvas, "Make as many baskets as you can before the time runs out")
        self.string2 = ttk.Label(self._canvas, textvariable=self.str2).place(anchor=tkinter.CENTER,x=635, y=680)

        self.str3 = tkinter.StringVar(self._canvas, " Each time you score the player will move back further away from the hoop")
        self.string3 = ttk.Label(self._canvas, textvariable=self.str3).place(anchor=tkinter.CENTER, x=635, y=700)

        self.str6 = tkinter.StringVar(self._canvas, "Click & Drag on the ball to shoot")
        self.string6 = ttk.Label(self._canvas, textvariable=self.str6).place(anchor=tkinter.CENTER, x=635, y=720)


        self.str4 = tkinter.StringVar(self._canvas, " Good Luck!")
        self.string4 = ttk.Label(self._canvas, textvariable=self.str4).place(anchor=tkinter.CENTER,x=635, y=740)

        self.str5 = tkinter.StringVar(self._canvas, " Press the Start Button to begin")
        self.string5 = ttk.Label(self._canvas, textvariable=self.str5).place(anchor=tkinter.CENTER,x=635, y=760)


        #self.time = self._canvas.create_rectangle()
        self._canvas.move('Body', 700, 35)
        self._canvas.move('hoop', 400, 0)
        self.startbutton = ttk.Button( self._frame, text = "Start", command=self.start  ).grid(column = 0, row= 1)


    #def instructions(self):




    # Create a canvas for animation and add it to main window
    def create_canvas(self):
        self._canvas = tkinter.Canvas(self._frame, height=self._canvas_height, width=self._canvas_width)
        self._canvas.grid(column=3, row=3)
        self._canvas.configure(bg="#55BED7")
        self._canvas.bind( '<Button-1>', self._print_location)
        self._canvas.bind( '<ButtonRelease-1>', self._print_location2)
        self._canvas.bind_all('<Key-Left>', self.moveleft)
        self._canvas.bind_all('<KeyRelease-Left>', self.stop)
        self._canvas.bind_all('<Key-Right>', self.moveright)
        self._canvas.bind_all('<KeyRelease-Right>', self.stop)
        self._canvas.bind_all('<Key-Up>', self.jump)
        self._canvas.bind_all('<KeyRelease-Up>',self.stop)
        self._canvas.bind_all('<Key-Down>',self.down)
        self._canvas.bind_all('<KeyRelease-Down>', self.stop)

        self.score = 0
        self.scorestring = tkinter.StringVar(self._canvas, " Score: 0")
        self.scoreboard = ttk.Label(self._canvas, textvariable=self.scorestring).place(anchor=tkinter.CENTER, x=450, y=75)

        self.timer = 60
        self.timerstr = tkinter.StringVar(self._canvas, "Time:")
        self.timerlabel = ttk.Label(self._canvas, textvariable=self.timerstr).place(anchor=tkinter.CENTER, x=610, y=75)

        self.miss = 0
        self.missstr= tkinter.StringVar(self._canvas, "Miss Shots: 0")
        self.misslabel = ttk.Label( self._canvas, textvariable = self.missstr).place (anchor=tkinter.CENTER, x=760, y=75)

        self.miss == self.miss + 1

    def _print_location(self, event):
        print( 'Button 1 was pressed at pixel x=%d, y=%d' % (event.x, event.y))
        self.start =  (event.x, event.y)
        self.mouse_is_clicked = True
        self.animate_power_meter()

    def _print_location2(self, event):
        print( 'Button 1 was released at pixel x=%d, y=%d' % (event.x, event.y))
        self.stop =  (event.x, event.y)
        self._xinc = (self.start[0] - self.stop[0])/4
        self._yinc = (self.start[1] - self.stop[1])/4
        if self.start[0] == self.stop[0]:
            self.gravity=0
        else:
            self.gravity = 2

        if self.start[1] == self.stop[1]:
            self.gravity = 0
        else:
            self.gravity = 2
        self.start = (event.x, event.y)
        self._canvas.coords(self._ball,
                            self.start[0] - self._ball_radius,
                            self.start[1] - self._ball_radius,
                            self.start[0] + self._ball_radius,
                            self.start[1] + self._ball_radius)
        self.mouse_is_clicked = False

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
                                              fill="#B54213", outline="black", width=1.5)
        self.gravity=0


    # Update the ball animation, end with callback after self._refresh_msec
    def animate_ball(self):
        if not self._ball:
            return
        self._canvas.move(self._ball, self._xinc, self._yinc)
        # Get the current coordinates of the bounding box of the ball
        xl, yl, xr, yr = self._canvas.coords(self._ball)

        # adding gravity
        hoopcoords = self._canvas.coords(self.hoop)
        self._yinc = self._yinc + self.gravity  # the top of the screen is y = 0, bottom is y = window height
        buffer=15
        if xl >= hoopcoords[0]-buffer and xr <= hoopcoords[2]+buffer and (yl - self._yinc) <=hoopcoords[1] and yl > hoopcoords[1]:
            if self.start[0]<400:
                self.score= self.score + 3

            else:
                self.score = self.score +2
            self.scorestring.set("Score=%d" % self.score)
            self._canvas.move('Body', - 25,0)
        backboardcoords= self._canvas.coords(self.backboard)
        if xr >= backboardcoords[0] and xr - self._xinc < backboardcoords[0] and yr > backboardcoords[1] and yl < backboardcoords[3]:
            self._xinc= -self._xinc * 0.8
            print('hitbackboard')

        elif xl < abs(self._xinc) or xr > self._canvas_width - abs(self._xinc):
            self.resetball()
            self._xinc=0
            self._yinc=0
            self.gravity=0
            self.miss = self.miss + 1
            self.missstr.set("Missed: %d" % self.miss)
        elif yl < abs(self._yinc) or yr > self._canvas_height - abs(self._yinc):
            self.resetball()
            self._xinc = 0
            self._yinc = 0
            self.gravity=0
            self.miss = self.miss + 1
            self.missstr.set("Missed: %d" % self.miss)
        self._root.after(self._refresh_msec, self.animate_ball)

    # Update the power meter animation
    def animate_power_meter(self):
        # delete the existing one
        #print("powerfunction")
        self._canvas.delete('power_meter')
        # only update while the button is held down
        if not self.mouse_is_clicked:
            return
        # Figure out where the cursor is now
        cursor_x = self._canvas.winfo_pointerx() - self._canvas.winfo_rootx()
        cursor_y = self._canvas.winfo_pointery() - self._canvas.winfo_rooty()
        # Get the arrow direction as difference between current mouse position and where click started
        dx = cursor_x - self.start[0]
        dy = cursor_y - self.start[1]
        scale = 0.25
        # Start the arrow at a fixed position
        #arrow_start_pos = self._canvas_width - 50, 50

        # Start the arrow where the ball is
        xl, yl, xr, yr = self._canvas.coords(self._ball)
        arrow_start_pos = (xl+xr)/2., (yl+yr)/2.

        # Create the line
        self._canvas.create_line(arrow_start_pos[0], arrow_start_pos[1], arrow_start_pos[0] - dx * scale,
                                 arrow_start_pos[1] - dy * scale, tags='power_meter', arrow=tkinter.LAST, dash = (3,5))
        # Call this function again after _refresh_msec to update the power arrow
        self._root.after(self._refresh_msec, self.animate_power_meter)


def main():
    # The actual execution starts here
    ba = BallAnimation()
    ba.run(0, 0)


if __name__ == '__main__':
    main()
