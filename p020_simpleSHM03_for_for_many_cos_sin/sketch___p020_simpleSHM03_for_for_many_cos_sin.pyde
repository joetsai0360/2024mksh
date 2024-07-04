# p020_simpleSHM03_for_for_many_cos_sin
def setup():
    size(300,300)
def draw():
    background(255)
    for x in range(0, 300, 20):
        for y in range(0, 300, 20):
            ellipse(x, y, 8, 8)
            r = 4
            a = frameCount*1
            ellipse(x+r*cos(a), y+r*sin(a), 3, 3)
