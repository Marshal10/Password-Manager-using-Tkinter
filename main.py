from tkinter import *
from tkinter import messagebox 
from password import Password
import pyperclip
import json

# ---------------------------- FILE HANDLING ------------------------------- #
def write_data(data):
    with open("data.json",mode="w") as file:
        json.dump(data,file,indent=4)
        
def read_data():
    with open("data.json",mode="r") as file:
        data=json.load(file)
    return data

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd=Password()
    if len(pwd_input.get())==0:
        pwd_input.insert(END,f"{pwd.password}")
    else:
        pwd_input.delete(0,'end')
        pwd_input.insert(END,f"{pwd.password}")
    pyperclip.copy(pwd.password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    website=web_input.get().title()
    email=email_input.get()
    password=pwd_input.get()
    new_data={
                website:{
                    "email":email,
                     "password":password
                }
            }
    
    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showerror("Oops","Please don't leave any of the fields empty")
        return
    
    confirm_save=messagebox.askokcancel(title=website,message=f"Email: {email}\nPassword: {password}\n is this ok?")
    if confirm_save:
        try:
            data=read_data()
        except FileNotFoundError:
            write_data(new_data)
        else:
            data.update(new_data)
            write_data(data)
        finally:
            web_input.delete(0,'end')
            pwd_input.delete(0,'end')
            web_input.focus()
            
# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search():
    website=web_input.get().title()
    
    if len(website)==0:
        messagebox.showerror("Oops","Please type-in something to search.")
        return
    try:
        data=read_data()
    except FileNotFoundError:
        messagebox.showinfo("Error","No Data File Found.")
        return
        
    try:
        messagebox.showinfo(website,f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
    except KeyError:
        messagebox.showinfo("Error",f"No details for {website} exists.")
    else:
        pass
    
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

web_lbl=Label(text="Website:")
web_lbl.grid(column=0,row=1,pady=5)

web_input=Entry(width=21)
web_input.focus()
web_input.grid(column=1,row=1,pady=5,sticky=W+E,padx=10)

email_lbl=Label(text="Email/Username:")
email_lbl.grid(column=0,row=2,pady=5)

email_input=Entry(width=35)
email_input.insert(END,'xyz@gmail.com')
email_input.grid(column=1,row=2,pady=5,columnspan=2,sticky=W+E,padx=10)

pwd_lbl=Label(text="Password:")
pwd_lbl.grid(column=0,row=3,pady=5)

pwd_input=Entry(width=21)
pwd_input.grid(column=1,row=3,padx=10,pady=5,sticky=W+E) 

generate_btn=Button(text="Generate Password",command=generate_pwd)
generate_btn.grid(column=2,row=3,padx=10,pady=5)

add_btn=Button(text="Add",width=36,command=save_pwd)
add_btn.grid(column=1,row=4,padx=10,columnspan=2,pady=5,sticky=W+E)

search_btn=Button(text="Search",command=search)
search_btn.grid(column=2,row=1,sticky=W+E,padx=10,pady=5)

window.mainloop()