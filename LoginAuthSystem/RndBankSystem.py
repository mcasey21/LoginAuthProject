import tkinter as tk
from CeaserCypherDict import encrypt_ceaser
import random as rnd

filename = "user_info.txt"


def SignUp():
    """ This function deals with the sign up button on the main screen,
        it gathers the username and password using .get() and then
        passes password into the encryption code, the username and
        encrypted code are then placed in the text file """
    
    username = entry_username.get()
    password = entry_password.get()

    encrypted_password = encrypt_ceaser(password)
    
    with open(filename, "a") as file:
        file.write(f"{username}:{encrypted_password}\n")
        print("Data written to file !!") # Debug Print


def Login():
    """ This func deals with the login button, it checks the text file
        for the username and password combo, if it exists it lets the
        user into the bank screen, otherwise it prompts the user to
        sign up """
    
    username = entry_username.get()
    password = entry_password.get()
    encrypted_password = encrypt_ceaser(password)

    info_found_flag = False

    login_info = f"{username}:{encrypted_password}"

    # Check for empty username or password
    if not username or not password:
        EmptyFieldsWarning()
    else:
        with open(filename, "r") as file:
            content = file.read()
            if login_info in content:
                print("Login info found!") # Debug print
                info_found_flag = True

    if info_found_flag == True:
        BankAccWindow(username)
    else:
        NoUserExists()


def EmptyFieldsWarning():
    """ Displays a warning window if username or password fields are empty """

    warning_window = tk.Toplevel(root)
    warning_window.title("Warning")
    warning_window.geometry("300x150")
    warning_window.resizable(False, False)

    message = tk.Label(warning_window, text="Username and Password cannot be empty!",
                       font=("Arial", 12), fg="red")
    message.pack(pady=30)
    close_button = tk.Button(warning_window, text="Close", command=warning_window.destroy)
    close_button.pack(pady=10)


def BankAccWindow(username):
    """ Bank account window, displays username and random account
        balance using rnd.randint() """

    # Making random account balance
    balance = rnd.randint(0, 1000000) / 100

    # Creating new window
    new_window = tk.Toplevel(root)
    new_window.title("RndBank")
    new_window.geometry("400x400")
    new_window.resizable(False, False)

    # New window content
    hello_label = tk.Label(new_window, text=f"Hello, {username}!", font=("Arial", 20))
    balance_label = tk.Label(new_window, text=f"Account Balance: {balance}", font=("Arial", 14))
    hello_label.pack(pady=20)
    balance_label.pack(pady=10)


def NoUserExists():
    """ If user dosent exist this displays, it includes a close button which
        destroys the current window """

    # Creating new window
    error_window = tk.Toplevel(root)
    error_window.title("User does not exist")
    error_window.geometry("300x200")
    error_window.resizable(False, False)

    # Error window content
    message = tk.Label(error_window, text=f"An account with this info does not exist, try signing up!")
    message.pack(pady=50)
    close_button = tk.Button(error_window, text="Close", command=error_window.destroy)
    close_button.pack(pady=10)

    
# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")
root.resizable(False, False)  # Disable resizing

# Configure widgets
page_title = tk.Label(root, text="Welcome to RndBank!", font=("Arial", 20))
label_username = tk.Label(root, text="Username:", font=("Arial", 14))
label_password = tk.Label(root, text="Password:", font=("Arial", 14))
entry_username = tk.Entry(root, font=("Arial", 14))
entry_password = tk.Entry(root, show="*", font=("Arial", 14))  # Show '*' for password input
button_login = tk.Button(root, text="Login", font=("Arial", 14), command=Login)
button_SignUp = tk.Button(root, text="Sign Up", font=("Arial", 14), command=SignUp)

# Configure grid
root.grid_rowconfigure(0, weight=1)  # Space above content
root.grid_rowconfigure(1, weight=0)  # No extra space between widgets
root.grid_rowconfigure(2, weight=0)  # No extra space between widgets
root.grid_rowconfigure(3, weight=1)  # Space below content
root.grid_columnconfigure(0, weight=1)  # Space on the left
root.grid_columnconfigure(1, weight=1)  # Center column
root.grid_columnconfigure(2, weight=1)  # Space on the right

# Place the widgets in the grid
page_title.grid(row=0, column=0, columnspan=3)
label_username.grid(row=1, column=0)
label_password.grid(row=2, column=0)
entry_username.grid(row=1, column=1)
entry_password.grid(row=2, column=1)
button_login.grid(row=4, column=1)
button_SignUp.grid(row=4, column=0)

# Start the Tkinter event loop
root.mainloop()