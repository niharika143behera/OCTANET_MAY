from tkinter import *
import time
#-------------------------------------------------------

def bank():
    global acca
    accno = ["0001", "0002", "0003"]
    account = number.get()
    if account in accno:
        label.config(text="Registered User ")
        bank = {"0001": 10000, "0002": 5000, "0003": 700}
        balance = bank[account]
        acca = balance
    else:
        label.config(text="Non-Registered user")
    return int(acca)


def deposit():
    acca = bank()
    amo = float(amount.get())
    bal = acca + amo
    label3.config(text=("Net Balance", str(bal)))
    return bal

def withdrawn():
    acca = deposit()
    wd = float(withd.get())
    if acca > wd:
        bal = acca - wd
        label4.config(text=("Net Balance", str(bal)))
    else:
        label4.config(text="Insufficient Balance")
    return bal

def bal():
    acca = withdrawn()
    label5.config(text=("Net Balance", str(acca)))


def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
#----------------------------------------------------------------------------
root=Tk()
root.title("ATM MACHINE")
root.geometry("800x400")

number= StringVar()
amount=IntVar()
withd=IntVar()
acca=" "

localtime=time.asctime(time.localtime(time.time()))

lbinfo=Label(text="ATM MACHINE",fg="powder Blue",bg="black",bd=10,anchor="w")
lbinfo.place(x=300,y=0)
lbinfo= Label(text=localtime,fg="blue",bg="white",bd=5,anchor="w")
lbinfo.place(x=280,y=40)

lb1=Label(text="Enter the Account Number",bd=10)
lb1.place(x=0,y=80)
txt=Entry(textvariable=number,insertwidth=6,bd=10) #
txt.place(x=220,y=80)

label=Label(bd=10)
label.place(x=200,y=120)
submit=Button(padx=10,pady=4,bd=10,fg="blue",width=7,text="SUBMIT",command=bank)
submit.place(x=500,y=80)

lb1=Label(text="Enter the amount to be Deposited",bd=3)
lb1.place(x=0,y=160)
txt=Entry(textvariable=amount,bd=2,insertwidth=4,justify="right")
txt.place(x=220,y=160)

label3=Label(bd=10)
label3.place(x=200,y=180)
bdeposit=Button(padx=10,pady=4,bd=5,fg="blue",width=7,text="DEPOSIT",command=deposit)
bdeposit.place(x=500,y=140) # deposit

bw=Button(padx=10,pady=4,bd=5,fg="blue",width=7,text="WITHDRAW",command=withdrawn)
bw.place(x=500,y=200)

bbal=Button(padx=10,pady=4,bd=5,fg="blue",width=7,text="BALANCE",command=bal)
bbal.place(x=500,y=260)

breset=Button(padx=6,pady=3,text="RESET",command=reset)
breset.place(x=500,y=320)

bexit=Button(padx=6,pady=3,text="EXIT",command=root.destroy)
bexit.place(x=500,y=360)

lb1=Label(text="Enter the amount to be Withdrawn",bd=10)
lb1.place(x=0,y=220)
txt=Entry(textvariable=withd,bd=6,insertwidth=4,justify="right")
txt.place(x=220,y=220)
label4=Label()
label4.place(x=220,y=240)
label5 = Label(fg="white",bg='red')
label5.place(x=220,y=280)

root.mainloop()
