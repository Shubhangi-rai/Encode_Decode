#import libraries
from tkinter import*
import base64

#initialize Window
root = Tk()               #initialized tkinter
root.geometry('500x300')  #set width and height of the window
root.resizable(0,0)       #set fixed size of window
root.title("Message Encode and Decode") #set title of window

Label(root, text ='ENCODE DECODE', font = 'Courier 20 bold').pack()

Text = StringVar() #variable stores the message to encode and decode
private_key = StringVar() #variable store the private key used to encode and decode
mode = StringVar()  # is used to select that is either encoding or decoding
Result = StringVar() #store the result

#function to encode
def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
#function to decode
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)
#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

#function to exit window
def Exit():
    root.destroy()
#function to reset window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
#label and buttons
Label(root, font= 'Courier 12 bold', text='Message').place(x= 60,y=60)
Entry(root, font = 'Courier 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'Courier 12 bold', text ='Key').place(x=60, y = 90)
Entry(root, font = 'Courier 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'Courier 12 bold', text ='Mode(e-encode,d-decode)').place(x=60, y = 120)
Entry(root, font = 'Courier 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'Courier 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

Button(root, font = 'Courier 10 bold', text = 'RESULT'  ,padx =2,bg ='lightGreen' ,command = Mode).place(x=60, y = 150)

Button(root, font = 'Courier 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'lightblue', padx=2).place(x=80, y = 190)

Button(root, font = 'Courier 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed3', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()

    
