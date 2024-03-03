# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:29:13 2023

@author: musta
"""
from tkinter import * 
import time
import passo

pas=passo()

email=""
password=""
security=""
tck=""
matchTime=""
# Create the main window
root =Tk()
root.title("Tkinter Example")
root.geometry("1000x600")

fr_userInfo=Frame(root,relief=RAISED,bg="lightblue",bd=2)
fr_content=Frame(root,relief=RAISED,bg='black',bd=2)
fr_securityNumber=Frame(fr_userInfo,relief=RAISED,bg="darkgreen",bd=2)

userNameField=Entry(fr_userInfo,width=30)
passwordField=Entry(fr_userInfo,width=30)
matchHourEnt=Entry(fr_userInfo,width=10)
tcEntry=Entry(fr_userInfo)

userNameLabel=Label(fr_userInfo,text="E-mail adresi:",fg='Blue',bg='lightblue')
passwordLabel=Label(fr_userInfo,text="Şifre:",fg='Blue',bg='lightblue')
matchTimeLabel=Label(fr_userInfo,text="Maç Saati: [SAAT]:[DAKİKA] şeklinde",fg='Blue',bg='lightblue')
labelSeperator=Label (fr_userInfo,text=":",fg='blue',bg='lightblue')
tcLabel=Label (fr_userInfo,text="TC Kimlik Numarası(opsiyonel)",fg='blue',bg='lightblue')


title= Label(fr_content,text="BİLET ALMA UYGULAMASINA HOŞ GELDİNİZ!",bg='black',fg='red',font=(25))
rules=Label(fr_content,text="Lütfen Bilgilerinizi doldurup giriş yapınız! Öncelikle mail ve şifre bilgilerinizi giriniz",bg='black',fg='white', fon =(11))
rules1=Label(fr_content,text="Ardından onaylaya basınız, ardından açılan passolig ekrandaki güvenlik kodunu girip onaylaya basınız",bg='black',fg='white', fon =(11))
rules2=Label(fr_content,text="GS KART ÖNCELİKLİ BİLET ALMAK İSTİYORSANIZ TC KİMLİK NUMARANIZI GİRİNİZ!",bg='black',fg='red', fon =(11))


userNameLabel.grid(pady=1,padx=5,sticky="w",row=0)
userNameField.grid(pady=2,padx=5,sticky="ew",row=1)
passwordLabel.grid(pady=1,padx=5,sticky="w",row=2)
passwordField.grid(pady=3,padx=5,sticky="ew",row=3)
matchTimeLabel.grid(pady=3,padx=5,sticky="ew",row=4)
matchHourEnt.grid(padx=5,row=5,sticky="w")
tcEntry.grid(padx=5,row=7,sticky="w")
tcLabel.grid(padx=5,row=6,sticky="we")


title.grid(pady=50,padx=200,sticky="ewns")
rules.grid(pady=1,padx=75,sticky="ewns")
rules1.grid(pady=10,padx=75,sticky="ewns")
rules2.grid(pady=1,padx=75,sticky="ewns")


secNumEnt=Entry(fr_securityNumber,width=10)
secLabel=Label(fr_securityNumber,text="Güvenlik Kodunu Giriniz",bg="darkgreen",fg="red")

secNumEnt.grid(pady=5,padx=5,sticky="w",row=1)
secLabel.grid(pady=2,padx=5,sticky="ew",row=0)

def on_button_click():
    pas.run()
    email=userNameField.get()
    password=passwordField.get()
    matchTime=matchHourEnt.get()
    fr_securityNumber.grid(pady=5,padx=5,sticky="we",row=10)
    
def on_btn_click():
    security=secNumEnt.get()
    tck=tcEntry.get()
    pas.runProgram(matchTime)
    # fr_userInfo.place(x=350,y=100)  
# Create a button and a label
applyButton = Button(fr_userInfo, text="ONAYLA", command=on_button_click)
secApplyBtn=Button(fr_securityNumber,text="Onayla",command=on_btn_click)
label = Label(fr_userInfo, text="Lütfen Bilgilerinizi Giriniz!",bg="lightblue")

# Pack the button and label
applyButton.grid(row=9,column=0,pady=5,padx=5,sticky="ew")
secApplyBtn.grid(row=4,column=0,pady=5,padx=5,sticky="ew")
label.grid(row=8,column=0,pady=5,padx=5,sticky="ew")

fr_userInfo.pack(side="left",fill="y")
fr_content.pack(expand='True',fill="both")
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