#!/usr/bin/env python3

"""
Unreal Engine 5: Plugin Manager
"""
import os
import json
import tkinter
from tkinter import ttk, messagebox
from ttkwidgets import CheckboxTreeview

script_directory = os.path.dirname(os.path.abspath(__file__))
uproject_files = [f for f in os.listdir(script_directory) if f.endswith('.uproject')]
if not uproject_files:
    messagebox.showerror("Error", "No .uproject found!")
    exit(1)

project_path = os.path.join(script_directory, uproject_files[0])

window = tkinter.Tk()
window.title("UE5 Plugin Manager")
window.minsize(320, 480)

tree = CheckboxTreeview(window)
tree.pack(expand=True, fill=tkinter.BOTH)

with open(project_path, "r") as f:
    uproject_json = json.load(f)

checkboxes = {}
plugins = uproject_json.get("Plugins", [])
for plugin in plugins:
    plugin_name = plugin.get("Name", "")
    checkboxes[plugin_name] = plugin.get("Enabled", False)

for plugin_name in sorted(checkboxes.keys(), reverse=True):
    enabled = checkboxes[plugin_name]
    tree.insert("", 0, iid=plugin_name, text=plugin_name, tags=("checked" if enabled else "unchecked"))

select_all_button = ttk.Button(window, text="All", command=tree.check_all)
select_all_button.pack(side=tkinter.LEFT, padx=5, pady=5)

deselect_all_button = ttk.Button(window, text="None", command=tree.uncheck_all)
deselect_all_button.pack(side=tkinter.LEFT, padx=0, pady=5)


def save_plugins():
    for item in tree.get_children(""):
        checkboxes[item] = tree.tag_has("checked", item)

    for plugin in plugins:
        plugin_name = plugin.get("Name", "")
        plugin["Enabled"] = checkboxes[plugin_name]

    with open(project_path, "w") as f:
        json.dump(uproject_json, f, indent=4)


save_button = ttk.Button(window, text="Save", command=save_plugins)
save_button.pack(side=tkinter.RIGHT, padx=5, pady=5)

window.mainloop()
