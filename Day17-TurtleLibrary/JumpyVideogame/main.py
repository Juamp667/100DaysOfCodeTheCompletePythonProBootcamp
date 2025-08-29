import turtle as t
from player import player
import scenario as scn
from numpy.random import random, choice

global show_TitleScreen
show_TitleScreen=True

def winnerScreen(win):
    global i_
    f = lambda n: f"C:\\Users\\Juamp6.67\\Documents\\projects\\100DaysOfCodeTheCompletePythonProBootcamp\\Day17-TurtleLibrary\\JumpyVideogame\\images\\winnerScreen\\frame_{str('000'+str(n))[-3:]}.gif"
    imax = 299
    win.bgpic(f(i_))
    print(i_,imax)
    if i_<imax:
        i_+=1
    else:
        i_=0
    win.ontimer(lambda win=win: winnerScreen(win),16)

def init_game(win):
    global show_TitleScreen,i_
    i_ = 0
    show_TitleScreen = False
    win.bgpic(picname = "C:\\Users\\Juamp6.67\\Documents\\projects\\100DaysOfCodeTheCompletePythonProBootcamp\\Day17-TurtleLibrary\\JumpyVideogame\\images\\bg_spikes.gif")

    #Initializing platforms
    y0 = -0.45*win.window_height()
    base_platform = scn.Platform(length=1000,x=0, y=y0, width=2, color="green")
    n_platforms = choice(range(5, 10))
    platforms:list[scn.Platform] = [scn.Platform() for i in range(n_platforms)]
    dy = 0.7*win_height/(n_platforms+1)
    y_ = -0.7*win_height/2 + dy*random()
    for platform in platforms:
        x_ = 0.75*random()*win_width/2*choice([-1,1])
        platform.setpos(x=x_, y=y_)
        y_ += dy*(1+0.5*random())

    #Initializing the winners platform
    platforms[-1].fillcolor("DarkGoldenRod")


    #Initializing player
    p1 = player()
    p1.sety(y0+50)
    p1_pos_0 = p1.pos()

    #Setting key listener events
    win.onkeypress(p1.charge_jump, key="w")
    win.onkeyrelease(p1.jump, key="w")
    for side_key in "ad":
        win.onkeypress(lambda k=side_key: p1.side_move(k), key=side_key)
        win.onkeyrelease(fun=p1.stop_side_move, key=side_key)
    win.listen()


    def game_loop():
        if win.win:
            win.clear()
            winnerScreen(win)
        else:
            p1.update(win)
            p1.detect_collision([base_platform, *platforms], win)
            win.ontimer(game_loop, 2)
            if win.loose:
                p1.setpos(p1_pos_0)
                win.loose = False
                p1.on_platform = False
                p1.v_y = 0
                p1.v_y0 = 0
                p1.v_x = 0

    game_loop()
    win.mainloop()

win_width = 510
win_height = 703
win = t.Screen()
win.setup(win_width,win_height)
win.bgpic(picname="C:\\Users\\Juamp6.67\\Documents\\projects\\100DaysOfCodeTheCompletePythonProBootcamp\\Day17-TurtleLibrary\\myImplementation\\images\\titleScreen.gif")
win.onkey(fun=lambda window=win: init_game(window), key="space")
win.listen()

win.loose = False
win.win = False

global i_
i_=0
def update_TitleScreen():
    global i_
    f = lambda n: f"C:\\Users\\Juamp6.67\\Documents\\projects\\100DaysOfCodeTheCompletePythonProBootcamp\\Day17-TurtleLibrary\\myImplementation\\images\\titleScreen\\frame_{str('000'+str(n))[-3:]}.gif"
    imax = 299
    if show_TitleScreen:
        win.bgpic(f(i_))
        print(i_,imax)
        if i_<imax:
            i_+=1
        else:
            i_=0
        win.ontimer(update_TitleScreen,16)

update_TitleScreen()
win.exitonclick()