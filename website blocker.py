
#import library
from tkinter import *

#Creating GUI window
root = Tk()
root.geometry('1366x768')
root.resizable(1366,768)

#Heading
Label(root, text = 'WEBSITE BLOCKER' , font = 'arial 40 bold').pack()
Label(root,text = 'DHANUSH' , font = 'arial 30 bold').pack(side = BOTTOM)

#Path of the host file ang ip adsdress 
host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

#ENTER WEBSITE
Label(root, text= 'Enter Website :', font = 'arial 20 bold').place(x=370,y=180)
Websites = Text(root, font = 'arial 10', height ='2', width = '40', wrap = WORD,padx = 55, pady=5)
Websites.place(x = 600, y =180)

#Block function
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

block_btn = Button(root, text = 'BLOCK' , font = 'arial 15 bold', command = Blocker, width = 6 , bg = 'Red', activebackground = 'sky blue')
block_btn.place(x = 730, y =280)
root.mainloop
    
