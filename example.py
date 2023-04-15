"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import pygame
import cv2
from gaze_tracking import GazeTracking

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
key = ""
while running:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "Looking right"
        key = "right"
    elif gaze.is_left():
        text = "Looking left"
        key = "left"
    elif gaze.is_up():
        text = "Looking up"
        key = "up"
    elif gaze.is_down():
        text = "Looking down"
        key = "down"
    elif gaze.is_center:
        text = "Looking center"
        key = "None"

        #Pygame:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 20)

    if key == "up":
        player_pos.y -= 150 * dt
        print("up")
    if key == "down":
        player_pos.y += 150 * dt
        print("down")
    if key == "left":
        player_pos.x -= 150 * dt
        print("left")
    if key == "right":
        player_pos.x += 150 * dt
        print("right")
    elif key == "None":
        print("not moving")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

        
        

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
pygame.quit()
