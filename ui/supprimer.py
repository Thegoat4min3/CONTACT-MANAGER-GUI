from customtkinter import *
from tkinter import messagebox
import json


def ouvrir_supprimer(window , contacts , dernier_id):
    supp_window = CTkToplevel(window)
    supp_window.title('❌ Supprimer un contact')
    supp_window.geometry('720x480')
    supp_window.grab_set()

    


    main_frame = CTkFrame(supp_window , fg_color='white')
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)


    titlelbl = CTkLabel(main_frame, text='❌ Supprimer un contact' , font=('Arial' , 20 , 'bold'))
    titlelbl.grid(row=0 , column=2 , columnspan = 2)

    verif_id_lbl = CTkLabel(main_frame , text='Votre ID ici :')
    verif_id_lbl.grid(row=1 , column=1 , padx=5 , pady= 20 , sticky='e')

    verif_id_entry = CTkEntry(main_frame , width=250)
    verif_id_entry.grid(row=1 , column=2 , pady=20 , sticky='w')

    nom_lbl = CTkLabel(main_frame, text="Nom :")
    nom_lbl.grid(row=3, column=1, sticky='e', padx=5, pady=10)
    nom_entry = CTkEntry(main_frame, width=250)
    nom_entry.grid(row=3, column=2, sticky='w')

    prenom_lbl = CTkLabel(main_frame, text="Prénom :")
    prenom_lbl.grid(row=4, column=1, sticky='e', padx=5, pady=10)
    prenom_entry = CTkEntry(main_frame, width=250)
    prenom_entry.grid(row=4, column=2, sticky='w')

    email_lbl = CTkLabel(main_frame, text="Email :")
    email_lbl.grid(row=5, column=1, sticky='e', padx=5, pady=10)
    email_entry = CTkEntry(main_frame, width=250)
    email_entry.grid(row=5, column=2, sticky='w')

    telephone_lbl = CTkLabel(main_frame, text="Téléphone :")
    telephone_lbl.grid(row=6, column=1, sticky='e', padx=5, pady=10)
    telephone_entry = CTkEntry(main_frame, width=250)
    telephone_entry.grid(row=6, column=2, sticky='w')

    rechercher_btn = CTkButton(main_frame , text='Rechercher' , command= lambda: rechercher(verif_id_entry ,  nom_entry , prenom_entry ,email_entry, telephone_entry , contacts))
    rechercher_btn.grid(row=1 , column=3 ,  padx = 10 ,pady=20 , sticky='w')

    supp_button = CTkButton(main_frame, text='Supprimer', height=40 , width=200 , command=lambda: supprimer(supp_window ,verif_id_entry , contacts , dernier_id  , nom_entry , prenom_entry ,email_entry, telephone_entry))
    supp_button.grid(row=9, column=1, sticky='ew', padx=5, pady=10)

    annuler_button = CTkButton(main_frame, text='Annuler', height=40 ,  width=200, command=supp_window.destroy)
    annuler_button.grid(row=9, column=2, sticky='ew', padx=5, pady=10)

def rechercher(verif_id_entry ,  nom_entry , prenom_entry ,email_entry, telephone_entry , contacts):

    if  not verif_id_entry.get() :
        messagebox.showwarning('CHAMP VIDE','Veuillez remplir le champ ( ID ) SVP ')
        return
    
    messagebox.showinfo('CONFIRMATION ID' , "Etes-vous sur que c'est L'ID du contact que vous voulez supprimer ?")
    id = int(verif_id_entry.get())
    for contact in contacts :
        if id == contact['id'] :
            nom_entry.insert(0 , contacts[id - 1]['nom'])
            prenom_entry.insert(0 , contacts[id - 1]['prenom'])
            email_entry.insert(0 , contacts[id - 1]['email'])
            telephone_entry.insert(0, contacts[id - 1]['telephone'])
            return

    else :
        messagebox.showerror('EREUR ID' , 'Ce ID ne correspond à aucun contact\n Veuillez entrer le bon ID')
        verif_id_entry.delete(0 , END)
        nom_entry.delete(0 , END)
        prenom_entry.delete(0 , END)
        email_entry.delete(0 , END)
        telephone_entry.delete(0,END)
        return



def supprimer(supp_window ,verif_id_entry , contacts , dernier_id  , nom_entry , prenom_entry ,email_entry, telephone_entry):

    minifenetre = CTkToplevel(supp_window)
    minifenetre.geometry("300x150")
    minifenetre.grab_set()
    minifenetre.title("Confirmation")

    choix_var = StringVar(value="non")

    CTkLabel(minifenetre, text="Supprimer ce contact ?").pack(pady=10)

    CTkRadioButton(minifenetre, text="Oui",
                   variable=choix_var, value="oui").pack()

    CTkRadioButton(minifenetre, text="Non",
                   variable=choix_var, value="non").pack()
    
    CTkButton(minifenetre, text="Valider",command= lambda : valider( minifenetre , contacts ,dernier_id ,choix_var ,verif_id_entry ,nom_entry , prenom_entry ,email_entry, telephone_entry)).pack(pady=10)

def valider(minifenetre , contacts ,dernier_id, choix_var, verif_id_entry,nom_entry, prenom_entry, email_entry, telephone_entry):

    if choix_var.get() == "oui":
        id_recherche = int(verif_id_entry.get())

        for contact in contacts:
            if contact["id"] == id_recherche:
                contacts.remove(contact)
                break
        else:
            messagebox.showerror("Erreur", "Contact introuvable")
            return

        if id_recherche == dernier_id :
            dernier_id = dernier_id - 1
       
        with open("data/backend.json", "w", encoding="utf-8") as f:
            json.dump({"dernier_id": dernier_id, "contacts": contacts},f,indent=4,ensure_ascii=False)

        verif_id_entry.delete(0, END)
        nom_entry.delete(0, END)
        prenom_entry.delete(0, END)
        email_entry.delete(0, END)
        telephone_entry.delete(0, END)

        messagebox.showinfo("Suppression", "Contact supprimé avec succès")

    else:
        print("ANNULATION")

    minifenetre.destroy()


