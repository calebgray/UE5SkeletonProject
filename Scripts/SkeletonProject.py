#!/usr/bin/env python3

"""
Unreal Engine 5: Rename Project
"""
import os
from tkinter import messagebox

script_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
uproject_files = [f for f in os.listdir(script_directory) if f.endswith('.uproject')]
if not uproject_files:
    messagebox.showerror("Error", "No .uproject found!")
    exit(1)


# Export Config
class Config:
    ProjectPath = os.path.join(script_directory, uproject_files[0])
