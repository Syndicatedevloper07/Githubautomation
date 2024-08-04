# import pyautogui
# import time

# def type_command(command):
#     time.sleep(5)
#     pyautogui.write(command, interval=0.1)
#     time.sleep(2)
#     pyautogui.press('enter')
#     time.sleep(10)  # Adjust the sleep time if necessary to wait for the command to complete

# def main():
#     choice = input("Do you want to push the code to an existing repository or create a new one? (existing/new): ").strip().lower()
#     repo_link = input("Enter the repository link: ").strip()
#     commit_message = input("Enter the commit message: ").strip()

#     if choice == 'new':
#         commands = [
#             "git init",
#             "git add .",
#             f'git commit -m "{commit_message}"',
#             "git branch -M main",
#             f"git remote add origin {repo_link}",
#             "git push -u origin main"
#         ]
#     elif choice == 'existing':
#         commands = [
#             "git add .",
#             f'git commit -m "{commit_message}"',
#             f"git remote add origin {repo_link}",
#             "git push -u origin main"
#         ]
#     else:
#         print("Invalid choice. Please enter 'existing' or 'new'.")
#         return

#     for command in commands:
#         print(f"Executing command: {command}")
#         type_command(command)

# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

def type_command(command, status_label):
    status_label.config(text=f"Executing: {command}")
    root.update()  # Update the UI to show the current status
    time.sleep(5)
    pyautogui.write(command, interval=0.1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)  # Adjust the sleep time if necessary to wait for the command to complete
    status_label.config(text="Completed")

def run_commands(choice, repo_link, commit_message, status_label):
    if choice == 'new':
        commands = [
            "git init",
            "git add .",
            f'git commit -m "{commit_message}"',
            "git branch -M main",
            f"git remote add origin {repo_link}",
            "git push -u origin main"
        ]
    elif choice == 'existing':
        commands = [
            "git add .",
            f'git commit -m "{commit_message}"',
            f"git remote add origin {repo_link}",
            "git push -u origin main"
        ]
    else:
        messagebox.showerror("Invalid Choice", "Please enter 'existing' or 'new'.")
        return

    for command in commands:
        print(f"Executing command: {command}")
        type_command(command, status_label)

def submit():
    choice = var.get().strip().lower()
    repo_link = entry_repo.get().strip()
    commit_message = entry_commit.get().strip()

    if not choice or not repo_link or not commit_message:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    run_commands(choice, repo_link, commit_message, status_label)

# Set up the UI
root = tk.Tk()
root.title("GitHub Automation")


frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Do you want to push the code to an existing repository or create a new one? (existing/new)").pack()
var = tk.StringVar()
entry_choice = tk.Entry(frame, textvariable=var)
entry_choice.pack()

tk.Label(frame, text="Enter the repository link:").pack()
entry_repo = tk.Entry(frame, width=50)
entry_repo.pack()

tk.Label(frame, text="Enter the commit message:").pack()
entry_commit = tk.Entry(frame, width=50)
entry_commit.pack()

tk.Button(frame, text="Submit", command=submit).pack(pady=10)

status_label = tk.Label(frame, text="Status: Idle")
status_label.pack(pady=10)

root.mainloop()
