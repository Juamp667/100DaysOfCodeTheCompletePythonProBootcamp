import turtle as t
import time as tm
from time import time
from turtle import Screen
import scenario as scn


#Player's class is created with inheritance form Turtle class
class player(t.Turtle):
    global t0,t1, w_clicked, delay, t_, on_platform, dt 
    dt=0.2

    def __init__(self, shape = "circle", undobuffersize = 1000, visible = False):
        global w_clicked, t_, on_platform

        super().__init__(shape, undobuffersize, visible)
        
        #Player's velocity is set to zero initially
        self.v_y = 0
        self.v_x = 0
        self.v_y0 = 0

        self.penup()    #Pen is up so it does not paint 
        self.speed(0)   #Speed's set to fastest
        self.showturtle()

        #Jumping variables
        w_clicked = False   #Ininitally "w" is not clicked
        t_ = 0  
        self.on_platform = False    #Initially player should fall if it's not in a platform


    def charge_jump(self):
        '''
        Charges jump until "w" key is released. The more time player presses "w" the higher the jump.
        '''
        global t0, w_clicked
        if not w_clicked:
            w_clicked = True
            t0 = time() #Time when "w" is initially clicked
            print("Charging jump")


    def jump(self):
        '''
        Jumps when the player releases "w" key.
        '''
        global t0,t1, w_clicked
        if self.on_platform:    #Player can jump only stepping in a platform
            t1 = time() #Time when "w" is released
            dt=t1-t0    #Time the key "w" has been pressed
            
            #Set both velocities to an amount depending dt, so the higher dt the higher v_y
            self.v_y  = int(dt/0.025)   
            self.v_y0 = int(dt/0.025)
            
            w_clicked = False           #After release "w" key, it's not clicked/pressed
            self.on_platform = False    #As the player jumps it leaves the platform

            #Debug information: prints the initial jump velocity
            print(f"v_y={self.v_y}")


    def side_move(self, key):
        '''
        Sets the horizontal velocity depending on the key pressed ("a"/"d").
        '''
        v_x0 = 20   #Default constant horizontal velocity
        dirs = {"a":-v_x0, "d":+v_x0}
        self.v_x = dirs[key]

    def stop_side_move(self):
        '''
        Stops the horizontal velocity when "a"/"d" key is released.
        '''
        self.v_x = 0

    def update(self, screen):
        '''
        Updates player position
        '''
        self.check_x(screen)
        self.check_y(screen)

    def check_x(self,win):
        '''
        Updates the horizontal position depending on v_x.
        '''
        global dt
        #Move the player when v_x!=0
        if self.v_x!=0: 
            x_0 = self.xcor()
            self.setx(x_0+self.v_x*dt)

        #Check if the player has touched the spikes at the sides
        if abs(self.xcor())>win.window_width()/2-30:
            win.loose = True


    
    def check_y(self, win:t.Screen):
        '''
        Updates the vertical position.
        '''
        global t_, dt
        #Move the player when v_y!=0 or its not in a platform
        a = -10 #Acceleration due to gravity
        if not self.on_platform:    #If not in a platform, player should feel gravity
            t_ += dt    #Time since the ball started falling
            self.sety(self.ycor()+(self.v_y0+a*t_)*dt)
            self.v_y += a*dt
        elif (self.v_y)and(t_):   #If in a platform, v_y and t_ are reset to zero
            self.v_y = 0
            t_ = 0

        #Check if the player has touched the spikes at the top
        if abs(self.ycor())>win.window_height()/2-30:
            win.loose = True

    
    def detect_collision(self, platforms:list[scn.Platform],win):
        '''
        Detects collisions between the player and platforms.
        '''
        #Get the player coordinates
        y0 = self.ycor()
        x0 = self.xcor()

        #Check for collision with platforms
        for platform in  platforms:
            pltfrm_height = platform.shapesize()[0]*10
            pltfrm_width = platform.shapesize()[1]*10

            dy = 10+pltfrm_height
            y_diff = y0-platform.ycor()
            
            if (0<=y_diff<dy)and(self.v_y<=0):  #When stepping/falling and coincide with platfotms ycor()
                if abs(x0-platform.xcor())<pltfrm_width: #If inside the platform
                    self.on_platform = True
                    self.v_y0 = 0
                    if platform==platforms[-1]: #If platform is the winner's one 
                        win.win = True
                else:   #If outside the platform, player falls
                    self.on_platform = False

            elif (-dy<y_diff<0)and(abs(x0-platform.xcor())<pltfrm_width+10):  #When colliding with a platform from below
                self.v_y0 = -self.v_y
                self.v_y = -self.v_y
                self.on_platform = False