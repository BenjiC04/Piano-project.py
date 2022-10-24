import turtle as trtl
import winsound
import pygame as py
tr = trtl.Turtle()
wn = trtl.Screen()
'''wn.setup(400, 400)'''

#create piano
wn.addshape("piano.gif")
tr.shape("piano.gif")

#import notes
wn.bgcolor('black')
wn.setup(width=800, height=600)
def play():
    winsound.PlaySound('G1.wav', winsound.SND_ASYNC)

wn.listen()
wn.onkeypress(play, 'space')

trtl.done()


#correlate keys to sounds




wn.mainloop()
wn.exitonclick()




'''Twinkle_List = ['A1','B1','C1','D1','E1','F1', 'G1']



from threading import Thread
import time
import pygame as pg

pg.mixer.init()
pg.init()


pg.mixer.set_num_channels(len(Twinkle_List))

def play_notes(notePath,duration):
	time.sleep(duration) # make a pause 
	pg.mixer.Sound(notePath).play()
	time.sleep(duration) # Let the sound play 
	print(notePath) # To see which note is now playing

path  = 'Sounds/'

cnt =1	# A counter to delay once a line is finished as there
# are 6 total lines

th = {}

for t in Twinkle_List:
	th[t] = Thread(target = play_notes,args = (path+'{}.wav'.format(t),0.3))
	# These are arguments (path+'{}.wav'.format(t),0.3)
	# Lets start the thread
	th[t].start()
	th[t].join()
	if cnt%7==0:
		print("---Long Pause---")
		time.sleep(1) # Let the sound play for the last note of each line
		
	cnt+=1'''



