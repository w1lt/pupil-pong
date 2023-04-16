import pong
import cv2
import speech_recognition as sr

main_img = cv2.resize(cv2.imread('assets/main.png'), (500,500), interpolation= cv2.INTER_LINEAR)
about_img = cv2.resize(cv2.imread('assets/about.png'), (500,500), interpolation= cv2.INTER_LINEAR)
window_name = 'Pupil Pong'

def show_menu(image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1000, phrase_time_limit=4)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print("You said: {}.".format(query))
        return query
    except Exception as e:
        print("Voice not recognized")  

def menu_voice():
        ans = takecommand()
        if "start" in ans:
            cv2.destroyAllWindows()
            pong.main()
            print("Starting game")
        elif "help" in ans:
            show_menu(about_img)
            cv2.destroyAllWindows()
        elif "return" in ans:
            show_menu(main_img)
            cv2.destroyAllWindows()
        elif "quit" in ans:
            print("Quitting")
            cv2.destroyAllWindows()

def main():
    show_menu(main_img)
    while True:
        menu_voice()
main()
