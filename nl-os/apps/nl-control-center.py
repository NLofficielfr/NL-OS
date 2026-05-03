#!/usr/bin/env python3
import tkinter as tk
import subprocess

def run(cmd):
    output.delete("1.0", tk.END)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output.insert(tk.END, result.stdout + result.stderr)
    except Exception as e:
        output.insert(tk.END, str(e))

root = tk.Tk()
root.title("NL Control Center")
root.geometry("760x520")
root.configure(bg="#08080c")

title = tk.Label(root, text="NL OS", fg="#f4e7b0", bg="#08080c", font=("Helvetica", 30, "bold"))
title.pack(pady=18)

subtitle = tk.Label(root, text="Luxury Linux Control Center", fg="#aaa", bg="#08080c", font=("Helvetica", 14))
subtitle.pack()

frame = tk.Frame(root, bg="#08080c")
frame.pack(pady=20)

buttons = [
    ("System Info", "uname -a && echo && free -h && echo && df -h /"),
    ("Performance Mode", "bash ~/nl-os/scripts/nl-performance.sh"),
    ("Clean Cache", "rm -rf ~/.cache/thumbnails/* ~/.cache/fontconfig/* 2>/dev/null; echo 'Cache cleaned.'"),
    ("Update System", "sudo apt update"),
]

for text, cmd in buttons:
    b = tk.Button(frame, text=text, command=lambda c=cmd: run(c), width=20, height=2, bg="#1d1d25", fg="white")
    b.pack(side=tk.LEFT, padx=8)

output = tk.Text(root, bg="#111118", fg="white", insertbackground="white", font=("Menlo", 11))
output.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()
