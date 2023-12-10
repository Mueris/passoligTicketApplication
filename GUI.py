# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:29:13 2023

@author: musta
"""
from tkinter import * 
import time



# Create the main window
root =Tk()
root.title("Tkinter Example")
root.geometry("1000x600")

fr_userInfo=Frame(root,relief=RAISED,bg="lightblue",bd=2)
fr_content=Frame(root,relief=RAISED,bg='red',bd=2)
fr_securityNumber=Frame(fr_userInfo,relief=RAISED,bg="darkgreen",bd=2)

userNameField=Entry(fr_userInfo,width=30)
passwordField=Entry(fr_userInfo,width=30)
userNameLabel=Label(fr_userInfo,text="E-mail adresi:",fg='Blue',bg='lightblue')
passwordLabel=Label(fr_userInfo,text="Şifre:",fg='Blue',bg='lightblue')

userNameLabel.grid(pady=1,padx=5,sticky="w",row=0)
userNameField.grid(pady=2,padx=5,sticky="ew",row=1)
passwordLabel.grid(pady=1,padx=5,sticky="w",row=2)
passwordField.grid(pady=3,padx=5,sticky="ew",row=3)

secNumEnt=Entry(fr_securityNumber,width=10)
secLabel=Label(fr_securityNumber,text="Güvenlik Kodunu Giriniz",bg="darkgreen",fg="red")

secNumEnt.grid(pady=5,padx=5,sticky="w",row=1)
secLabel.grid(pady=2,padx=5,sticky="ew",row=0)

def on_button_click():

    fr_securityNumber.grid(pady=5,padx=5,sticky="we",row=7)

def on_btn_click():
    fr_securityNumber.place_forget()
    # fr_userInfo.place(x=350,y=100)
    
    
    
# Create a button and a label
applyButton = Button(fr_userInfo, text="ONAYLA", command=on_button_click)
secApplyBtn=Button(fr_securityNumber,text="Onayla",command=on_btn_click)
label = Label(fr_userInfo, text="Lütfen Bilgilerinizi Giriniz!",bg="lightblue")

# Pack the button and label
applyButton.grid(row=4,column=0,pady=5,padx=5,sticky="ew")
secApplyBtn.grid(row=4,column=0,pady=5,padx=5,sticky="ew")
label.grid(row=5,column=0,pady=5,padx=5,sticky="ew")

fr_userInfo.pack(side="left",fill="y")
#fr_userInfo.place(x=370,y=200)
#fr_content.grid(row=0,column=1,sticky="nsew")
# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
    
    

""""
window=Tk()
window.title("My app")
window.geometry("1000x600")

window.mainloop
fr_userInfo=Frame(window, relief=RAISED,bg="pink",bd=2)
usr=Label(window,text="sa")
usr.pack()
fr_userInfo.pack()
"""