# p11_for_many_image_list_void_mousePressed
def setup():
    global imgBG, imgBird
    size(1180,590) 
    imgBG= loadImage('background.jpg')
    imgBird = loadImage('Bird.png')
def draw():
    global imgBG, imgBird
    image(imgBG, 0, 0)
    for i in range(200):
        image(imgBird, x[i]-400, y[i]-300, 800, 600)
    image(imgBird, mouseX-400, mouseY-300, 800,600)
x = [0]*200
y = [0]*200
N = 0
def mousePressed():
    global N
    x[N], y[N] = mouseX, mouseY
    N += 1  
