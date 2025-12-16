from customtkinter import *
from tkinter import messagebox


def ouvrir_lire(window , contacts) :

    lire_window = CTkToplevel(window)
    lire_window.title("📖 Lire un contact")
    lire_window.geometry('720x480')

    lire_window.grab_set() 

    

    main_frame = CTkFrame(lire_window, fg_color='white')
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)


    title_lbl = CTkLabel(main_frame, text='📖 Lire un contact', font=('Arial', 25, 'bold'))
    title_lbl.grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)

    verif_id_lbl = CTkLabel(main_frame , text='Votre ID :')
    verif_id_lbl.grid(row=1 , column=1 ,padx=20 , pady=50, sticky='e')

    verif_id_entry = CTkEntry(main_frame)
    verif_id_entry.grid(row=1 , column=2 , pady=50 , sticky='w')

    read_button = CTkButton(main_frame, text='📖 Lire un contact', width=50, height=40 , command= lambda:afficher_contact(verif_id_entry , affichage , contacts))
    read_button.grid(row=2, column=2, pady=20, sticky='ew')

    affichage = CTkTextbox(main_frame , width=500 , height=100 , fg_color= 'gray')
    affichage.grid(row=3 , column=2)

    annuler_bouton = CTkButton(main_frame , text='Annuler' , width=50, height=40, command=lire_window.destroy)
    annuler_bouton.grid(row=4 , column=2 , pady=20, sticky='ew')


def afficher_contact(verif_id_entry , affichage , contacts) :

    id = int(verif_id_entry.get())

    for contact in contacts :
        if id == contact["id"] :
            affichage.delete("0.0", END)  # vide la zone avant
            texte = f"ID: {contact['id']}\nNom: {contact['nom']}\nPrénom: {contact['prenom']}\nEmail: {contact['email']}\nTéléphone: {contact['telephone']}\n"
            affichage.insert("0.0", texte)
            return
    else :
        messagebox.showinfo("ID introuvable , Cet ID ne correspond à aucun Contact")

    verif_id_entry.delete(0, END)
    verif_id_entry.focus()