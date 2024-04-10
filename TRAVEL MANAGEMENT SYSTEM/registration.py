from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import re  # Import regular expression module
import json
from travel import Travel

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080")

        pil_image = Image.open(r"D:\projects\TRAVEL MANAGEMENT SYSTEM\Travel-the-world-wallpaper-1920x1080.png")
        pil_image = pil_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Convert the PIL image to Tkinter PhotoImage
        self.background_image = ImageTk.PhotoImage(pil_image)

        # Create a label with the background image
        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

        self.username_var = StringVar()
        self.password_var = StringVar()

        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the center coordinates for the widgets
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Calculate the width of the widgets
        widget_width = 200  # Adjust as needed

        # Calculate the height of the widgets
        widget_height = 30  # Adjust as needed

        # Calculate the vertical spacing between widgets
        vertical_spacing = 70  # Adjust as needed

        # Username Label and Entry
        Label(root, text="Username:", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width - 30, y=center_y - widget_height - vertical_spacing)
        Entry(root, textvariable=self.username_var, width=40, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x - 30, y=center_y - widget_height - vertical_spacing)

        # Password Label and Entry
        Label(root, text="Password:", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width - 30, y=center_y - vertical_spacing)
        Entry(root, textvariable=self.password_var, show="*", width=40, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x - 30, y=center_y - vertical_spacing)

        # Login Button
        Button(root, text="Login", command=self.login, padx=18, bd=7, width=11, height=1, font=('Arial', 14, 'bold')).place(x=center_x - widget_width - 50, y=center_y)

        # Signup Button
        Button(root, text="Signup", command=self.signup, padx=18, bd=7, width=11, height=1, font=('Arial', 14, 'bold')).place(x=center_x + 50, y=center_y)

    def login(self):
        # Check if the username and password are empty
        if self.username_var.get() == "" or self.password_var.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter username and password.")
        else:
            # Check if the entered username and password match any registered user
            username = self.username_var.get()
            password = self.password_var.get()
            if self.authenticate(username, password):
                tkinter.messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
                # Open the Travel class window after successful login
                root = Tk()
                app = Travel(root)
                root.mainloop()
            else:
                tkinter.messagebox.showerror("Login Failed", "Invalid username or password.")

    def authenticate(self, username, password):
        # Load registered users from file
        registered_users = self.load_registered_users()

        # Check if the username and password match any registered user
        for user in registered_users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def load_registered_users(self):
        try:
            with open("registered_users.json", "r") as file:
                registered_users = json.load(file)
        except FileNotFoundError:
            registered_users = []
        return registered_users

    def save_registered_users(self, registered_users):
        with open("registered_users.json", "w") as file:
            json.dump(registered_users, file)

    def signup(self):
        # Close the login window
        self.root.destroy()

        # Open the registration window
        root = Tk()
        app = RegistrationPage(root, self)
        root.mainloop()

class RegistrationPage:
    def __init__(self, root, login_page):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1920x1080")
        self.login_page = login_page

        pil_image = Image.open(r"D:\projects\TRAVEL MANAGEMENT SYSTEM\Travel-Download-Free-Images-HD.jpg")
        pil_image = pil_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Convert the PIL image to Tkinter PhotoImage
        self.background_image = ImageTk.PhotoImage(pil_image)

        # Create a label with the background image
        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

        self.name_var = StringVar()
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()

        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the center coordinates for the widgets
        center_x = screen_width // 2
        center_y = screen_height // 2

        # Calculate the width of the widgets
        widget_width = 200  # Adjust as needed

        # Calculate the height of the widgets
        widget_height =30  # Adjust as needed

        # Calculate the vertical spacing between widgets
        vertical_spacing = 20  # Adjust as needed

        # Labels and Entry widgets
        Label(root, text="Name:         ", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width, y=center_y - widget_height - vertical_spacing)
        Entry(root, textvariable=self.name_var, width=50, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x, y=center_y - widget_height - vertical_spacing)

        Label(root, text="Username: ", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width, y=center_y - vertical_spacing)
        Entry(root, textvariable=self.username_var, width=50, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x, y=center_y - vertical_spacing)

        Label(root, text="Password: ", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width, y=center_y + 10)
        Entry(root, textvariable=self.password_var, show="*", width=50, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x, y=center_y + 10)

        Label(root, text="Email ID:     ", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width, y=center_y + 40)
        Entry(root, textvariable=self.email_var, width=50, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x, y=center_y + 40)

        Label(root, text="Address:    ", font=('Arial', 12, 'bold'), bd=7).place(x=center_x - widget_width, y=center_y + 70)
        Entry(root, textvariable=self.address_var, width=50, bd=7, font=('arial', 11, 'bold'), justify=RIGHT).place(x=center_x, y=center_y + 70)

        # Button
        Button(root, text="Register", command=self.register, padx=18, bd=7, width=30, height=1, font=('Arial', 14, 'bold')).place(x=center_x - widget_width // 2, y=center_y + 150)

    def validate_username(self, username):
        # Validate username using regular expression
        # It should contain at least one alphabet and one digit
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        return bool(re.match(pattern, username))

    def register(self):
        # Check if any field is empty
        if (self.name_var.get() == "" or self.username_var.get() == "" or
            self.password_var.get() == "" or self.email_var.get() == "" or
            self.address_var.get() == ""):
            tkinter.messagebox.showerror("Error", "Please fill all details.")
            return

        # Validate username
        if not self.validate_username(self.username_var.get()):
            tkinter.messagebox.showerror("Error", "Username must contain at least one alphabet and one digit. Example: username123")
            return

        # Proceed with registration
        name = self.name_var.get()
        username = self.username_var.get()
        password = self.password_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        # Load registered users
        registered_users = self.login_page.load_registered_users()

        # Check if username already exists
        for user in registered_users:
            if user['username'] == username:
                tkinter.messagebox.showerror("Error", "Username already exists.")
                return

        # Store registration data in a dictionary
        user_data = {'username': username, 'password': password, 'name': name, 'email': email, 'address': address}

        # Add user data to the list of registered users
        registered_users.append(user_data)

        # Save registered users to file
        self.login_page.save_registered_users(registered_users)

        # Display registration success message
        tkinter.messagebox.showinfo("Registration", "Registration Successful!")

        # Close the registration window
        self.root.destroy()

        # Open the login window
        root = Tk()
        app = LoginPage(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
