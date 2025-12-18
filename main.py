from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("test")
root['background']='#3E4149'

#Set size of window
root.geometry("300x400")

saveButton=Button(root,text='Save',background='grey',highlightthickness=0)
editButton=Button(root,text='Edit',background='grey',highlightthickness=0)
loadButton=Button(root,text='Load',background='grey',highlightthickness=0)

tab1=Button(root,text='1',background='grey',highlightthickness=0)
tab2=Button(root,text='2',background='grey',highlightthickness=0)

tf=Text(root)
tf['background']='#3E4149'
tf['width']=50

# Place widgets in window (with pack function!)

editButton.grid(row=0,column=0)
saveButton.grid(row=0,column=1)
loadButton.grid(row=0,column=2)

tab1.grid(row=1,column=0)
tab2.grid(row=2,column=0)
tf.grid(row=3,column=1,rowspan=1,columnspan=1)



# red_button.pack()
# yellow_button.pack()
# green_button.pack()
# label.pack()
# tf.pack()
# Start the GUI event loop
root.mainloop()