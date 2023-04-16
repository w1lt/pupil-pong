import cv2
from gaze_tracking import GazeTracking
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
import pygame
from pygame.locals import *
import pygame.freetype
import speech_recognition as sr
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

pointcounter = 0

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)
print('system font :', sysfont)

class Pong(object):
    def __init__(self, screensize):
        self.screensize = screensize
        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)

        self.radius = 8

        self.rect = pygame.Rect(self.centerx-self.radius, self.centery-self.radius, self.radius*2, self.radius*2)

        self.color = (255,255,255)

        self.direction = [1,1]
        #speed of ball
        self.speedx = 15
        self.speedy = 15

        self.hit_edge_left = False
        self.hit_edge_right = False

    def update(self, player_paddle, ai_paddle):

        global pointcounter
        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:
            self.direction[1] = 1
            self.hit_edge_top = True
        elif self.rect.bottom >= self.screensize[1]-1:
            self.direction[1] = -1
            self.hit_edge_bottom = True

        if self.rect.right >= self.screensize[0]-1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True

        if self.rect.colliderect(player_paddle.rect):
            self.direction[0] = -1
            pointcounter += 1
        if self.rect.colliderect(ai_paddle.rect):
            self.direction[0] = 1

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0,0,0), self.rect.center, self.radius, 1)

#creates the AI paddle
class AIPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = 5
        self.centery = int(screensize[1]*0.5)

        #ai paddle dimensions
        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5),      self.width, self.height)

        self.color = (255,255,255)
        #ai paddle speed
        self.speed = 18

    def update(self, pong):
        if pong.rect.top < self.rect.top:
            self.centery -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.centery += self.speed

        self.rect.center = (self.centerx, self.centery)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

#creates the player paddle
class PlayerPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = screensize[0]-5
        self.centery = int(screensize[1]*0.5)

        #player paddle dimensions
        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5),     self.width, self.height)

        self.color = (255,255,255)

        #player paddle speed
        self.speed = 30
        self.direction = 0

        self.hit_edge_top = False
        self.hit_edge_bottom = False

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1
        print(self.rect.bottom)
        print(f"center y is:{self.centery}")
        print(f"player bottom is {self.rect.bottom}")
        

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)


def main():

    pygame.init()

    global pointcounter

    screensize = (600,480)

    screen = pygame.display.set_mode(screensize)


    clock = pygame.time.Clock()

    pong = Pong(screensize)
    ai_paddle = AIPaddle(screensize)
    player_paddle = PlayerPaddle(screensize)

    running = True

    while running:
        ai_paddle.render(screen)
        player_paddle.render(screen)
        pong.render(screen)
        
            # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""
        clock.tick(64)

        if gaze.is_up():
            text = "looking up"
            if player_paddle.centery > 0:
                player_paddle.direction = -1
            else:
                player_paddle.direction = 0
        elif gaze.is_down():
            text = "looking down"
            if player_paddle.centery < player_paddle.screensize[1]:
                player_paddle.direction = 1
            else:
                player_paddle.direction = 0
        else:
            player_paddle.direction = 0
            #print("Looking down")

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False




        ai_paddle.update(pong)
        player_paddle.update()
        pong.update(player_paddle, ai_paddle)

        if pong.hit_edge_left:
            print ('You Won')
            running = False
        elif pong.hit_edge_right:
            print ('Your Score')
            print (pointcounter)
            running = False


        screen.fill((0,0,0))

        ai_paddle.render(screen)
        player_paddle.render(screen)
        pong.render(screen)

        pygame.display.flip()
        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        cv2.imshow("Demo", frame)
        img = font.render(f"Score: {str(pointcounter)}", True, (255, 255, 255))
        rect = img.get_rect()
        pygame.draw.rect(img, (0, 0, 0), rect, 1)
        screen.blit(img, (240, 22))
        pygame.display.update()

        if cv2.waitKey(1) == 27:
            break
        pygame.display.set_caption("Pupil Pong")
        ai_paddle.render(screen)
        player_paddle.render(screen)
        pong.render(screen)

   
    webcam.release()
    cv2.destroyAllWindows()

    pygame.quit()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1000, phrase_time_limit=4)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print("You said: {}.".format(query))
        return query

    except Exception as e:
        print("voice not recognized")  
