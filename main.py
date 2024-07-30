import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pytz
from datetime import datetime


# Window
root = tk.Tk()
root.title("Nicho's Note Generator")
root.geometry("800x400")


# Program
def make_note():
    current_time = cst_entry.get()
    note_content = note_text.get(
        "1.0", tk.END
    ).strip()  # Get the content of the big textbox
    agent_tier = tier_combobox.get()
    user = user_entry.get()
    company = company_entry.get()

    # Generate the formatted note string
    note_string = (
        f"{current_time} / CCI / {note_content} / {user} / {agent_tier} / {company}"
    )

    # Clear the big textbox and insert the formatted note string
    note_text.delete("1.0", tk.END)
    note_text.insert(tk.END, note_string + "\n")


# Get the current CST time
def get_cst_time():
    cst = pytz.timezone("US/Central")
    cst_time = datetime.now(cst)
    return cst_time.strftime("%m-%d-%Y / %I:%M %p CST")


def refresh_time():
    cst_entry.delete(0, tk.END)  # Clear the current entry
    cst_entry.insert(0, get_cst_time())  # Insert the current CST time


def on_tier_change(event):
    selected_tier = tier_combobox.get()


def restart_program():
    refresh_time()
    note_text.delete("1.0", tk.END)


def exit_program(event=None):
    root.quit()


root.bind("<Control-w>", exit_program)
# ------ UI -----------------

cst_label = tk.Label(root, text="Current Time", width=20)
cst_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

user_label = tk.Label(root, text="User", width=20)
user_label.grid(column=1, row=0, padx=10, pady=10, sticky="w")

tier_label = tk.Label(root, text="Agent Tier", width=20)
tier_label.grid(column=2, row=0, padx=10, pady=10, sticky="w")

company_label = tk.Label(root, text="Company", width=20)
company_label.grid(column=3, row=0, padx=10, pady=10, sticky="w")

# ------ Text Box -------------
cst_entry = tk.Entry(root, width=20)
cst_entry.grid(column=0, row=1, padx=10, pady=10, sticky="w")

user_entry = tk.Entry(root, width=20)
user_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
user_entry.insert(0, "Csiqueiros")

# Create a Combobox for Agent Tier
tier_combobox = ttk.Combobox(root, values=["T1", "T2"], width=20)
tier_combobox.grid(column=2, row=1, padx=10, pady=10, sticky="w")
tier_combobox.bind("<<ComboboxSelected>>", on_tier_change)  # Bind the selection event
tier_combobox.set("T1")

company_entry = tk.Entry(root, width=20)
company_entry.grid(column=3, row=1, padx=10, pady=10, sticky="w")
company_entry.insert(0, "Hum")

note_text = tk.Text(root, width=80, height=10)
note_text.grid(column=0, row=3, columnspan=4, padx=10, pady=10)

cst_entry.insert(0, get_cst_time())

# ------ Button ---------------
generate_button = tk.Button(root, text="Generate Note", command=make_note)
generate_button.grid(column=0, row=4, columnspan=4, padx=10, pady=10)

refresh_button = tk.Button(root, text="Refresh Time", command=refresh_time)
refresh_button.grid(column=0, row=2, columnspan=4, padx=10, pady=10)

restart_button = tk.Button(root, text="Restart", command=restart_program)
restart_button.grid(column=5, row=5, padx=10, pady=10, sticky="e")

note_text.focus_set()

# End program
root.mainloop()
