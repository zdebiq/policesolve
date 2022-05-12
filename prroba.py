import time
from tkinter import *
from tkinter import messagebox
 
 
root = Tk()
 
root.geometry("600x600")
  
root.title("Permutations:")
  
second=StringVar()
  
second.set("00")

print(second)
  
# Use of Entry class to take input from the user
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=second)

secondEntry.place(x=180,y=20)
  
  
def submit():

    temp = int(second.get())
    while temp >-1:

        secs = divmod(temp,60)

        second.set(secs)
  
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = Button(root, text='Set Time Countdown', bd='5',
             command= submit)
btn.place(x = 70,y = 120)
  
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()