### IITGN BTECH 2020 ###

### INTRODUCTION TO COMPUTING PROJECT ###

# Ronak Hingonia, Roll No. 20110170.
# Saksham Dhaania, Roll No. 20110179.
# Shail Prajapati, Roll No. 20110188.
# Tanmay Wagh, Roll No. 20110233.
# Tarun Yadav, Roll No. 20110215.



def Exit():
    exit()

def TakeID():
    i = id.get()
    try:
        f = open(i, 'r')
        CheckPIN()

    except IOError:                                                             # prompts user if a wrong ID is provided
        Label(root1, text="\nIT SEEMS LIKE YOU DON'T HAVE AN ACCOUNT.\nWOULD YOU LIKE TO CREATE A NEW ACCOUNT?").pack()
        Button(root1, text="YES", command=YesNewAccount).pack()
        Button(root1, text="NO", command=Exit).pack()

def CheckPIN():

    def ContCheckPIN():
        f = open(i, 'r')
        pin_ = int(f.readline())                                                # accessing the pre-stored PIN
        if int(pin.get()) != pin_:                                              # comparing the pre-stored and user provided PIN
            Label(root2, text="WRONG PIN!", fg="red").pack()
            Button(root2, text="RE-ENTER", command=CheckPIN)
            Button(root2, text="EXIT", command=Exit)
        else:
            DisplayOptions()
    
    i = id.get()
    root2 = Tk()
    root2.geometry("300x300")
    root2.title("ATM SIMULATOR")
    Label(root2, text="PLEASE PROVIDE THE FOUR DIGIT SECURITY PIN :").pack()
    pin = Entry(root2, show="*")                                                # taking PIN from user
    pin.pack()
    Button(root2, text="OK", command=ContCheckPIN).pack()
    root2.mainloop()


def YesNewAccount():
    def Destroy():
        root1.destroy()
    i = id.get()
    root1.geometry("360x422")
    root1.title("ATM SIMULATOR")
    f = open(i, 'w')                                                            # creating a new account file
    Label(root1, text="YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED.\n").pack()
    Label(root1, text="YOUR DEFAULT 4 DIGIT SECURITY PIN IS *0000*\nYOU CAN CHANGE IT LATER.").pack()
    Label(root1, text="YOU CAN DEPOSIT MONEY AFTER CHANGING THE SECURITY PIN", fg="red").pack()
    f.write("0000")                                                             # storing the PIN in the file
    f.write("\n")
    f.write("0")                                                                # initiating the account with zero funds
    Button(root1, text="OK", command=DisplayOptions).pack()
    Button(root1, text="CLOSE", command=Exit).pack()

def DisplayOptions():
    try:
        root1.destroy()
    except:
        pass
    root2 = Tk()
    root2.geometry("400x222")
    root2.title("ATM SIMULATOR")
    Label(root2, text="\nCHOOSE ONE OF THE OPTIONS BELOW:").pack()
    Button(root2, text="1. CHECK THE AVAILABLE BALANCE IN YOUR ACCOUNT.", command=CheckBalance).pack()
    Button(root2, text="2. CHANGE THE 4 DIGIT SECURITY PIN.", command=ChangePIN).pack()
    Button(root2, text="3. WITHDRAW MONEY FROM YOUR ACCOUNT.", command=Withdraw).pack()
    Button(root2, text="4. DEPOSIT MONEY INTO YOUR ACCOUNT.", command=Deposit).pack()
    Button(root2, text="5. EXIT!", command=Exit).pack()
    
    root2.mainloop()
        
def CheckBalance():

    def Destroy():
        root2.destroy()

    root2 = Tk()
    root2.geometry("400x200")
    root2.title("ATM SIMULATOR")
    i = id.get()
    f = open(i, 'r')
    f.seek(5)                                                               # directing the file handle to the string containing balance
    bal = int(f.read())                                                         # accessing the balance
    s = "THE AVAILABLE BALANCE IN YOUR ACCOUNT IS : " +str(bal)+"\n"
    Label(root2,text=s).pack()
    f.seek(0)
    Button(root2, text="GO BACK", command=Destroy).pack()
    Button(root2, text="CLOSE", command=Exit).pack
    
    root2.mainloop()

def ChangePIN():

    def Destroy():
        root2.destroy()

    def ContChangePIN1():

        def ContChangePIN2():
            f = open(i, 'r')
            f.seek(5)                                                      # directing the file handle to the string containing balance
            bal = int(f.read())                                                 # saving the available balance
            f.seek(0)                                                           # resetting the file handle
            f = open(i, 'w')
            f.write('')                                                         # erasing everything in the file
            f.write(npin.get())                                                 # storing the new PIN
            f.write("\n")
            f.write(str(bal))                                                   # storing the available balance
            f.close()
            Label(root2, text="THE SECURITY PIN HAS BEEN SUCCESSFULLY UPDATED!").pack()
            Button(root2, text="GO BACK", command=Destroy).pack()
            Button(root2, text="CLOSE", command=Exit).pack


        if int(pin.get()) != pin_:                                               # comparing the user provided PIN with pre-stored PIN 
            Label(root2, text="\nWRONG PIN!", fg="red").pack()
        else:
            Label(root2, text="\nENTER THE NEW PIN :").pack()
            npin = Entry(root2, show="*")                                           # storing the newly entered PIN
            npin.pack()
            Button(root2, text="OK", command=ContChangePIN2).pack()
        
    i = id.get()
    f = open(i, 'r')
    f.seek(0)
    pin_ = int(f.readline())                                                    # accessing the pre-stored PIN
    root2 = Tk()
    root2.geometry("400x400")
    root2.title("ATM SIMULATOR")
    Label(root2, text="PLEASE ENTER THE PREVIOUS PIN").pack()
    pin = Entry(root2, show="*")                                                # taking the old PIN for verification
    pin.pack()
    Button(root2, text="OK", command=ContChangePIN1).pack()
    
    
    root2.mainloop()


def Withdraw():

    def Destroy():
        root2.destroy()

    def ContWithdraw():
        if int(amt.get()) > bal:                               # comparing if the amount to be withdrawn exceeds the available balance
            Label(root2, text="\nINSUFFICIENT FUNDS!", fg="red").pack()
        else:
            nbal = bal - int(amt.get())                                         # reducing the amount withdrawn
            f = open(i, 'w')
            f.write('')                                                         # erasing everything in the file
            f.write(str(pin_))                                                  # storing the PIN
            f.write("\n")
            f.write(str(nbal))                                                  # storing the new balance
            Label(root2, text="MONEY HAS BEEN SUCCESSFULLY WITHDRAWN.").pack()
            Button(root2, text="GO BACK", command=Destroy).pack()
            Button(root2, text="CLOSE", command=Exit).pack()

    root2 = Tk()
    root2.geometry("400x300")
    root2.title("ATM SIMULATOR")
    i = id.get()
    f = open(i, 'r')
    f.seek(5)                                                   # directing the file handle to the string containing balance
    bal = int(f.read())                                         # accessing the balance
    f.seek(0)                                                   # resetting the file handle for future use
    pin_ = int(f.readline())                                    # accessing the pin
    s = "\nTHE AVAILABLE BALANCE IN YOUR ACCOUNT IS : " +str(bal)
    Label(root2, text=s).pack()
    Label(root2, text="\nENTER THE AMOUNT TO BE WITHDRAWN : ").pack()
    amt = Entry(root2)
    amt.pack()
    Button(root2, text="OK", command=ContWithdraw).pack()

    root2.mainloop()
    
def Deposit():

    def Destroy():
        root2.destroy()

    def ContDeposit():
            nbal = bal + int(amt.get())                                     # adding the amount deposited
            f = open(i, 'w')
            f.write('')                                                     # erasing everything in the file
            f.write(str(pin_))                                              # storing the PIN
            f.write("\n")
            f.write(str(nbal))                                              # storing the new balance
            Label(root2, text="MONEY HAS BEEN SUCCESSFULLY DEPOSITED.").pack()
            Button(root2, text="GO BACK", command=Destroy).pack()
            Button(root2, text="CLOSE", command=Exit).pack()

    root2 = Tk()
    root2.geometry("400x300")
    root2.title("ATM SIMULATOR")
    i = id.get()
    f = open(i, 'r')
    f.seek(5)                                                   # directing the file handle to the string containing balance
    bal = int(f.read())                                         # accessing the balance
    f.seek(0)                                                   # resetting the file handle for future use
    pin_ = int(f.readline())                                    # accessing the pin
    s = "\nTHE AVAILABLE BALANCE IN YOUR ACCOUNT IS : " +str(bal)
    Label(root2, text=s).pack()
    Label(root2, text="\nENTER THE AMOUNT TO BE DEPOSITED : ").pack()
    amt = Entry(root2)
    amt.pack()
    Button(root2, text="OK", command=ContDeposit).pack()
    root2.mainloop()


from tkinter import *
root1 = Tk()
root1.geometry("300x322")
root1.title("ATM SIMULATOR")
Label(root1, text=("WELCOME TO ATM SIMULATOR"), bg=("black"), fg=("white")).pack(fill=X)
Label(root1, text="PLEASE ENTER YOUR ID BELOW\n\nID:").pack(fill=X)
id = StringVar()
Entry(root1, textvariable=id).pack()
Button(root1, text="NEXT", command=TakeID).pack()
root1.mainloop()