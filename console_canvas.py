#!/usr/bin/env python3
import sys
import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab

class ConsoleEditorApp:
    def __init__(self, root, text):
        self.root = root
        self.root.title("Console Editor with Canvas")

        # Text widget styled like console
        self.text_widget = tk.Text(
            root, 
            wrap="none", 
            bg="black", 
            fg="white", 
            insertbackground="white",  # cursor color
            font=("Courier", 14)
        )
        self.text_widget.pack(fill="both", expand=True)

        # Insert initial console text
        self.text_widget.insert("1.0", text)

        # Save button
        save_btn = tk.Button(root, text="Save as PNG", command=self.save_as_png)
        save_btn.pack()

    def save_as_png(self):
        # Get widget position
        x = self.text_widget.winfo_rootx()
        y = self.text_widget.winfo_rooty()
        w = x + self.text_widget.winfo_width()
        h = y + self.text_widget.winfo_height()

        # Screenshot only the text widget area
        img = ImageGrab.grab(bbox=(x, y, w, h))
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            img.save(filename)
            print(f"[+] Saved editable console screenshot as {filename}")


def main():
    print("Paste your console text below. Press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) when done:\n")
    text = sys.stdin.read()

    if not text.strip():
        print("[-] No input provided.")
        sys.exit(1)

    root = tk.Tk()
    app = ConsoleEditorApp(root, text)
    root.mainloop()


if __name__ == "__main__":
    main()
