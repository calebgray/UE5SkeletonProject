#!/usr/bin/env python3

"""
Skeleton Project: Plugin Manager
"""
import json
import tkinter
from tkinter import ttk
from ttkwidgets import CheckboxTreeview
from SkeletonProject import Config

###
# Read the Plugins from the .uproject File
###
with open(Config.ProjectPath, "r") as f:
    uproject_json = json.load(f)

###
# Create the Window
###
window = tkinter.Tk()
window.title("Skeleton Project: Plugin Manager")
window.minsize(320, 480)

###
# Create the Checkbox Tree
###
tree = CheckboxTreeview(window)
tree.pack(expand=True, fill=tkinter.BOTH)

###
# Gather the Plugins
###
checkboxes = {}
plugins = uproject_json.get("Plugins", [])
for plugin in plugins:
    plugin_name = plugin.get("Name", "")
    checkboxes[plugin_name] = plugin.get("Enabled", False)

###
# Add the Checkboxes to the Tree
###
for plugin_name in sorted(checkboxes.keys(), reverse=True):
    enabled = checkboxes[plugin_name]
    tree.insert("", 0, iid=plugin_name, text=plugin_name, tags=("checked" if enabled else "unchecked"))

###
# Add the Select "All" Button
###
select_all_button = ttk.Button(window, text="All", command=tree.check_all)
select_all_button.pack(side=tkinter.LEFT, padx=5, pady=5)

###
# Add the Select "None" Button
###
deselect_all_button = ttk.Button(window, text="None", command=tree.uncheck_all)
deselect_all_button.pack(side=tkinter.LEFT, padx=0, pady=5)


###
# Save Button Callback
###
def save_plugins():
    # Update the Enabled/Disabled States of the Plugins
    for item in tree.get_children(""):
        checkboxes[item] = tree.tag_has("checked", item)

    # Modify the Original Plugins List
    for plugin in plugins:
        plugin_name = plugin.get("Name", "")
        plugin["Enabled"] = checkboxes[plugin_name]

    # Save the Updated Plugins to the .uproject File
    with open(Config.ProjectPath, "w") as f:
        json.dump(uproject_json, f, indent=4)


###
# Add the Save Button
###
save_button = ttk.Button(window, text="Save", command=save_plugins)
save_button.pack(side=tkinter.RIGHT, padx=5, pady=5)

###
# Run the App
###
window.mainloop()
