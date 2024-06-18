#!/usr/bin/env python3

"""
Skeleton Project: Rename Project
"""
import json
import tkinter
from tkinter import ttk
from tkinter import StringVar
from SkeletonProject import Config

###
# Read from the .uproject File
###
with open(Config.ProjectPath, "r") as f:
    uproject_json = json.load(f)

###
# Find the Project Module
###
project_modules = uproject_json.get("Modules", [])
for project_module in project_modules:
    if project_module.get("Type") == "Runtime":
        break

###
# Create the Window
###
window = tkinter.Tk()
window.title("Skeleton Project: Rename Project")
window.minsize(320, 100)
window.maxsize(320, 100)

###
# Create the "Project Name:" Label
###
project_label = ttk.Label(window, text="Project Name:", anchor="w")
project_label.pack(padx=5, pady=5, fill="x")


###
# Add the Text Entry Field
###
def on_enter_key(event):
    rename_project()


project_name = StringVar(value=project_module.get("Name"))
project_entry = ttk.Entry(window, textvariable=project_name)
project_entry.pack(padx=5, pady=5, fill="x")
project_entry.bind("<Return>", on_enter_key)
project_entry.focus_set()


###
# Rename Project Callback
###
def rename_project():
    ###
    # Update the Status Message
    ###
    status_label["text"] = "Renaming Project..."

    ###
    # Update the Project Name
    ###
    project_module["Name"] = project_name.get()

    # Save the .uproject File
    with open(Config.ProjectPath, "w") as f:
        json.dump(uproject_json, f, indent=4)

    ###
    # Update the Status Message
    ###
    status_label["text"] = "Finished; Enjoy!"


###
# Status Message
###
status_label = ttk.Label(window, anchor="w")
status_label.pack(side=tkinter.LEFT, padx=5, pady=5, fill="x")

###
# Add the "Rename Project" Button
###
save_button = ttk.Button(window, text="Rename Project", command=rename_project)
save_button.pack(side=tkinter.RIGHT, padx=5, pady=5)

###
# Run the App
###
window.mainloop()
