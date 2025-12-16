from customtkinter import *
from tkinter import messagebox
import json



def ouvrir_ajouter(window , contacts , dernier_id):

    ajouter_window = CTkToplevel(window)
    ajouter_window.title('➕ Ajouter un contact')
    ajouter_window.geometry('720x480')

  
    ajouter_window.grab_set()  # bloque la fenêtre principale

    

    main_frame = CTkFrame(ajouter_window, fg_color='white')
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Labels et Entries
    title_lbl = CTkLabel(main_frame, text='➕ Ajouter un contact', font=('Arial', 25, 'bold'))
    title_lbl.grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)

    nom_lbl = CTkLabel(main_frame, text="Nom :")
    nom_lbl.grid(row=1, column=1, sticky='e', padx=20, pady=10)
    nom_entry = CTkEntry(main_frame, width=250)
    nom_entry.grid(row=1, column=2, sticky='w')

    prenom_lbl = CTkLabel(main_frame, text="Prénom :")
    prenom_lbl.grid(row=2, column=1, sticky='e', padx=20, pady=10)
    prenom_entry = CTkEntry(main_frame, width=250)
    prenom_entry.grid(row=2, column=2, sticky='w')

    email_lbl = CTkLabel(main_frame, text="Email :")
    email_lbl.grid(row=3, column=1, sticky='e', padx=20, pady=10)
    email_entry = CTkEntry(main_frame, width=250)
    email_entry.grid(row=3, column=2, sticky='w')

    telephone_lbl = CTkLabel(main_frame, text="Téléphone :")
    telephone_lbl.grid(row=4, column=1, sticky='e', padx=20, pady=10)
    telephone_entry = CTkEntry(main_frame, width=250)
    telephone_entry.grid(row=4, column=2, sticky='w')

    valider_button = CTkButton(main_frame, text='Valider', height=40, command= lambda:valider_contact( dernier_id ,nom_entry, prenom_entry, email_entry, telephone_entry , contacts))
    valider_button.grid(row=5, column=1, sticky='ew', padx=5, pady=10)

    annuler_button = CTkButton(main_frame, text='Annuler', height=40, command= ajouter_window.destroy)
    annuler_button.grid(row=5, column=2, sticky='ew', padx=5, pady=10)

def valider_contact(dernier_id ,nom_entry, prenom_entry, email_entry, telephone_entry , contacts):

    nom = nom_entry.get().strip()
    prenom = prenom_entry.get().strip()
    email = email_entry.get().strip()
    telephone = telephone_entry.get().strip()

    if not nom or not prenom or not email or not telephone:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
        return

    dernier_id += 1
    contact = {
        "id": dernier_id,
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "telephone": telephone
    }

    contacts.append(contact)

    with open("data/backend.json", "w", encoding="utf-8") as f:
        json.dump({"dernier_id": dernier_id, "contacts": contacts}, f, indent=4, ensure_ascii=False)

    for entry in [nom_entry, prenom_entry, email_entry, telephone_entry]:
        entry.delete(0, END)
    nom_entry.focus()

    messagebox.showinfo("Succès", "Contact ajouté avec succès !")