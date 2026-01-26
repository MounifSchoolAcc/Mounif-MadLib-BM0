from tkinter import *
from tkmacosx import Button

import random

def readFile():
	
	with open("demofile.txt","r") as f:
		content=f.read()
		print(content)

def writeFile():
	
	with open("demofile.txt","w") as f:
		f.write("text in txt file")

root=Tk()
root.title='test'
root['background']='#3E4149'

tf=Text(root)
tf['background']='#3E4149'
tf['width']=10
tf['height']=5

readButton=Button(root,text='read file',command=readFile)

writeButton=Button(root,text='write file',command=writeFile)



tf.grid(column=0,row=0)
readButton.grid(column=0,row=1)
writeButton.grid(column=0,row=2)

root.mainloop()