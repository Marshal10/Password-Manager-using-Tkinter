from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

web_input=Entry()
web_input.grid(column=1,row=1,pady=5,columnspan=2,sticky=W+E,padx=10)

email_lbl=Label(text="Email/Username:")
email_lbl.grid(column=0,row=2,pady=5)

email_input=Entry()
email_input.grid(column=1,row=2,pady=5,columnspan=2,sticky=W+E,padx=10)

pwd_lbl=Label(text="Password:")
pwd_lbl.grid(column=0,row=3,pady=5)

pwd_input=Entry(width=21)
pwd_input.grid(column=1,row=3,padx=10,pady=5,sticky=W+E) 

generate_btn=Button(text="Generate Password")
generate_btn.grid(column=2,row=3,padx=10,pady=5)

add_btn=Button(text="Add",width=36)
add_btn.grid(column=1,row=4,padx=10,columnspan=2,pady=5,sticky=W+E)

window.mainloop()