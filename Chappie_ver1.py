from gtts import gTTS
import sys
from time import *
import pygame
import RPi.GPIO as GPIO  
from time import sleep
from random import *

d = [4, 5, 6, 7]
t = [1, 2, 3]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

ser = GPIO.PWM(12, 50)   
ser2 = GPIO.PWM(11, 50)   

GPIO.output(13, True)
GPIO.output(15, True)

ser.start(0)    
ser2.start(0)  

first = "Chappie has been activated"
language = "en"
output = gTTS(text = first, lang = language, slow = False)
output.save("output.mp3")

# os.system("start output.mp3")

pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()

chappie = "Chappie"

print("="*19)
print("  Talk to Chappie  ")
print("="*19)

while True:
    class mode():
        def __init__(self):
            pass
        def sleep_mode(self, mode):
            tt3 = "Yes... Bye bye I have to sleep"
            language = "en"
            output = gTTS(text = tt3, lang = language, slow = False)
            output.save("sleep.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("sleep.mp3")
            pygame.mixer.music.play()
            clock = pygame.time.Clock()

            while pygame.mixer.music.get_busy():
                clock.tick(30)
            pygame.mixer.quit()
            print("{} : Chappie is in sleeping!~".format(chappie))
            GPIO.output(13, False)
            GPIO.output(15, False)
            ser.ChangeDutyCycle(7)
            ser2.ChangeDutyCycle(8)

        def active_mode(self, mode):
            tt5 = "I want to play!"
            language = "en"
            output = gTTS(text = tt5, lang = language, slow = False)
            output.save("active.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("active.mp3")
            pygame.mixer.music.play()
            clock = pygame.time.Clock()

            while pygame.mixer.music.get_busy():
                clock.tick(30)
            pygame.mixer.quit()
            print("{} : Chappie is activing".format(chappie))
            GPIO.output(13, True)
            GPIO.output(15, True)
            pygame.mixer.init()
            pygame.mixer.music.load("Donny.wav")
            pygame.mixer.music.play()

            a = [7, 8, 9, 10, 11, 12,13, 14, 15]
            b = choice(a)
            while b:

                b -= 1

                degree = choice(d)
                time = choice(t)
                ser.ChangeDutyCycle(degree)
                if degree == 5:
                    degree2 = 10
                elif degree == 4:
                	degree2 = 11
                elif degree == 6:
                    degree2 = 9
                elif degree == 7:
                    degree2 = 8
                ser2.ChangeDutyCycle(degree2)
                sleep(time)

                if b <= 0:
                    # clock = pygame.time.Clock()
                    # while pygame.mixer.music.get_busy():
                    #     clock.tick(30)
                    # pygame.mixer.quit()    	
                    pygame.mixer.music.stop()
                    tt5 = "I want to rest now...."
                    language = "en"
                    output = gTTS(text = tt5, lang = language, slow = False)
                    output.save("active.mp3")
                    pygame.mixer.init()
                    pygame.mixer.music.load("active.mp3")
                    pygame.mixer.music.play()
                    clock = pygame.time.Clock()

                    while pygame.mixer.music.get_busy():
                        clock.tick(30)
                    pygame.mixer.quit()
                    GPIO.output(13, True)
                    GPIO.output(15, True)

                    break
            
    degree = choice(d)
    time = choice(t)
    ser.ChangeDutyCycle(degree)
    if degree == 5:
        degree2 = 10

    elif degree == 6:
        degree2 = 9
    elif degree == 4:
    	degree2 = 11

    elif degree == 7:
        degree2 = 8

    ser2.ChangeDutyCycle(degree2)
    sleep(time)

    question = raw_input(" : ")
    if question == "who are you?":
        tt = "I am Chappie."
        language = "en"
        output = gTTS(text = tt, lang = language, slow = False)
        output.save("myname.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("myname.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()

    elif question == "who is your maker?":
        tt1 = "My maker is Jeong Seo Jin"
        language = "en"
        output = gTTS(text = tt1, lang = language, slow = False)
        output.save("maker.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("maker.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()

    elif question == "shutdown system":
        tt2 = "Chappie has been unactivated"
        language = "en"
        output = gTTS(text = tt2, lang = language, slow = False)
        output.save("shutdown.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("shutdown.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()
        GPIO.output(13, False)
        GPIO.output(15, False)
        ser.ChangeDutyCycle(7)
        ser2.ChangeDutyCycle(8)
        sys.exit()

    elif question == "do you think I'm handsome?":
    	t0 = "Umm.... I don't know"
        tt7 = "I will tell you that you are a little handsome"
        handsome = "You are so handsome"
        answer = [t0, tt7, handsome]
        tex = choice(answer)
        language = "en"
        output = gTTS(text = tex, lang = language, slow = False)
        output.save("handsome.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("handsome.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()
        GPIO.output(13, True)
        GPIO.output(15, True)

    elif question == "are you sleepy?":
    	true = "sleep"
    	false = "nope"
    	tf = [true, false]
    	truth = choice(tf)
    	if truth == "sleep":
            sl = mode()
            sl.sleep_mode("sleep mode")
        elif truth == "nope":
            tt18 = "No, I'm not sleep"
            language = "en"
            output = gTTS(text = tt18, lang = language, slow = False)
            output.save("nopesleep.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("nopesleep.mp3")
            pygame.mixer.music.play()
            clock = pygame.time.Clock()

            while pygame.mixer.music.get_busy():
                clock.tick(30)
            pygame.mixer.quit()
            GPIO.output(13, True)
            GPIO.output(15, True)        	

    elif question == "wake up" :
        tt6 = "Oh, Ok    Ok"
        language = "en"
        output = gTTS(text = tt6, lang = language, slow = False)
        output.save("w.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("w.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()
        GPIO.output(13, True)
        GPIO.output(15, True)

    elif question == "do you want to play?":
    	play = [1, 2]
    	pl = choice(play)
    	if pl == 1:
            ac = mode()
            ac.active_mode("active_mode")

        elif pl == 2:
            tt11 = "No, I don't want to play"
            language = "en"
            output = gTTS(text = tt11, lang = language, slow = False)
            output.save("unactive.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("unactive.mp3")
            pygame.mixer.music.play()
            clock = pygame.time.Clock()

            while pygame.mixer.music.get_busy():
                clock.tick(30)
            pygame.mixer.quit()
            GPIO.output(13, True)
            GPIO.output(15, True)

    elif question == "turn on music":
        tt16 = "Turn on music"
        language = "en"
        output = gTTS(text = tt16, lang = language, slow = False)
        output.save("mus.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("mus.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()
        GPIO.output(13, True)
        GPIO.output(15, True)

        # music_cond = input("If you want to stop to listen music => [stop] : ")

        pygame.mixer.init()
        pygame.mixer.music.load("Donny.wav")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        print("="*58)
        ques = raw_input("   If you want to stop to listen music => [stop] : ")
        print("="*58)
        if ques == "stop":
        	pygame.mixer.music.stop()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()

    elif question == "guitar music":
    	music_question = raw_input("Write music name : ")
        tt9 = "Turn on {}".format(music_question)
        language = "en"
        output = gTTS(text = tt9, lang = language, slow = False)
        output.save("gu.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("gu.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()
        GPIO.output(13, True)
        GPIO.output(15, True)

        # music_cond = input("If you want to stop to listen music => [stop] : ")

        pygame.mixer.init()
        pygame.mixer.music.load("{}.mp3".format(music_question))
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        print("="*58)
        ques = raw_input("   If you want to stop to listen music => [stop] : ")
        print("="*58)
        if ques == "stop":
        	pygame.mixer.music.stop()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()


    elif question == "I'm boring":
        tt12 = "Shall we turn on music?"
        language = "en"
        output = gTTS(text = tt12, lang = language, slow = False)
        output.save("shall.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("shall.mp3")
        pygame.mixer.music.play()
        clock = pygame.time.Clock()

        while pygame.mixer.music.get_busy():
            clock.tick(30)
        pygame.mixer.quit()
        GPIO.output(13, True)
        GPIO.output(15, True)
        shall = raw_input("Shall we turn on music? [ yes | no ] : ")

        guitar_musics = ["Sweden", "Time", "Deathbed", "No time to die", "A thousand years"]

        if shall == "yes":
            topic = raw_input("Topic : ")
            if topic == "asmr":
                tt13 = "Turn on rain sound"
                language = "en"
                output = gTTS(text = tt13, lang = language, slow = False)
                output.save("asmr.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("asmr.mp3")
                pygame.mixer.music.play()
                clock = pygame.time.Clock()       		
                while pygame.mixer.music.get_busy():
                    clock.tick(30)
                pygame.mixer.quit()

                GPIO.output(13, True)
                GPIO.output(15, True)
                pygame.mixer.init()
                pygame.mixer.music.load("rainasmr.mp3")
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                print("="*58)
                ques = raw_input("   If you want to listen next music => [stop] : ")
                print("="*58)
                if ques == "stop":
                    pygame.mixer.music.stop()

                while pygame.mixer.music.get_busy():
                    clock.tick(30)
                pygame.mixer.quit()

            elif topic == "guitar":
                tt15 = "Turn on Guitar musics"
                language = "en"
                output = gTTS(text = tt15, lang = language, slow = False)
                output.save("guitars.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("guitars.mp3")
                pygame.mixer.music.play()
                clock = pygame.time.Clock()       		
                while pygame.mixer.music.get_busy():
                    clock.tick(30)
                pygame.mixer.quit()

            	for i in guitar_musics:
   
                    GPIO.output(13, True)
                    GPIO.output(15, True)
                    pygame.mixer.init()
                    pygame.mixer.music.load("{}.mp3".format(i))
                    pygame.mixer.music.play()
                    clock = pygame.time.Clock()
                    print("="*58)
                    ques = raw_input("[Enter => next song] [stop => stop] : ")
                    print("="*58)
                    if ques == "stop":
                        pygame.mixer.music.stop()
                        break

                    elif ques == "":
                    	pygame.mixer.music.stop()
                    	
                    else:
                    	print("{} can't understand...".format(chappie))

                    while pygame.mixer.music.get_busy():
                        clock.tick(30)
                    pygame.mixer.quit()

            elif topic =="funny song":
                tt8 = "Turn on music"
                language = "en"
                output = gTTS(text = tt8, lang = language, slow = False)
                output.save("mus.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("mus.mp3")
                pygame.mixer.music.play()
                clock = pygame.time.Clock()

                while pygame.mixer.music.get_busy():
                    clock.tick(30)
                pygame.mixer.quit()
                GPIO.output(13, True)
                GPIO.output(15, True)

        # music_cond = input("If you want to stop to listen music => [stop] : ")

                pygame.mixer.init()
                pygame.mixer.music.load("Donny.wav")
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
                print("="*58)
                ques = raw_input("   If you want to stop to listen music => [stop] : ")
                print("="*58)
                if ques == "stop":
                   	pygame.mixer.music.stop()
   
                while pygame.mixer.music.get_busy():
                    clock.tick(30)
                pygame.mixer.quit()        	


        elif shall == "no":
            tt14 = "Will I joke for you?"
            language = "en"
            output = gTTS(text = tt14, lang = language, slow = False)
            output.save("ok.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("ok.mp3")
            pygame.mixer.music.play()
            clock = pygame.time.Clock()
  
            while pygame.mixer.music.get_busy():
                clock.tick(30)
            pygame.mixer.quit()
            GPIO.output(13, True)
            GPIO.output(15, True)

            print("Will I joke for you? [ yes | no ]")
            joke = raw_input(" : ")
            if joke == "yes":
            	pass
            elif joke == "no":
                tt14 = "Will I joke for you?"
                language = "en"
                output = gTTS(text = tt14, lang = language, slow = False)
                output.save("ok.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load("ok.mp3")
                pygame.mixer.music.play()
                clock = pygame.time.Clock()
  
                while pygame.mixer.music.get_busy():
                    clock.tick(30)
                pygame.mixer.quit()
                GPIO.output(13, True)
                GPIO.output(15, True)
            


        else:
        	print("{} can't understand".format(chappie))
    else:
        print("{} : I can't understand...".format(chappie))


ser.stop()
ser2.stop()
GPIO.cleanup()
GPIO.output(13, False)
GPIO.output(15, False)