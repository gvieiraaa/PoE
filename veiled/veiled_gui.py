import tkinter as tk
from tkinter import font
import json
import os

options = [
    "chance to deal Double Damage",
    "chance to deal Double Damage while Focused",
    "chance to Trigger Level 1 Blood Rage",
    "increased Attack Speed while a Rare or Unique",
    "increased Cast Speed, chance to gain Arcane Surge",
    "increased Damage per Endurance Charge",
    "increased Damage per Frenzy Charge",
    "increased Damage per Power Charge",
    "Dexterity, Intelligence, increased Attack Speed",
    "Strength, Dexterity, Accuracy",
    "Strength, Intelligence, Critical Strike Chance",
    "Multiplier while a Rare or Unique Enemy is Nearby",
    "Chaos Damage over Time Multiplier",
    "Fire Damage over Time Multiplier",
    "Physical Damage over Time Multiplier",
    "Minions have increased Attack Speed",
    "Trigger a Socketed Spell on Using a Skill",
]
def display_selections():
    selected_options = [var.get() for var in column_vars]
    if any(sel == "" for sel in selected_options) or len(set(selected_options)) != 3:
        exit()
    for o in selected_options:
        json_sum["mods"][o] += 1
    json_sum["veiled chaos count"] += 1
    json_all.append(selected_options)
    with open(f"{os.path.dirname(__file__)}/sum.json", "w") as f:
        json.dump(json_sum, f, indent=4)
    with open(f"{os.path.dirname(__file__)}/all.json", "w") as f:
        json.dump(json_all, f, indent=4)
    for var in column_vars:
        var.set("")


bg_color = "#333333"
fg_color = "#ffffff"
button_color = "#555555"

with open(f"{os.path.dirname(__file__)}/sum.json", "r") as f:
    json_sum = json.load(f)
with open(f"{os.path.dirname(__file__)}/all.json", "r") as f:
    json_all = json.load(f)

root = tk.Tk()
my_font = font.Font(size=13)
root.title("Unveil Options")
root.attributes("-topmost", True)
root.configure(bg=bg_color)

column_vars = [tk.StringVar(value="") for _ in range(3)]
radio_buttons = []

for i, option in enumerate(options):
    frame = tk.Frame(root, bg=bg_color)
    frame.pack(side="top", fill="x", padx=5, pady=5)
    label = tk.Label(frame, text=option, bg=bg_color, fg=fg_color)
    label.pack(side="right")
    
    for j in range(3):
        radio = tk.Radiobutton(frame, variable=column_vars[j], value=option, font=my_font, bg=bg_color)
        radio.pack(side="left")
        radio_buttons.append(radio)

submit_button = tk.Button(root, text="Ignore Attack speed, Acc, Crit Chance, Dex", command=display_selections)
submit_button.pack(side="bottom", fill="x", padx=5, pady=5)

root.mainloop()