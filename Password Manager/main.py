from tkinter import *
from tkinter import messagebox
from generator import password_generate


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_generated_password():
    password_text.delete(0, END)
    generated_password = password_generate()
    password_text.insert(END, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email = email_username_input.get()
    password = password_text.get()
    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="Oopss", message="Please don't leave any fields empty")
    else:
        
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details enetered: \nEmail: {email}\nPassword: {password}\nIs it okay to save? ")
        
        if is_ok:
            with open("data.csv", mode="a") as input_data:
                input_data.write(f"{website}, {email}, {password}\n")
                website_input.delete(0, END)
                password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
image_content = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image_content)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", fg="black", bg="white", font=("Arial", 11))
website_label.grid(row=1, column=0)

website_input = Entry(width=45, fg="black", bg="white", highlightthickness=0)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:", fg="black", bg="white", font=("Arial", 11))
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=45, fg="black", bg="white", highlightthickness=0)
email_username_input.insert(0, "bright@gmail.com")
email_username_input.grid(row=2, column=1, columnspan=2)


password_label = Label(text="Password:", fg="black", bg="white", font=("Arial", 11))
password_label.grid(row=3, column=0)

password_text = Entry(width=25, fg="black", bg="white", highlightthickness=0)
password_text.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=15, fg="black", bg="white", highlightthickness=0, command=get_generated_password)
generate_password_button.grid(row=3, column=2)


add_button = Button(text="Add", width=42, fg="black", bg="white", highlightthickness=0, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)








window.mainloop()