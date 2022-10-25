#attmpt 1:
import turtle as trtl
import pygame as py
import time
import keyboard

tr = trtl.Turtle()
wn = trtl.Screen()
note_list = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1']
wav_list = ["A1.wav", "B1.wav", "C1.wav", "D1.wav", "E1.wav", "F1.wav", "G1.wav"]

#create piano
wn.addshape("piano.gif")
tr.shape("piano.gif")

#initial test
wn.bgcolor('black')
wn.setup(width=800, height=600)


#note setup
py.mixer.init()
note_list = py.mixer.Sound(wav_list.pop())

a = py.mixer.Sound("A1.wav")
b = py.mixer.Sound("B1.wav")
c = py.mixer.Sound("C1.wav")
d = py.mixer.Sound("D1.wav")
e = py.mixer.Sound("E1.wav")
f = py.mixer.Sound("F1.wav")
g = py.mixer.Sound("G1.wav")


while True:
	if keyboard.is_pressed("a"):
		py.mixer.Sound.play(a)
		break

	if keyboard.is_pressed("b"):
		py.mixer.Sound.play(b)
		break

	if keyboard.is_pressed("c"):
		py.mixer.Sound.play(c)
		break

	if keyboard.is_pressed("d"):
		py.mixer.Sound.play(d)
		break

	if keyboard.is_pressed("e"):
		py.mixer.Sound.play(e)
		break

	if keyboard.is_pressed("f"):
		py.mixer.Sound.play(f)
		break

	if keyboard.is_pressed("g"):
		py.mixer.Sound.play(g)
		break




wn.mainloop()
wn.exitonclick()





#attempt 2:

'''Twinkle_List = ['A1','B1','C1','D1','E1','F1', 'G1']



from threading import Thread
import time
import pygame as pg

pg.mixer.init()
pg.init()


pg.mixer.set_num_channels(len(Twinkle_List))

def play_notes(notePath,duration):
	#make a pause
	time.sleep(duration)
	pg.mixer.Sound(notePath).play()
	#let the sound play
	time.sleep(duration)
	#see which note is playing
	print(notePath)

path  = 'Sounds/'

cnt =1	# A counter to delay once a line is finished

th = {}

for t in Twinkle_List:
	#arguments (path+'{}.wav'.format(t),0.3)
	th[t] = Thread(target = play_notes,args = (path+'{}.wav'.format(t),0.3))
	th[t].start()
	th[t].join()
	if cnt%7==0:
		print("---Long Pause---")
		time.sleep(1) # Let the sound play for the last note of each line
		
	cnt+=1
'''


