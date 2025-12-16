from customtkinter import *
import json, os
from ui.ajouter import ouvrir_ajouter
from ui.lire import ouvrir_lire
from ui.modifier import ouvrir_modifier
from ui.supprimer import ouvrir_supprimer



# Charger les données
if os.path.exists("data/backend.json"):
    with open("data/backend.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            contacts = data["contacts"]
            dernier_id = data["dernier_id"]
        except:
            contacts = []
            dernier_id = 0
else:
    contacts = []
    dernier_id = 0

window = CTk()
window.title("Gestion Contacts")
window.geometry("720x580")
window.iconbitmap("icons/contact.ico")




# ---------- BOUTONS FENÊTRE PRINCIPALE ----------

title_lbl = CTkLabel(window, text='📇 GESTION DES CONTACTS', font=('Arial', 20, 'bold'), height=40)
title_lbl.grid(row=0, column=1, padx=230, pady=50, sticky='nsew')

add_button = CTkButton(window, text='➕ Ajouter un contact', width=50, height=40, command= lambda :ouvrir_ajouter(window , contacts , dernier_id))
add_button.grid(row=1, column=1, padx=100, pady=20, sticky='ew')

read_button = CTkButton(window, text='📖 Lire un contact', width=50, height=40, command= lambda : ouvrir_lire(window , contacts))
read_button.grid(row=2, column=1, padx=100, pady=20, sticky='ew')

edit_button = CTkButton(window, text='✏️ Modifier un contact', width=50, height=40, command= lambda :ouvrir_modifier(window, contacts, dernier_id))
edit_button.grid(row=3, column=1, padx=100, pady=20, sticky='ew')

delete_button = CTkButton(window, text='❌ Supprimer un contact', width=50, height=40, command= lambda :ouvrir_supprimer(window , contacts , dernier_id))
delete_button.grid(row=4, column=1, padx=100, pady=20, sticky='ew') 

quit_button = CTkButton(window, text='🚪 Quitter', width=50, height=40, command=window.destroy)
quit_button.grid(row=5, column=1, padx=100, pady=20, sticky='ew')

window.mainloop()
