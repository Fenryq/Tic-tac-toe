from tkinter import *    
from tkinter import ttk
from tkinter import font as tkFont


# create a tkinter window
root = Tk()     
root.geometry('480x510') 
helv36 = tkFont.Font(family='Helvetica', size=57, weight='bold')
 


class ButtonCreator():
    
    def __init__(self, column, row):
        self.button = Button(root, height= 1, width=3, bg='black',fg='white', command=self.ChangeText, text="")
        self.button.grid(column=column, row=row, sticky=E, padx=5, pady=5)
        self.button['font'] = helv36
        

    def ChangeText(self):
        self.button['text'] = 'X'
    
        
        
btn_text = StringVar()
button_1 = ButtonCreator(1,1)
button_2 = ButtonCreator(1,2)
button_3 = ButtonCreator(1,3)
button_4 = ButtonCreator(2,1)
button_5 = ButtonCreator(2,2)
button_6 = ButtonCreator(2,3)
button_7 = ButtonCreator(3,1)
button_8 = ButtonCreator(3,2)
button_9 = ButtonCreator(3,3)





root.mainloop()