#!/bin/bash

echo "======================================"
echo "        NLOS ALPHA 3 VISUAL PACK"
echo "======================================"

mkdir -p "$HOME/.nlos/apps"
mkdir -p "$HOME/.nlos/assets"
mkdir -p "$HOME/.config/autostart"
mkdir -p "$HOME/Desktop"

cat > "$HOME/.nlos/apps/nlos-dashboard.py" <<'PY'
#!/usr/bin/env python3
import tkinter as tk
import subprocess
import time

def run(cmd):
    subprocess.Popen(cmd, shell=True)

root = tk.Tk()
root.title("NLOS Dashboard")
root.geometry("1100x680")
root.configure(bg="#edf8fb")

top = tk.Frame(root, bg="#edf8fb")
top.pack(fill="x", padx=30, pady=24)

title = tk.Label(top, text="NLOS", bg="#edf8fb", fg="#14202a", font=("Helvetica", 44, "bold"))
title.pack(side="left")

clock = tk.Label(top, text="", bg="#edf8fb", fg="#526773", font=("Helvetica", 15))
clock.pack(side="right")

subtitle = tk.Label(root, text="Liquid Linux Experience · Alpha 3", bg="#edf8fb", fg="#647782", font=("Helvetica", 18))
subtitle.pack(anchor="w", padx=34)

main = tk.Frame(root, bg="#edf8fb")
main.pack(fill="both", expand=True, padx=28, pady=24)

left = tk.Frame(main, bg="#f9fdff", highlightbackground="#d8e9ef", highlightthickness=1)
left.place(x=0, y=0, width=310, height=470)

center = tk.Frame(main, bg="#ffffff", highlightbackground="#d8e9ef", highlightthickness=1)
center.place(x=335, y=0, width=430, height=470)

right = tk.Frame(main, bg="#f9fdff", highlightbackground="#d8e9ef", highlightthickness=1)
right.place(x=790, y=0, width=280, height=470)

tk.Label(left, text="Bonjour,", bg="#f9fdff", fg="#6b7a84", font=("Helvetica", 15)).pack(anchor="w", padx=24, pady=(28, 0))
tk.Label(left, text="NL User", bg="#f9fdff", fg="#14202a", font=("Helvetica", 28, "bold")).pack(anchor="w", padx=24)
tk.Label(left, text="Session Live · NLOS Alpha 3", bg="#f9fdff", fg="#647782", font=("Helvetica", 13)).pack(anchor="w", padx=24, pady=(0, 26))

tk.Label(left, text="Apps rapides", bg="#f9fdff", fg="#14202a", font=("Helvetica", 18, "bold")).pack(anchor="w", padx=24)

apps = [
    ("Fichiers", "exo-open --launch FileManager"),
    ("Terminal", "xfce4-terminal"),
    ("Internet", "firefox-esr"),
    ("Réglages", "xfce4-settings-manager"),
    ("Performance", "xfce4-terminal -e nl-performance"),
]

for name, cmd in apps:
    tk.Button(left, text=name, command=lambda c=cmd: run(c), bg="white", fg="#14202a",
              relief="flat", font=("Helvetica", 13), width=22, height=2).pack(pady=6, padx=24)

tk.Label(center, text="NLOS", bg="#ffffff", fg="#14202a", font=("Helvetica", 64, "bold")).pack(pady=(55, 0))
tk.Label(center, text="Designed to feel calm, clear and premium.", bg="#ffffff", fg="#71828d", font=("Helvetica", 15)).pack(pady=12)

search = tk.Entry(center, bg="#f2f8fb", fg="#14202a", relief="flat", font=("Helvetica", 15))
search.pack(padx=42, pady=22, fill="x", ipady=12)
search.insert(0, "  Rechercher dans NLOS")

row = tk.Frame(center, bg="#ffffff")
row.pack(pady=18)

for text in ["Optimiser", "Nettoyer", "Analyser"]:
    tk.Button(row, text=text, bg="#eef7fb", fg="#14202a", relief="flat",
              font=("Helvetica", 12), width=11, height=2).pack(side="left", padx=7)

tk.Label(right, text="Centre de contrôle", bg="#f9fdff", fg="#14202a", font=("Helvetica", 18, "bold")).pack(anchor="w", padx=22, pady=(28, 18))

controls = [
    "Wi-Fi actif",
    "Mode clair",
    "Session Live",
    "Interface Alpha",
    "NLOS Shield prêt"
]

for c in controls:
    tk.Label(right, text="✓ " + c, bg="#f9fdff", fg="#253744", font=("Helvetica", 13)).pack(anchor="w", padx=24, pady=8)

dock = tk.Frame(root, bg="#f9fdff", highlightbackground="#d8e9ef", highlightthickness=1)
dock.place(relx=0.5, rely=0.93, anchor="center", width=520, height=74)

dock_items = [
    ("N", "python3 ~/.nlos/apps/nlos-dashboard.py"),
    ("⌂", "exo-open --launch FileManager"),
    (">", "xfce4-terminal"),
    ("◎", "firefox-esr"),
    ("⚙", "xfce4-settings-manager")
]

for label, cmd in dock_items:
    tk.Button(dock, text=label, command=lambda c=cmd: run(c), bg="white", fg="#14202a",
              relief="flat", font=("Helvetica", 20, "bold"), width=4, height=2).pack(side="left", padx=14, pady=8)

def update_time():
    clock.config(text=time.strftime("%a %d %b  %H:%M"))
    root.after(1000, update_time)

update_time()
root.mainloop()
PY

chmod +x "$HOME/.nlos/apps/nlos-dashboard.py"

cat > "$HOME/Desktop/NLOS Dashboard.desktop" <<EOF2
[Desktop Entry]
Type=Application
Name=NLOS Dashboard
Exec=python3 $HOME/.nlos/apps/nlos-dashboard.py
Icon=preferences-system
Terminal=false
Categories=Utility;
EOF2

chmod +x "$HOME/Desktop/NLOS Dashboard.desktop"

cat > "$HOME/.config/autostart/nlos-dashboard.desktop" <<EOF2
[Desktop Entry]
Type=Application
Name=NLOS Dashboard
Exec=python3 $HOME/.nlos/apps/nlos-dashboard.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
EOF2

cat > "$HOME/.config/gtk-3.0.css" <<'CSS'
* {
  font-family: Sans;
}

window,
dialog,
.background {
  background-color: #edf8fb;
  color: #14202a;
}

button {
  background-image: none;
  background-color: rgba(255,255,255,0.95);
  color: #14202a;
  border-radius: 18px;
  border: 1px solid rgba(190,215,226,0.8);
  padding: 8px 12px;
}

button:hover {
  background-color: #e8f6fb;
}

entry {
  background-color: rgba(255,255,255,0.95);
  color: #14202a;
  border-radius: 16px;
  border: 1px solid rgba(190,215,226,0.8);
  padding: 8px;
}
CSS

python3 "$HOME/.nlos/apps/nlos-dashboard.py" &

echo "NLOS Alpha 3 Visual Pack installé."
