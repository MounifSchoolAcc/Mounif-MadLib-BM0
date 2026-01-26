from tkinter import *
from tkmacosx import Button

import random

def b1Trig():
	L1.config(text='button one pressed')

def b2Trig():
	L2.config(text='button two pressed')

def b3Trig():
	L3.config(text='button three pressed')

def rand():
	ls=[B1,B2,B3]
	index=random.randint(0,2)
	if index==1:
		B1.config(text='random')
		L1.config(text='random')
	elif index==2:
		B2.config(text='random')
		L2.config(text='random')
	elif index==3:
		B3.config(text='random')
		L3.config(text='random')

root=Tk()
root.title='test'
root['background']='#3E4149'

B1=Button(root,text='b1',command=b1Trig)
B2=Button(root,text='b2',command=b2Trig)
B3=Button(root,text='b3',command=b3Trig)

L1=Label(root,text='L1')
L2=Label(root,text='L2')
L3=Label(root,text='L3')

randomB=Button(root,text='select random',command=rand)

B1.grid(column=0,row=0)
B2.grid(column=0,row=1)
B3.grid(column=0,row=2)

L1.grid(column=2,row=0)
L2.grid(column=2,row=1)
L3.grid(column=2,row=2)

randomB.grid(column=1,row=3)

root.mainloop()