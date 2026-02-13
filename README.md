# File-Rename-Script

A Python utility script that cleans up your messy folders by renaming files to a simple, numbered format (e.g., `ss1.png`, `ss2.png`).

## ✨ Key Features
* **Bulk Renaming:** transform "Screenshot 2023-10-27..." into `ss1.png`.
* **Smart Numbering:** Automatically detects existing files! If you already have `ss1` through `ss5`, the script detects this and starts naming the new files `ss6`.

## ⚙️ Configuration (Required)

Before running the script, you **must** tell it which folder to clean.

1. Open `renamer.py` in your text editor.
2. Replace the path with the location of your folder.

```python
# Example for Windows:
folder_path = r"C:\Users\YourName\Pictures\Screenshots"
