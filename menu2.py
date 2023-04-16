import pong
import cv2
import speech_recognition as sr
gamestart = False
# path
# path
import cv2
  
# path
path = "assets/main.png"
image = cv2.imread(path)
window_name = 'image'
cv2.imshow(window_name, image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
  

def show_menu(image):
     cv2.imshow(window_name, image)

  
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
def menu_voice():
        ans = takecommand()
        if "play" in ans:
            gamestart = True
            cv2.destroyAllWindows()
            pong.main()
            print("starting game")
        elif "about" in ans:
            cv2.destroyAllWindows()
            path = "assets/about.png"
            image = cv2.imread(path)
            window_name = 'image'
            cv2.imshow(window_name, image)
            cv2.waitKey(1000)
        elif "return" in ans:
            cv2.destroyAllWindows()
            path = "assets/main.png"
            image = cv2.imread(path)
            window_name = 'image'
            cv2.imshow(window_name, image)
            cv2.waitKey(1000)
        elif "quit" in ans:
            gamestart = True
            print("quitting")
            cv2.destroyAllWindows()
while gamestart == False:
    menu_voice()
