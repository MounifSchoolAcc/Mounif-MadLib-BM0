from tkinter import *
from tkmacosx import Button

import random

def editFile():
	
	with open("textFileOne.txt","r") as f:
		content=f.read()
		tf.insert('1.0',content)
def saveFile():
	
	with open("textFileOne.txt","w") as f:
		content=tf.get("1.0", 'end-1c')
		f.write(content)

def clearText():
	tf.delete('1.0','end')

root=Tk()
root.title='main'
root['background']='#3E4149'

tf=Text(root,borderwidth=0)
tf['background']='#3E4149'
tf['fg']='#FFFDD0'
tf['width']=25
tf['height']=15

clearButton=Button(
	root,
	text='clear text',
	activebackground='#FFFFFF',
	command=clearText)

clearButton['fg']='#FFFDD0'
clearButton['background']='#3E4149'


editButton=Button(
	root,
	text='edit file',
	activebackground='#FFFFFF',
	command=editFile)

editButton['fg']='#FFFDD0'
editButton['background']='#3E4149'


saveButton=Button(
	root,
	text='save file',
	activebackground='#FFFFFF',
	command=saveFile)

saveButton['background']='#3E4149'
saveButton['fg']='#FFFDD0'

tf.grid(column=1,row=0,rowspan=5,columnspan=5)
editButton.grid(column=0,row=0)
saveButton.grid(column=0,row=1)
clearButton.grid(column=0,row=2)

root.mainloop()