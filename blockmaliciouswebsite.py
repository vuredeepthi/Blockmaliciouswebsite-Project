import tkinter as tk
from tkinter import messagebox
import os

# Path to hosts file (Windows)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Redirect IP
redirect_ip = "127.0.0.1"

# Target websites
websites = [
    "badwebsite.com",
    "www.badwebsite.com"
]

def block_sites():
    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in websites:
                entry = f"{redirect_ip} {site}\n"
                if entry not in content:
                    file.write(entry)
        messagebox.showinfo("Success", "Blocked badwebsite.com")
    except PermissionError:
        messagebox.showerror("Error", "Run program as Administrator!")

def unblock_sites():
    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()
        with open(hosts_path, "w") as file:
            for line in lines:
                if not any(site in line for site in websites):
                    file.write(line)
        messagebox.showinfo("Success", "Unblocked badwebsite.com")
    except PermissionError:
        messagebox.showerror("Error", "Run program as Administrator!")

# ---------------------------
# GUI Setup
# ---------------------------
root = tk.Tk()
root.title("Website Blocker Tool")
root.geometry("350x200")

label = tk.Label(root, text="Block Malicious Website Project", font=("Arial", 12, "bold"))
label.pack(pady=10)

block_btn = tk.Button(root, text="Block badwebsite.com", width=25, command=block_sites)
block_btn.pack(pady=5)

unblock_btn = tk.Button(root, text="Unblock badwebsite.com", width=25, command=unblock_sites)
unblock_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", width=25, command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()