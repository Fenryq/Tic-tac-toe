from tkinter import *    
from tkinter import ttk
from tkinter import font as tkFont
import time

# create a tkinter window
root = Tk()     
root.geometry('490x550') 
helv36 = tkFont.Font(family='Helvetica', size=57, weight='bold')
helv35 = tkFont.Font(family='Helvetica', size=15, weight='bold')
helv34 = tkFont.Font(family='Helvetica', size=17, weight='bold')

calls_count = 0
after_id = True
result_nowin = None
result_wino = None
result_winx = None
clean = False
class ButtonCreator():
    

    def __init__(self, column, row):
        global calls_count
        calls_count = 1
        self.button_text = StringVar()
        self.button = Button(root, height= 1, width=3, bg='black',fg='white', command=self.ChangeText, text="")
        self.button.grid(column=column, row=row, sticky=E, padx=5, pady=5)
        self.button['font'] = helv36
        self.button['text'] = ""
        self.text = self.button['text']
       
        

    def ChangeText(self):
        global calls_count
        if calls_count==0 or calls_count % 2 == 0:
               self.button['text'] = 'X'
        elif calls_count % 2 == 1:
            self.button['text'] = 'O'
        calls_count += 1
        self.text = self.button['text']        
        
def engine(button_1, button_2, button_3, button_4, button_5, button_6, button_7,button_8, button_9):
    global after_id, result_nowin, result_wino, result_winx
    result_nowin = Label(root,text='No one win', font=helv34, bg='red')
    result_wino = Label(root, text='Win player O', font=helv34, bg='red')
    result_winx = Label(root, text='Win player X', font=helv34, bg='red')
    
 # Letter O
    if button_1.text == "O" and button_2.text == 'O' and button_3.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_7.text == "O" and button_8.text == 'O' and button_9.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_1.text == "O" and button_4.text == 'O' and button_7.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_3.text == "O" and button_6.text == 'O' and button_9.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_8.text == "O" and button_5.text == 'O' and button_2.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_4.text == "O" and button_5.text == 'O' and button_6.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_1.text == "O" and button_5.text == 'O' and button_9.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    elif button_3.text == "O" and button_5.text == 'O' and button_7.text == 'O':
        print("Winner O player")
        result_wino.grid(column=2,row=2)
        after_id=False
    #Letter X
    elif button_1.text == "X" and button_2.text == 'X' and button_3.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
        # Letter O
    elif button_7.text == "X" and button_8.text == 'X' and button_9.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    elif button_1.text == "X" and button_4.text == 'X' and button_7.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    elif button_3.text == "X" and button_6.text == 'X' and button_9.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    elif button_8.text == "X" and button_5.text == 'X' and button_2.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    elif button_4.text == "X" and button_5.text == 'X' and button_6.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    elif button_1.text == "X" and button_5.text == 'X' and button_9.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    elif button_3.text == "X" and button_5.text == 'X' and button_7.text == 'X':
        print("Winner X player")
        result_winx.grid(column=2,row=2)
        after_id=False
    if button_1.text != "" and button_2.text != "" and button_3.text != "" and button_4.text != "" and button_5.text != "" and button_6.text != "" and button_7.text != "" and button_8.text != "" and button_9.text != "":
        print("no one win")
        result_nowin.grid(column=2,row=2)
        after_id=False
def run_engine():
    engine(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9)
    global after_id
    if after_id:
        root.after(100, run_engine)



def clearFunc():
    global after_id, result_nowin, result_wino, result_winx, clean
    result_wino.destroy()
    result_winx.destroy()
    result_nowin.destroy()
    after_id=True
    clean=True
    button_1.button['text'] = ''
    button_2.button['text'] = ''
    button_3.button['text'] = ''
    button_4.button['text'] = ''
    button_5.button['text'] = ''
    button_6.button['text'] = ''
    button_7.button['text'] = ''
    button_8.button['text'] = ''
    button_9.button['text'] = ''
    button_1.text = ""
    button_2.text = ""
    button_3.text = ""
    button_4.text = ""
    button_5.text = ""
    button_6.text = ""
    button_7.text = ""
    button_8.text = ""
    button_9.text = ""
    root.after(1000, run_engine)



btn_text = StringVar()
button_1 = ButtonCreator(1,1)
button_2 = ButtonCreator(2,1)
button_3 = ButtonCreator(3,1)
button_4 = ButtonCreator(1,2)
button_5 = ButtonCreator(2,2)
button_6 = ButtonCreator(3,2)
button_7 = ButtonCreator(1,3)
button_8 = ButtonCreator(2,3)
button_9 = ButtonCreator(3,3)
again_button = Button(root, height= 1, width=12, bg='red',fg='white', command=clearFunc  , text="Again", font=helv35)
end_button = Button(root, height= 1, width=12, bg='red',fg='white', command=root.destroy, text="END", font=helv35)
again_button.grid(column=1, row=4, sticky=E, padx=5, pady=5)
end_button.grid(column=3, row=4, sticky=E, padx=5, pady=5)
root.after(1000, run_engine)
root.mainloop()


