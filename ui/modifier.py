from customtkinter import *
from tkinter import messagebox
import json

def ouvrir_modifier(window , contacts , dernier_id):
    modifier_window = CTkToplevel(window)
    modifier_window.title('✏️ Modifier un contact')
    modifier_window.geometry('720x480')
    modifier_window.grab_set() 

    

    main_frame = CTkFrame(modifier_window, fg_color='white')
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    title_lbl = CTkLabel(main_frame , text="✏️ Modifier un contact" , font=('Arial', 25, 'bold'))
    title_lbl.grid(row=0, column=2 , columnspan=2 , sticky='nsew')

    verif_id_lbl = CTkLabel(main_frame , text='Votre ID ici :')
    verif_id_lbl.grid(row=1 , column=1 , padx=10 , pady= 20 , sticky='e')

    verif_id_entry = CTkEntry(main_frame)
    verif_id_entry.grid(row=1 , column=2 , pady=20 , sticky='w')

    nom_lbl = CTkLabel(main_frame, text="Nom :")
    nom_lbl.grid(row=3, column=1, sticky='e', padx=20, pady=10)
    nom_entry = CTkEntry(main_frame, width=250)
    nom_entry.grid(row=3, column=2, sticky='w')

    prenom_lbl = CTkLabel(main_frame, text="Prénom :")
    prenom_lbl.grid(row=4, column=1, sticky='e', padx=20, pady=10)
    prenom_entry = CTkEntry(main_frame, width=250)
    prenom_entry.grid(row=4, column=2, sticky='w')

    email_lbl = CTkLabel(main_frame, text="Email :")
    email_lbl.grid(row=5 , column=1, sticky='e', padx=20, pady=10)
    email_entry = CTkEntry(main_frame, width=250)
    email_entry.grid(row=5, column=2, sticky='w')

    telephone_lbl = CTkLabel(main_frame, text="Téléphone :")
    telephone_lbl.grid(row=6, column=1, sticky='e', padx=20, pady=10)
    telephone_entry = CTkEntry(main_frame, width=250)
    telephone_entry.grid(row=6, column=2, sticky='w')

    search_button = CTkButton(main_frame , text='Rechercher', width=50, height=40 , command=lambda : rechercher_contact (verif_id_entry , contacts ,nom_entry , prenom_entry , email_entry , telephone_entry))
    search_button.grid(row=2 , column=2 , pady=20, sticky='ew')


    valider_button = CTkButton(main_frame, text='Valider', height=40,command=lambda: modifier_contact( verif_id_entry , contacts ,dernier_id , nom_entry , prenom_entry , email_entry , telephone_entry))
    valider_button.grid(row=7, column=1, sticky='ew', padx=5, pady=10)

    annuler_button = CTkButton(main_frame, text='Annuler', height=40 , command=modifier_window.destroy)
    annuler_button.grid(row=7, column=2, sticky='ew', padx=5, pady=10)


    def rechercher_contact (verif_id_entry , contacts ,nom_entry , prenom_entry , email_entry , telephone_entry):
        id = int(verif_id_entry.get())

        for contact in contacts :
            if id == contact["id"] :
                nom_entry.insert(0 ,contacts[id -  1 ]['nom'])
                prenom_entry.insert(0 ,contacts[id - 1]['prenom'] )
                email_entry.insert(0 ,contacts[id - 1]['email'])
                telephone_entry.insert(0 ,contacts[id -1 ]['telephone'])
                return
        else :
            messagebox.showinfo("ID introuvable , Cet ID ne correspond à aucun Contact")

    def modifier_contact( verif_id_entry , contacts ,dernier_id , nom_entry , prenom_entry , email_entry , telephone_entry) :

        id = int(verif_id_entry.get())

        for contact in contacts :
            if id == contact["id"] :
                contact['nom'] = nom_entry.get()
                contact['prenom'] = prenom_entry.get()
                contact['email'] = email_entry.get()
                contact['telephone'] = telephone_entry.get()

                if not nom_entry.get().strip() or not prenom_entry.get().strip() or not  email_entry.get().strip() or  not telephone_entry.get().strip() :
                    messagebox.showinfo("Champ Vide" , "Veuillez remplir tous les champs SVP")
                    return

                with open("data/backend.json" , 'w' , encoding="utf-8") as f :
                    json.dump({"dernier_id":dernier_id , "contacts":contacts} , f,indent=4, ensure_ascii=False)

                messagebox.showinfo("MODIFICATION" , "JOLIEEE , Le Contact a été modifié avec succes ")
                verif_id_entry.delete(0, END)
                verif_id_entry.focus()
                nom_entry.delete(0 , END)
                prenom_entry.delete(0 , END)
                email_entry.delete(0 , END)
                telephone_entry.delete(0 , END)
                return
                
        else :
            messagebox.showinfo("ID introuvable , Cet ID ne correspond à aucun Contact")

       
