import pong
import cv2
import speech_recognition as sr

main_img = cv2.resize(cv2.imread('assets/main.png'), (400,400), interpolation= cv2.INTER_LINEAR)
about_img = cv2.resize(cv2.imread('assets/about.png'), (400,400), interpolation= cv2.INTER_LINEAR)
window_name = 'Pupil Pong'
cv2.imshow(window_name, main_img)
cv2.waitKey(1000)

def show_menu(image):
    cv2.destroyAllWindows()
    cv2.imshow(window_name, image)
    cv2.waitKey(1000)

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
        if "play" in ans:
            cv2.destroyAllWindows()
            print("Starting game")
            pong.main()
        elif "about" in ans:
            show_menu(about_img)
        elif "return" in ans:
            show_menu(main_img)
        elif "quit" in ans:
            exit()

def main():
    while True:
        menu_voice()
main()
