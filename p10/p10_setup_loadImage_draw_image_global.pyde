# p10_setup_loadImage_draw_image_global
def setup():
    global imgBG, imgBird
    size(1180,590) 
    imgBG= loadImage('background.jpg')
    imgBird = loadImage('Bird.png')
def draw():
    global imgBG, imgBird
    image(imgBG, 0, 0)
    image(imgBird, mouseX-400, mouseY-300, 800,600)
