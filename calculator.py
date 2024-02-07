# import tkinter

# window =tkinter.Tk()

# window.mainloop()
from tkinter import Tk 
import tkinter

original = Tk()
original.title("**** CALCULATOR****")
original.geometry('400x400+100+100')
original.resizable(False,False)
original.iconbitmap(r'car_4.ico')
# original.state('zoomed')
# original.attributes('apha', 0.5)

original['bg']="Green"
label_widget=tkinter.Label(original,text="**** Calculations ****  \n")
label_widget.pack()

txt_first = tkinter.Entry(original)
txt_first.place(x=150,y=80)
label_first_name=tkinter.Label(original,text="First Number")
label_first_name.place(x=40,y=80)

txt_second =tkinter.Entry(original)
txt_second.place(x=150,y=150)
label_second_name=tkinter.Label(original,text="Second Number")
label_second_name.place(x=40,y=150)

txt_operator =tkinter.Entry(original)
txt_operator.place(x=100,y=180)

label_results=tkinter.Label(original,text="0")
label_results.place(x=150,y=250)

def result_button():
    a = int(txt_first.get())
    b= int(txt_second.get())
    c= txt_operator.get()
    ans= 0
    if c== "+":
        ans= a+b
    elif c== "-":
       ans= a-b
    elif c== "/":
       ans= a/b
    elif c=="*":
        ans=a*b
    else:
        print("The Operator is not part")

     
    label_results.config(text=ans)

result_button=tkinter.Button(original,text="Results", command=result_button)
result_button.place(x=150,y=220)



original.mainloop()
