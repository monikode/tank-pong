# https://youtu.be/3DeW-7vbc50
#https://www.youtube.com/watch?v=3DeW-7vbc50

#key pressed
# https://nerdparadise.com/programming/pygame/part6
#shoot in any direction
# pygame.mouse.get_pos()
import pygame, math, random

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
screen_width = 850
screen_height = 550
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

rot = 0
rot_speed = 2

class Tank1: #classe que movimenta o tanque
    def __init__(self, color, x, y, dx_sq1, dy_sq1, speed,screen_width,screen_height,lim_tanks_board):
        self.rect = pygame.Rect(x,y,dx_sq1, dy_sq1)
        self.color = color
        self.direction = ''
        self.speed = speed

    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed
        

    def moveDirection(self, direction):
        if direction == 'E':
            self.rect.x = self.rect.x+self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.x > screen_width - dx_sq1 * 2:
              self.rect.x = screen_width - dx_sq1 * 2
          
        if direction == 'W':
            self.rect.x = self.rect.x-self.speed
	    #Check that you are not going too far (off the screen)
            if self.rect.x < dx_sq1:
                self.rect.x = dx_sq1
                
        if direction == 'N':
            self.rect.y = self.rect.y-self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.y < lim_tanks_board + dx_sq1 * 0.5:
                self.rect.y = lim_tanks_board + dx_sq1 * 0.5
                
        if direction == 'S':
            self.rect.y = self.rect.y+self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.y > screen_height - dy_sq1 * 2.5:
                self.rect.y = screen_height - dy_sq1 * 2.5

    def collided(self, other_rect):
        #Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Tank2: #classe que movimenta o tanque
    def __init__(self, color, x, y, dx_sq2, dy_sq2, speed,screen_width,screen_height,lim_tanks_board):
        self.rect = pygame.Rect(x,y,dx_sq2, dy_sq2)
        self.color = color
        self.direction = ''
        self.speed = speed

    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed
        

    def moveDirection(self, direction):
        if direction == 'E':
            self.rect.x = self.rect.x+self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.x > screen_width - dx_sq2 * 2:
              self.rect.x = screen_width - dx_sq2 * 2
          
        if direction == 'W':
            self.rect.x = self.rect.x-self.speed
	    #Check that you are not going too far (off the screen)
            if self.rect.x < dx_sq2:
                self.rect.x = dx_sq2
                
        if direction == 'N':
            self.rect.y = self.rect.y-self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.y < lim_tanks_board + dx_sq2 * 0.5:
                self.rect.y = lim_tanks_board + dx_sq2 * 0.5
                
        if direction == 'S':
            self.rect.y = self.rect.y+self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.y > screen_height - dy_sq2 * 2.5:
                self.rect.y = screen_height - dy_sq2 * 2.5


    def collided(self, other_rect):
        #Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)        


#Inheritance
class Bullet(Tank1): #classe que gerencia os tiros
    def __init__(self, color, x, y, width, height, speed, targetx,targety):
        super().__init__(color, x, y, width, height, speed)
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        print('Angle in degrees:', int(angle*180/math.pi))
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y
    #Override
    def move(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


lim_tanks_board = 50

#Build Tank1 (https://pygame.readthedocs.io/en/latest/rect/rect.html)
dx_sq1 = 20
dy_sq1 = 20
x_sq1 = 2 * dx_sq1 #dx + borda
y_sq1 = screen_height // 2
speed = 10
sq1 = Tank1(green,x_sq1,y_sq1,dx_sq1,dy_sq1, speed,screen_width,screen_height,lim_tanks_board)

#Build Tank2 (https://pygame.readthedocs.io/en/latest/rect/rect.html)
dx_sq2 = 20
dy_sq2 = 20
x_sq2 = screen_width - 3 * dx_sq2 #dx + borda
y_sq2 = screen_height // 2
speed = 10
sq2 = Tank1(blue,x_sq2,y_sq2,dx_sq2,dy_sq2, speed,screen_width,screen_height,lim_tanks_board)

bullets = []
enemies = []

#Main program loop
done = False
while not done:
    #Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key) #Print value of key press
            if event.key == pygame.K_f: #32: #press f to tank1 shoots
                #Fire a bullet
                spawnx1 = (sq1.rect.x) + (sq1.rect.width - dy_sq1 * 0.5)
                b1 = Tank1(white, spawnx1,sq1.rect.y, 5,5, 15,screen_width,screen_height,lim_tanks_board)
                b1.direction = 'E'
                bullets.append(b1)

            if event.key == pygame.K_c: #32: #press f to tank2 shoots
                #Fire a bullet
                spawnx2 = (sq2.rect.x) + (sq2.rect.width - dy_sq2 * 0.5)
                b2 = Tank2(white, spawnx2,sq2.rect.y, 5,5, 10,screen_width,screen_height,lim_tanks_board)
                b2.direction = 'W'
                bullets.append(b2)                

    #Handle held down keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        sq1.moveDirection('N')
    if pressed[pygame.K_LEFT]:
        sq1.moveDirection('W')
    if pressed[pygame.K_DOWN]:
        sq1.moveDirection('S')
    if pressed[pygame.K_RIGHT]:
        sq1.moveDirection('E')

    pressed2 = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        sq2.moveDirection('N')
    if pressed[pygame.K_a]:
        sq2.moveDirection('W')
    if pressed[pygame.K_s]:
        sq2.moveDirection('S')
    if pressed[pygame.K_d]:
        sq2.moveDirection('E')
        
    #Update game objects
    for b in bullets:
        b.move()
    for e in enemies:
        e.move()

    surface.fill(red) #fill surface with red

    # Drawing the boards
    # pygame.draw.line(screen, colour, (startX, startY), (endX, endY), thickness) https://bournetocode.com/projects/9-CS-pyGame/pages/1_Lesson.html
    # Horizontal boards
    pygame.draw.line(surface, yellow, [0, lim_tanks_board], [0, screen_height], dx_sq1 * 2)
    pygame.draw.line(surface, yellow, [screen_width, lim_tanks_board], [screen_width, screen_height], dx_sq1 * 2)
    # Vertical boards
    pygame.draw.line(surface, yellow, [0, lim_tanks_board],[screen_width, lim_tanks_board], dx_sq1)
    pygame.draw.line(surface, yellow, [0, screen_height],[screen_width, screen_height], dx_sq1 * 3)
    
    #All the drawing
    
    for b in bullets:
        b.draw(surface)
    for e in enemies:
        e.draw(surface)
    sq1.draw(surface)
    sq2.draw(surface)
    pygame.display.flip()
    pygame.event.get()
    clock.tick(50) #30 FPS
pygame.quit()
exit()
