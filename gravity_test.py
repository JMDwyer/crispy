import sys, pygame
pygame.init()

size = width, height = 800, 640
speed = [1, 1]
black = 0, 0, 0
gravity = 0.2

screen = pygame.display.set_mode(size)

#image_file = os.path.expanduser("~/pybin/pygame_examples/data/ball.png")
ball = pygame.Surface([15,15])
ball.fill((255,255,255))
ballrect = ball.get_rect()

def clip(val, minval, maxval):
    return min(max(val, minval), maxval)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    speed[1] += gravity

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        
    ballrect.left = clip(ballrect.left, 0, width)
    ballrect.right = clip(ballrect.right, 0, width)        
    ballrect.top = clip(ballrect.top, 0, height)
    ballrect.bottom = clip(ballrect.bottom, 0, height)
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

