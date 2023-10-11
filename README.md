# Unreal Engine 5: Skeleton Project

A fine-tuned, lightweight, bare minimum, UE5 project to be used as the template for new projects.

## Features

* Disabled all superfluous plugins except CLion integration.

## Bulk Plugin Manager

As a convenience over the built-in Plugin Browser, run the following to re-enable desired plugins in bulk. This requires `tkinter` which ships with python, and the `ttkwidgets` package.

```sh
pip install ttkwidgets
python PluginManager.py
```

## ... But Why?

Project loads in under 2 seconds on my machine. Iterative development at its finest.

Fewer dependencies also leads to fewer headaches when upgrading to newer engine versions.
