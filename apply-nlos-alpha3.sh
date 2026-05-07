#!/bin/bash
echo "NLOS Alpha 3 Visual Pack"
echo "Installation rapide..."

mkdir -p "$HOME/.nlos/apps" "$HOME/.nlos/assets" "$HOME/Desktop"

cat > "$HOME/.nlos/apps/nlos-dashboard.py" <<'PY'
#!/usr/bin/env python3
import tkinter as tk, time, subprocess, os

def run(cmd):
    subprocess.Popen(cmd, shell=True)

root = tk.Tk()
root.title("NLOS Dashboard")
root.geometry("1000x620")
root.configure(bg="#eef8fb")

tk.Label(root, text="NLOS", bg="#eef8fb", fg="#14202a", font=("Helvetica", 54, "bold")).pack(pady=30)
tk.Label(root, text="Liquid Linux Experience · Alpha 3", bg="#eef8fb", fg="#647782", font=("Helvetica", 18)).pack()

frame = tk.Frame(root, bg="#eef8fb")
frame.pack(pady=40)

apps = [
    ("Fichiers", "exo-open --launch FileManager"),
    ("Terminal", "xfce4-terminal"),
    ("Navigateur", "firefox-esr"),
    ("Réglages", "xfce4-settings-manager"),
    ("Performance", "xfce4-terminal -e nl-performance"),
]

for name, cmd in apps:
    tk.Button(frame, text=name, command=lambda c=cmd: run(c), width=16, height=3,
              bg="white", fg="#14202a", relief="flat", font=("Helvetica", 13)).pack(side="left", padx=10)

tk.Label(root, text="Centre de contrôle NLOS", bg="#eef8fb", fg="#14202a", font=("Helvetica", 24, "bold")).pack(pady=20)
tk.Label(root, text="Wi-Fi actif · Mode clair · Session Live · Interface Alpha", bg="#eef8fb", fg="#647782", font=("Helvetica", 14)).pack()

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

python3 "$HOME/.nlos/apps/nlos-dashboard.py" &
echo "OK : NLOS Dashboard installé."
