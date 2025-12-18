from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("test")
root['background']='#3E4149'

#Set size of window
root.geometry("600x600")

# Create buttons
yellow_button = Button(root, text="Yellow", background='yellow',highlightthickness=0)

green_button=Button(root,text="Green",background='green',highlightthickness=0)
red_button = Button(root, text="Red", background='red',highlightthickness=0)

lightButton=Button(root,text="what is light, but photons?",background='white')

#Add a label
label = Label(root, text="stop sign? what stop sign?")
label['background']='#3E4149'
label['fg']='white'

tf=Text(root)
tf['background']='#3E4149'
label['fg']='white'
tf['width']=50

# Place widgets in window (with pack function!)

lightButton.grid(row=2,column=0,padx=10)
red_button.grid(row=0,column=0,padx=20,pady=20)
yellow_button.grid(row=0,column=1,padx=20,pady=20)
green_button.grid(row=0,column=2,padx=20,pady=20)
label.grid(row=1,column=1,pady=10)
tf.grid(row=3,column=1)



# red_button.pack()
# yellow_button.pack()
# green_button.pack()
# label.pack()
# tf.pack()
# Start the GUI event loop
root.mainloop()