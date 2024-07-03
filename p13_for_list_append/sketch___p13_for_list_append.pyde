# p13_for_list_append
def setup():
    global imgBG, imgBird
    size(1180,590) 
    imgBG= loadImage('background.jpg')
    imgBird = loadImage('Bird.png')
def draw():
    global imgBG, imgBird
    image(imgBG, 0, 0)
    for i in range(len(x)):
        image(imgBird, x[i]-400, y[i]-300, 800, 600)
    image(imgBird, mouseX-400, mouseY-300, 800,600)
x = [] # x = [0]*10
y = [] # y = [0]*10
#N = 0
def mousePressed():
    x.append(mouseX) #global N
    y.append(mouseY)#x[N], y[N] = mouseX, mouseY
    #N += 1  
